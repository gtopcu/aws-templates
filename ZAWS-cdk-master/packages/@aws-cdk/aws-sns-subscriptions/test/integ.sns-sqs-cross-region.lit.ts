import * as sns from '@aws-cdk/aws-sns';
import * as sqs from '@aws-cdk/aws-sqs';
import * as cdk from '@aws-cdk/core';
import * as subs from '../lib';

/// !cdk-integ *
const app = new cdk.App();

/// !show
const topicStack = new cdk.Stack(app, 'TopicStack', {
  env: { account: process.env.CDK_DEFAULT_ACCOUNT, region: 'us-east-1' },
});
const topic = new sns.Topic(topicStack, 'MyTopic', {
  topicName: cdk.PhysicalName.GENERATE_IF_NEEDED,
});

const queueStack = new cdk.Stack(app, 'QueueStack', {
  env: { region: 'us-east-2' },
});
const queue = new sqs.Queue(queueStack, 'MyQueue');

topic.addSubscription(new subs.SqsSubscription(queue));
/// !hide

app.synth();
