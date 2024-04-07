

import * as escPaterns from 'aws-cdk-lib/aws_ecs_patterns';

const scheduledFargateTask = new ecsPatterns.ScheduledFargateTask(this, 'ScheduledFargateTask', {
  cluster,
  scheduledFargateTaskImageOptions: {
    image: ecs.ContainerImage.fromRegistry('amazon/amazon-ecs-sample'),
    memoryLimitMiB: 512,
  },
  
  schedule: appscaling.Schedule.expression('rate(1 minute)'),
});