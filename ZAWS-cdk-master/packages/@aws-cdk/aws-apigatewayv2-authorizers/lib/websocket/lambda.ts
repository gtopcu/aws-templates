import {
  WebSocketAuthorizer,
  WebSocketAuthorizerType,
  WebSocketRouteAuthorizerBindOptions,
  WebSocketRouteAuthorizerConfig,
  IWebSocketRouteAuthorizer,
  IWebSocketApi,
} from '@aws-cdk/aws-apigatewayv2';
import { ServicePrincipal } from '@aws-cdk/aws-iam';
import { IFunction } from '@aws-cdk/aws-lambda';
import { Stack, Names } from '@aws-cdk/core';

// keep this import separate from other imports to reduce chance for merge conflicts with v2-main
// eslint-disable-next-line no-duplicate-imports, import/order
import { Construct as CoreConstruct } from '@aws-cdk/core';

/**
 * Properties to initialize WebSocketTokenAuthorizer.
 */
export interface WebSocketLambdaAuthorizerProps {

  /**
   * The name of the authorizer
   * @default - same value as `id` passed in the constructor.
   */
  readonly authorizerName?: string;

  /**
   * The identity source for which authorization is requested.
   *
   * @default ['$request.header.Authorization']
   */
  readonly identitySource?: string[];
}

/**
 * Authorize WebSocket Api routes via a lambda function
 */
export class WebSocketLambdaAuthorizer implements IWebSocketRouteAuthorizer {
  private authorizer?: WebSocketAuthorizer;
  private webSocketApi?: IWebSocketApi;

  constructor(
    private readonly id: string,
    private readonly handler: IFunction,
    private readonly props: WebSocketLambdaAuthorizerProps = {}) {
  }

  public bind(options: WebSocketRouteAuthorizerBindOptions): WebSocketRouteAuthorizerConfig {
    if (this.webSocketApi && (this.webSocketApi.apiId !== options.route.webSocketApi.apiId)) {
      throw new Error('Cannot attach the same authorizer to multiple Apis');
    }

    if (!this.authorizer) {
      this.webSocketApi = options.route.webSocketApi;
      this.authorizer = new WebSocketAuthorizer(options.scope, this.id, {
        webSocketApi: options.route.webSocketApi,
        identitySource: this.props.identitySource ?? [
          '$request.header.Authorization',
        ],
        type: WebSocketAuthorizerType.LAMBDA,
        authorizerName: this.props.authorizerName ?? this.id,
        authorizerUri: lambdaAuthorizerArn(this.handler),
      });

      this.handler.addPermission(`${Names.nodeUniqueId(this.authorizer.node)}-Permission`, {
        scope: options.scope as CoreConstruct,
        principal: new ServicePrincipal('apigateway.amazonaws.com'),
        sourceArn: Stack.of(options.route).formatArn({
          service: 'execute-api',
          resource: options.route.webSocketApi.apiId,
          resourceName: `authorizers/${this.authorizer.authorizerId}`,
        }),
      });
    }

    return {
      authorizerId: this.authorizer.authorizerId,
      authorizationType: 'CUSTOM',
    };
  }
}

/**
 * constructs the authorizerURIArn.
 */
function lambdaAuthorizerArn(handler: IFunction) {
  return `arn:${Stack.of(handler).partition}:apigateway:${Stack.of(handler).region}:lambda:path/2015-03-31/functions/${handler.functionArn}/invocations`;
}
