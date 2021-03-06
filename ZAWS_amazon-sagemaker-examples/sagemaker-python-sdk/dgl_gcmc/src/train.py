"""Training script"""
import argparse
import json
import logging
import os
import random
import string
import time

import mxnet as mx
import numpy as np
from data import MovieLens
from model import BiDecoder, GCMCLayer
from mxnet import gluon
from mxnet.gluon import Block

from utils import (
    MetricLogger,
    get_activation,
    gluon_net_info,
    gluon_total_param_num,
    params_clip_global_norm,
    parse_ctx,
)

os.system("python3 -m spacy download en")


class Net(Block):
    def __init__(self, args, **kwargs):
        super(Net, self).__init__(**kwargs)
        self._act = get_activation(args.model_activation)
        with self.name_scope():
            self.encoder = GCMCLayer(
                args.rating_vals,
                args.src_in_units,
                args.dst_in_units,
                args.gcn_agg_units,
                args.gcn_out_units,
                args.gcn_dropout,
                args.gcn_agg_accum,
                agg_act=self._act,
                share_user_item_param=args.share_param,
            )
            self.decoder = BiDecoder(
                args.rating_vals,
                in_units=args.gcn_out_units,
                num_basis_functions=args.gen_r_num_basis_func,
            )

    def forward(self, enc_graph, dec_graph, ufeat, ifeat):
        user_out, movie_out = self.encoder(enc_graph, ufeat, ifeat)
        pred_ratings = self.decoder(dec_graph, user_out, movie_out)
        return pred_ratings


def evaluate(args, net, dataset, segment="valid"):
    possible_rating_values = dataset.possible_rating_values
    nd_possible_rating_values = mx.nd.array(possible_rating_values, ctx=args.ctx, dtype=np.float32)

    if segment == "valid":
        rating_values = dataset.valid_truths
        enc_graph = dataset.valid_enc_graph
        dec_graph = dataset.valid_dec_graph
    elif segment == "test":
        rating_values = dataset.test_truths
        enc_graph = dataset.test_enc_graph
        dec_graph = dataset.test_dec_graph
    else:
        raise NotImplementedError

    # Evaluate RMSE
    with mx.autograd.predict_mode():
        pred_ratings = net(enc_graph, dec_graph, dataset.user_feature, dataset.movie_feature)
    real_pred_ratings = (
        mx.nd.softmax(pred_ratings, axis=1) * nd_possible_rating_values.reshape((1, -1))
    ).sum(axis=1)
    rmse = mx.nd.square(real_pred_ratings - rating_values).mean().asscalar()
    rmse = np.sqrt(rmse)
    return rmse


def train(args):
    print(args)
    dataset = MovieLens(
        args.data_name,
        args.ctx,
        use_one_hot_fea=args.use_one_hot_fea,
        symm=args.gcn_agg_norm_symm,
        test_ratio=args.data_test_ratio,
        valid_ratio=args.data_valid_ratio,
    )
    print("Loading data finished ...\n")

    args.src_in_units = dataset.user_feature_shape[1]
    args.dst_in_units = dataset.movie_feature_shape[1]
    args.rating_vals = dataset.possible_rating_values

    ### build the net
    net = Net(args=args)
    net.initialize(init=mx.init.Xavier(factor_type="in"), ctx=args.ctx)
    net.hybridize()
    nd_possible_rating_values = mx.nd.array(
        dataset.possible_rating_values, ctx=args.ctx, dtype=np.float32
    )
    rating_loss_net = gluon.loss.SoftmaxCELoss()
    rating_loss_net.hybridize()
    trainer = gluon.Trainer(
        net.collect_params(), args.train_optimizer, {"learning_rate": args.train_lr}
    )
    print("Loading network finished ...\n")

    ### perpare training data
    train_gt_labels = dataset.train_labels
    train_gt_ratings = dataset.train_truths

    ### prepare the logger
    train_loss_logger = MetricLogger(
        ["iter", "loss", "rmse"],
        ["%d", "%.4f", "%.4f"],
        os.path.join(args.save_dir, "train_loss%d.csv" % args.save_id),
    )
    valid_loss_logger = MetricLogger(
        ["iter", "rmse"],
        ["%d", "%.4f"],
        os.path.join(args.save_dir, "valid_loss%d.csv" % args.save_id),
    )
    test_loss_logger = MetricLogger(
        ["iter", "rmse"],
        ["%d", "%.4f"],
        os.path.join(args.save_dir, "test_loss%d.csv" % args.save_id),
    )

    ### declare the loss information
    best_valid_rmse = np.inf
    no_better_valid = 0
    best_iter = -1
    avg_gnorm = 0
    count_rmse = 0
    count_num = 0
    count_loss = 0

    print("Start training ...")
    dur = []
    for iter_idx in range(1, args.train_max_iter):
        if iter_idx > 3:
            t0 = time.time()
        with mx.autograd.record():
            pred_ratings = net(
                dataset.train_enc_graph,
                dataset.train_dec_graph,
                dataset.user_feature,
                dataset.movie_feature,
            )
            loss = rating_loss_net(pred_ratings, train_gt_labels).mean()
            loss.backward()

        count_loss += loss.asscalar()
        gnorm = params_clip_global_norm(net.collect_params(), args.train_grad_clip, args.ctx)
        avg_gnorm += gnorm
        trainer.step(1.0)
        if iter_idx > 3:
            dur.append(time.time() - t0)

        if iter_idx == 1:
            print("Total #Param of net: %d" % (gluon_total_param_num(net)))
            print(
                gluon_net_info(
                    net, save_path=os.path.join(args.save_dir, "net%d.txt" % args.save_id)
                )
            )

        real_pred_ratings = (
            mx.nd.softmax(pred_ratings, axis=1) * nd_possible_rating_values.reshape((1, -1))
        ).sum(axis=1)
        rmse = mx.nd.square(real_pred_ratings - train_gt_ratings).sum()
        count_rmse += rmse.asscalar()
        count_num += pred_ratings.shape[0]

        if iter_idx % args.train_log_interval == 0:
            train_loss_logger.log(
                iter=iter_idx, loss=count_loss / (iter_idx + 1), rmse=count_rmse / count_num
            )
            logging_str = "Iter={}, gnorm={:.3f}, loss={:.4f}, rmse={:.4f}, time={:.4f}".format(
                iter_idx,
                avg_gnorm / args.train_log_interval,
                count_loss / iter_idx,
                count_rmse / count_num,
                np.average(dur),
            )
            avg_gnorm = 0
            count_rmse = 0
            count_num = 0

        if iter_idx % args.train_valid_interval == 0:
            valid_rmse = evaluate(args=args, net=net, dataset=dataset, segment="valid")
            valid_loss_logger.log(iter=iter_idx, rmse=valid_rmse)
            logging_str += ",\tVal RMSE={:.4f}".format(valid_rmse)

            if valid_rmse < best_valid_rmse:
                best_valid_rmse = valid_rmse
                no_better_valid = 0
                best_iter = iter_idx
                net.save_parameters(
                    filename=os.path.join(
                        args.save_dir, "best_valid_net{}.params".format(args.save_id)
                    )
                )
                test_rmse = evaluate(args=args, net=net, dataset=dataset, segment="test")
                best_test_rmse = test_rmse
                test_loss_logger.log(iter=iter_idx, rmse=test_rmse)
                logging_str += ", Test RMSE={:.4f}".format(test_rmse)
            else:
                no_better_valid += 1
                if (
                    no_better_valid > args.train_early_stopping_patience
                    and trainer.learning_rate <= args.train_min_lr
                ):
                    logging.info("Early stopping threshold reached. Stop training.")
                    break
                if no_better_valid > args.train_decay_patience:
                    new_lr = max(
                        trainer.learning_rate * args.train_lr_decay_factor, args.train_min_lr
                    )
                    if new_lr < trainer.learning_rate:
                        logging.info("\tChange the LR to %g" % new_lr)
                        trainer.set_learning_rate(new_lr)
                        no_better_valid = 0
        if iter_idx % args.train_log_interval == 0:
            print(logging_str)
    print(
        "Best Iter Idx={}, Best Valid RMSE={:.4f}, Best Test RMSE={:.4f}".format(
            best_iter, best_valid_rmse, best_test_rmse
        )
    )
    train_loss_logger.close()
    valid_loss_logger.close()
    test_loss_logger.close()


def config():
    parser = argparse.ArgumentParser(description="Run the baseline method.")

    parser.add_argument("--seed", default=123, type=int)
    parser.add_argument(
        "--ctx",
        dest="ctx",
        default="gpu0",
        type=str,
        help="Running Context. E.g `--ctx gpu` or `--ctx gpu0,gpu1` or `--ctx cpu`",
    )
    parser.add_argument("--save_dir", type=str, help="The saving directory")
    parser.add_argument("--save_id", type=int, help="The saving log id")
    parser.add_argument("--silent", action="store_true")

    parser.add_argument(
        "--data_name", default="ml-1m", type=str, help="The dataset name: ml-100k, ml-1m, ml-10m"
    )
    parser.add_argument(
        "--data_test_ratio", type=float, default=0.1
    )  ## for ml-100k the test ration is 0.2
    parser.add_argument("--data_valid_ratio", type=float, default=0.1)
    parser.add_argument("--use_one_hot_fea", action="store_true", default=False)

    # parser.add_argument('--model_remove_rating', type=bool, default=False)
    parser.add_argument("--model_activation", type=str, default="leaky")

    parser.add_argument("--gcn_dropout", type=float, default=0.7)
    parser.add_argument("--gcn_agg_norm_symm", type=bool, default=True)
    parser.add_argument("--gcn_agg_units", type=int, default=500)
    parser.add_argument("--gcn_agg_accum", type=str, default="sum")
    parser.add_argument("--gcn_out_units", type=int, default=75)

    parser.add_argument("--gen_r_num_basis_func", type=int, default=2)

    # parser.add_argument('--train_rating_batch_size', type=int, default=10000)
    parser.add_argument("--train_max_iter", type=int, default=2000)
    parser.add_argument("--train_log_interval", type=int, default=1)
    parser.add_argument("--train_valid_interval", type=int, default=1)
    parser.add_argument("--train_optimizer", type=str, default="adam")
    parser.add_argument("--train_grad_clip", type=float, default=1.0)
    parser.add_argument("--train_lr", type=float, default=0.01)
    parser.add_argument("--train_min_lr", type=float, default=0.001)
    parser.add_argument("--train_lr_decay_factor", type=float, default=0.5)
    parser.add_argument("--train_decay_patience", type=int, default=50)
    parser.add_argument("--train_early_stopping_patience", type=int, default=100)
    parser.add_argument("--share_param", default=False, action="store_true")

    args = parser.parse_args()
    return args


if __name__ == "__main__":
    args = config()

    args.ctx = parse_ctx(args.ctx)[0]
    print(args.ctx)

    ### configure save_dir to save all the info
    if args.save_dir is None:
        args.save_dir = (
            args.data_name
            + "_"
            + "".join(random.choices(string.ascii_uppercase + string.digits, k=2))
        )
    if args.save_id is None:
        args.save_id = np.random.randint(20)
    args.save_dir = os.path.join(os.environ["SM_MODEL_DIR"], args.save_dir)
    if not os.path.isdir(args.save_dir):
        os.makedirs(args.save_dir)

    # PIN the seed
    if args.seed != -1:
        np.random.seed(args.seed)
        mx.random.seed(args.seed, args.ctx)
    train(args)
