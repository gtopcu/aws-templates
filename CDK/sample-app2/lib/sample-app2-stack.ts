//https://www.youtube.com/watch?v=_kf4ajni3Qk
import { Stack, StackProps } from 'aws-cdk-lib';
import { Construct } from 'constructs';
import * as sqs from 'aws-cdk-lib/aws-sqs';

//cdk init app --language typescript
//cdk bootstrap
//cdk synth
//cdk deploy
//cdk watch
//cdk destroy

export class SampleApp2Stack extends Stack {
  constructor(scope: Construct, id: string, props?: StackProps) {
    super(scope, id, props);
    /*
    // The code that defines your stack goes here
    // example resource
    const queue = new sqs.Queue(this, 'SampleApp2Queue', {
       visibilityTimeout: cdk.Duration.seconds(300)
    });
    */
  }
  
}
