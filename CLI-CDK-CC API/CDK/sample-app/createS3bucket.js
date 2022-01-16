
//https://docs.aws.amazon.com/cdk/v2/guide/hello_world.html

const cdk = require('aws-cdk-lib');
const s3 = require('aws-cdk-lib/aws-s3');

class HelloCdkStack extends cdk.Stack {
  constructor(scope, id, props) {
    super(scope, id, props);

    new s3.Bucket(this, 'MyFirstCDKBucket', {
      versioned: true
    });
  }
}

module.exports = { HelloCdkStack }