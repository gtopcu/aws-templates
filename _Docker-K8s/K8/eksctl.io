
https://eksctl.io/

export EKSCTL_ENABLE_CREDENTIAL_CACHE=1

eksctl get cluster [--name=<name>] [--region=<region>]
eksctl delete cluster --name=<name> [--region=<region>]

eksctl create cluster --name=cluster-1 --nodes=2 --version=1.28 --region us-east-1 \
                        --nodegroup-name k8nodes --node-type t2.micro \
                        --node-volume-size=50 --node-volume-type=gp2 \
                        --tags environment=staging

eksctl create cluster --name=cluster-5 --nodes-min=3 --nodes-max=5 -> autoscaling
eksctl create cluster --config-file=<path> --without-nodegroup
eksctl create cluster --name=cluster-2 --nodes=4 --kubeconfig=./kubeconfig.cluster-2.yaml

SSH
eksctl create cluster --enable-ssm -> Enable system manager SSH
~/.ssh/id_rsa.pub
eksctl create cluster --ssh-access --ssh-public-key=my_eks_node_id.pub                      -> custom public key
eksctl create cluster --ssh-access --ssh-public-key=my_kubernetes_key --region=us-east-1    -> existing EC2 keypair


eksctl create cluster -f cluster.yaml

apiVersion: eksctl.io/v1alpha5
kind: ClusterConfig

metadata:
  name: basic-cluster
  region: eu-north-1

nodeGroups:
  - name: ng-1
    instanceType: m5.large
    desiredCapacity: 10
  - name: ng-2
    instanceType: m5.xlarge
    desiredCapacity: 2