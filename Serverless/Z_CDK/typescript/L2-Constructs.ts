

import * as s3 from 'aws-cdk-lib/aws-s3';
import * as lambda from 'aws-cdk-lib/aws-lambda';

const bucket = new s3.Bucket(app, 'Bucket', {
  bucketName: "mybucketname",
  blockPublicAccess: s3.BlockPublicAccess.BLOCK_ALL,
  versioned: true,
});

new lambda.Function(app, 'Function', {
  runtime: lambda.Runtime.NODEJS_14_X,
  handler: 'index.handler',
  code: lambda.Code.fromAsset('lambda'),
  environment: {
    BUCKET_NAME: bucket.bucketName,
  },
});