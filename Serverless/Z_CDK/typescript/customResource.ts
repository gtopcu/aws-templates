

const getParametersCustomResource = new AwsCustomResource(
    scope,
  `GetParam${parameterName}`,
  {
    onCreate: {
      service: "SSM",
      action: "GetParameter",
      parameters: {
        Name: Fn.join("/", ["/", project, environment, parameterName]),
      },
      region: "eu-east-1",
      physicalResourceId: PhysicalResourceId.of(`GetParam${parameterName}`),
    },
    policy: AwsCustomResourcePolicy.fromSdkCalls({
      resources: AwsCustomResourcePolicy.ANY_RESOURCE,
    }),
  }
);