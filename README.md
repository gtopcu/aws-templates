# Serverless Notes

````sh
pip freeze | grep -i llama
ls -al -> ll  
````

General:
- Enable CloudTrail management & data events(i.e.S3 put)
- Enable IAM AccessAdvisor & CloudTrail(90 days default) -> CW/S3 & Insights
- Utilize organanizations & identitiy center, control tower, config, inspector, detective, guardduty, securityhub, codeguru, devopsguru, WAF & FirewallManager, ServiceQuotas, Health, Budgets, SavingPlans, ComputeOptimizer, Backup, Sys/Secrets Mgr, TrustedAdvisor, ResourceExplorer, TagEditor

Lambda:
- 128MB-10GB memory, 256kb async/6MB sync/20MB streaming payload, 15m timeout, /tmp 10GB ephemeral(durable & shared until cold)
- More memory = more vCPU + IO. 128MB -> 0.5vCPU, 1.8GB -> 1vCPU, 10GB -> 6vCPU, 1000 max concurrency per region
- 1 million requests & 400.000GB free. Pricing: number of requests & duration. Use Lambda PowerTuning SF to tune
- 50MB zipped 250MB unzipped including layers. 3MB console max, 10GB uncompressed for container lambdas. 10 extensions max
- Concurrency = RPS x duration in seconds
- Invocations Types -> sync: API GW, Lambda, Cognito, async: S3/EventBridge/SNS, polling: SQS, streaming: Kinesis/DynamoStreams
- To avoid cold starts: use min libs, set provisioned concurrency if necessary, define DB conn. etc outside handler method
- Type of errors:
  * Invocation errors(throttles, large size, permissions - for async invocations, retries 2 times for max 6 hours by default)
  * Function errors(function error, timeout)
- For invocation errors, can use Lambda DLQ or destinations(preferred, contains more data) (errors are delivered after all retries)
   -> success & fail for async(targets: S3/SQS/SNS/EventBridge/Lambda), fails only for streaming(targets: S3/SQS/SNS)
- Use reserved & provisioned concurrency as necessary. +1000 concurrency per 10seconds
- Use CW application insights & lambda insights (extension) for overall picture
- IAM PassRole -> Trust Policiy -> STS assumeRole
- Utilize lambda layers for NPM/pip packages (50MB compressed, 256MB uncompressed limit)
- Use the latest Lambda PowerTools as a layer
- Can filter messages(no charge)
- FunctionURLs are new, supports IAM or no auth
- SnapStart -> Python, .Net, Java 11/17 Spring Boot over 10sec lowers to <1 sec. beforeCheckpoint/afterRestore hooks
- For polling errors(SQS) -> refer to SQS notes, for streaming errors(Kinesis/DynamoDB Streams) -> refer to Kinesis notes

API GW:
- 10k req/s 30sec(can raise) 10MB max. Billed by million requests & cache size x hour, 1 million calls free per month for 12 months
- Regional, EdgeOptimized(CloudFront provides DDoS protection), Private(VPC endpoints)
- Log request_ids in your clients
- Direct service integration -> returns request_id for tracking
- API GW -> SQS -> SQS message_id -> can be tracked by client
- API Keys & usage plans, access logging, request validaton, throttling/caching, SDK generation, OIDC authentication, canary deployments per stage
- Set CW alarms using custom metrics & metric filters, utilize CW log insights & dashboards and X-Ray for tracing
- Use resource policies to restrict access to AWS accounts/users, VPCs, IPs etc
- Documentation, API keys, testing, monitization -> apiable.io, readme.com, AWS DataExchange
- Lambda Authorizer uses lambda concurrency, use auth caching - 5 min to 1 hour
- IAM auth useful for internal APIs, use WAF for public APIs
- HTTP APIs: Up to %40 faster & %30 cheaper compared to Rest APIs. OIDC/OAuth2 & Lambda Auth. Lambda & HTTP integration, no WAF etc
- WebSocket APIs: One Way or Bidiractional. Routes, Stages, API Key auth. Lambda, HTTP & AWS Service Integration (i.e. Kinesis)
- Edge-Optimized: Not charged separately for CloudFront - managed by API GW
- Private APIs: Can only be deployed to a single VPC. No data out charge, but charged for PrivateLink. Cannot convert to edge
- Caching: Charged per hour/GB, not per how many responses are stored. So track CloudWatch Metrics CacheHitCount and CacheMissCount
  Create a timestamp and include it in your API response.
- Mock integration: For hardcoded responses - i.e. healthchecks. No backend integration invoked
- Creating resources with path param: https://api_id.execute-API.region-id.amazon.com/stage/mypetapi/pets/{petName}
  (or /{proxy+} -> creates HTTP method ANY)
- API GW -> VPC Link -> Network Load Balancer -> EC2 in private subnet
- When testing from console, API calls are real, but CW logs are simulated, no logs written
- Stages: Catching, throttling & usage plans. SDK generation, import/export OpenAPI definition, canary deployments
- Stage variables: $stageVariables.[variable name]  -> i.e. Lambda Integration function name: ${stageVariables.lambdaFn}
- Map lambda aliases with stage variables to API GW stages -> Weighted traffic
- Can import existing OpenAPI 3.0.3 into SAM template
https://explore.skillbuilder.aws/learn/course/52/play/41664/amazon-api-gateway-for-serverless-applications;lp=92
- IAM Auth: Access key/secret access key must be in the header computed using SigV4 to compute a HMAC signature using SHA256
  IAM user / assume an IAM role
- Lambda Authorizer: Token (oauth, bearer) or Request(query strings, path param, method, headers, http method etch)
- API keys: x-API-key header
- Usage plans:  API Key Throttling per second and burst
                API Key Quota by day, week, or month
                API Key Usage by daily usage records
- Who can invoke the API: To call a deployed API, or refresh the API caching, the caller needs the execute-api permission
- Who can manage the API: To create, deploy, and manage an API in API Gateway, the API developer needs the apigateway permission
- CloudTrail captures all API calls for API Gateway as events. IP address, requester, and time of request are included.
  Event history can be reviewed. Create a trail to send events to a S3 bucket.
- Transformations(mapping templates, can now be in JS):
    $input: Body, json, params, path
    $stageVariables
    $util: escapeJavaScript(), parseJson(), urlEncode/Decode(), base64Encode/Decode()
- Gateway responses for invalid requests can be modified: Change HTTP status code. modify body content, add headers
  Can also customize specific responses or modify the default 4xx or 5xx error response.
- Request validation: can check required request parameters in the URL, query string, and headers are present
  Can also check the applicable request payload adheres to the configured JSON request model of the method
- No error handling for lambda(sync) -> Generate SDK from the API stage, and use the backoff and retry mechanisms it provides

DynamoDB:
- 400KB max item size, 2KB for PK & 1KB for SK, String, Number. Binary, Boolean or List, Map, Set (these can be 32 levels deep)
- 2 x 4KB Reads per RCU (eventually consistent), 1 x 1KB Write per RCU (%50 capacity for consistent reads & transactions)
- PutItem, UpdateItem, DeleteItem, GetItem, Query, Scan, BatchGetItems, BatchWriteItems, TransactWriteItems
- LocalSecondaryIndexes (5 max per table):
    * Index is local to a partition key
    * Allows you to query items with the same partition key – specified with the query. All the items with a particular partition key in the table and the items in the corresponding local secondary index (together known as an item collection) are stored on the same partition. The total size of an item collection cannot exceed 10 GB
    * The partition key is the same as the table’s partition key. The sort key can be any scalar attribute.
    * Can only be created when a table is created and cannot be deleted
    * Supports eventual consistency and strong consistency
    * Uses table's provisioned throughput- so do not project all attributes also 10GB limit!
    * Queries can return attributes that are not projected into the index
- GlobalSecondaryIndexes (20 max per table):
    * Index is across all partition keys. Same design principles apply as a regular table (hot partitions etc)
    * Allows you to query over the entire table, across all partitions
    * Can have a partition key and optional sort key that are different from the partition key and sort key of the original table
    * Key values do not need to be unique
    * Can be created when a table is created or can be added to an existing table and it can be deleted
    * Supports eventual consistency only
    * Has its own provisioned throughput settings for read and write operations
      -> Too high WCU will throttle the base table ! But reads do not affect, so can be used for heavy reads/scans
    * Queries only return attributes that are projected into the index
- On Prod:
  * Enable DynamoDB control API operations using CloudTrail
  * Log AWS error codes to CW logs
  * Enable CW ContributorInsights & CW alarms based on DynamoDB metrics for throttling & monitoring & hot PKs
  * Always use PIT recovery(any second within 35 days, no CUs used)
  * on-Demand Backup(almost instant, for >35 days, no CUs used), Restore(up to 12 hours)
  * Enable DeletionProtection for tables
- on-Demand can scale x2 previous read/write peaks within 30 minutes
- Provisioned can use auto-scaling, manages RCU/WCU separately both for table/GSIs based on CloudWatch metrics, can schedule
- DynamoDB Streams(exactly once but with lambda at least once, ordered by key, stays for 24 hours, subsecond delivery)
- Global Tables(%99.999 SLA instead of %99.99), only eventually consistent if not writing to same region, need to handle all writes
- 3,000 RCU and 1,000 WCU max per partition per table (max limit) - burst capacity preserved for up to 5mins
- Dynamo IA -> %60 cheaper on storage, %25 more expensive on reads & writes
- TTL expiration(can be any attribute, must be epoch time, may take 1-2 days, does not use CUs) -> or Streams->Lambda->Firehose->S3
- LeadingKeys IAM action on PKs for owner access
- Handle partial failures: BatchGetItem(GetItem): Unprocessed Keys and BatchWriteItem(PutItem, DeleteItem): Unprocessed Items
- Utilize VPC endpoints, DAX(only in same VPC & write thru)
- Design considerations: Avoid hot partitions, only use indexes if must, utilize write sharding, separate hot/cold tabbles, scatter/gather for large items, sparse indexes, STD, one-to-many(for many attributes), separate table for frequently used attributes(varied access pattern), optimistic locking(update ConditionExpression:versionNo=1) etc

SQS:
- Message size 256KB(max) default. Up to 2GB with Extended Client Library for Python/Java 
- Retention 4 days default (1 min - 14 days)
- Visibility timeout 30sec default (0 sec - 12 hours) Set 6 x Lambda timeout
- Delivery delay(0 - 15 mins), receive message wait time(0 - 20 secs), long polling
- SQS FIFO 70kTPS, 700kTPS with batching. Now also supports redrive, requires MessageGroupId, can de-duplicate by 
  MessageDeduplicationId(5min idempotency), order guaranteed within group, 120k in-flight max 
- Only use MaximumConcurrency setting on the queue with lambda, do not use ReservedConcurrency(leads to overpolling)
- Use correlationID & return address to track the message on the sender
- Batching:
  * Lambda timeout = no of messages (batch size) x avg message processing time
  * 10 messages max per batch(default), max 256kb total
  * Can set up batch window in seconds(max wait time for messages)
- Concurrent Batches per Shard:
  * 10 messages max per batch(default 5)
  * Starts with 5 concurrent lambdas max, scales down in case of errors, scales up if more messages
    (up to 1000 batches max, increases 300 parallel pollers per min)
- Error Handling(batchItemFailures -> check PowerTools batch):
    * If an invocation fails or times out, message is available again when the visibility timeout period expires
    * Lambda retries until successful or the queue’s maxReceiveCount(1-1000, default 2) limit has been exceeded
    * Can splitBatchOnError, maxAgeOfRecord (check Kinesis)
    * Define the DLQ on SQS, not Lambda
    * ApproximateAgeOfOldestMessage CloudWatch Metric + Alarm, queue redrive + event forking pipeline

SNS:
- Can filter/retry, filter PII data. Supports 3rd party HTTP. Fan-out to multiple SQS.
- FIFO (3000TPS) can now deliver to non-FIFO, now support archiving & replays , 5 min idempotency
- Supports millions of subscribers with small latency (<100ms)
- Async event sources(SNS, S3, EventBridge) do not wait for callback from lambda(no timeout), passes it to the lambda handler
- Lambda invocation errors(throttling/large size/timeout):
    * Retries 2 times defeault (RetryAttempts) for max of 6 hours default (Maximum Event Age)
    * Performs 3 immediate tries, 2 at 1 second apart, 10 backing off from 1 second to 20 seconds, and 100,000 at 20 seconds apart
    * Can also define DLQ on the topic

EventBridge:
- 70ms latency avg, 24 hour retry max, 256KB max 1$ per 1 million events, free delivery to AWS services, 5 receivers max per rule
- Use versions in events & schema registry
- Use open source EventBridge Atlas for visualization
- In dev/test, use archive/replay for live events(replays get new messageID!). Send to CW logs & tail logs for debugging
- EventBridge scheduler: 1 time or recurring, timezone support, start/end time, flexible window
- API destinations 24 hours retry max 300TPS default
- EventBridge Pipes:
  - 1 to 1 mapping, source -> target only. Supports all integrations as the EB
  - Maintains message order - uses event source mapping underneath
  - Set MaxRetryAttempt for polling (default: -1 inifinite!)
  - Set batch size(10 default), batch window(5 sec default), no of concurrent batches per shard, on error config for polling
  - Backs of 1 retry per minute

StepFunctions:
- Request-response, WaitForCallback(.waitForTaskToken $$.Task.Token - Standard only), RunJob(.sync). 90 day idempotency
  https://www.youtube.com/watch?v=SbL3a9YOW7s
- StartExecution API, retry/catch(States.ALL), retry jitter, no default timeout, wait(sleep), intrinsic functions
- 256KB max payload limit. Map & DistributedMap for parallel data processing
- Choice states do not have catch/retry
- Standard: 1 year max, async, exactly once. Express: 5 min max, sync/async execution, at least once
- Standard billed per no. of state transitions($25/million), express billed by duration($1/million + $0.000001/5GB-s)
- Use SFs if cannot guarantee idempotent lambdas
- Call express workflows from standard workflows for high speed/data processing/callback etc

Kinesis:
- DataStreams PartitionKey & SequenceNumber(unique per partition), ordered & at least once(idempotency!), replays, errors, base64 encoded
- 1-365 days storage, now supports serverless & multiple consumers per shard, ~50$ per shard
- DataStreams Write 1000RPS & 1MB/sec, Read 10kRPS 5t/sec 2MB/sec total per shard (shared between consumers)
- Enhanced fan-out - more consumers, push instead of pull, each consumer gets 2MB/s, 50-70 milisecs latency, 5min timeout max, uses HTTP/2
- DataStreams on-Demand can scale x2 the 30 last 30 days peak, will throttle >x2 spikes in less than 15 mins
- Automatic retries for HTTP 5xx errors up to 3 times with exponential backoff, 2 min timeout default
- AWS SDK putRecords(params, callback) up to 500 records / 5MiB. Handle partial failures!
- Lamda Event Source Mapping: 1 batch = 1 lambda instance. Batch size 1-10000 records, window 1 sec up to 5 min, 6MB payload limit
- 1 shard = 1 concurrent lambda -> can be up to 10 by setting ParallelizationFactor(no of batches to processed concurrently per shard)
- DataStreams aggregation to send/receive multiple records per record -> Kinesis Aggregation Library for Lambda
- DataStreams pricing based on storage duraction, no of open shards & data size. on-Demand up to %300 more expensive than Previsioned
- Firehose -> S3, OpenSearch, buffers, transform/filter/enrich, no order guarantee, at least once, single target, does 3 retries
- Firehose -> S3 batching: 1 to 15 minutes, or 1GBB to 128GBs
- Lambda Erorrs:
  * Lambda retries the entire batch until success or data expiration(at least 1 day!) No other batches are processed (poison pill)
  * BisectBatchOnFunctionError, MaximumRetryAttempts(0-1000, default 1), MaximumRecordAge 1 min(default) up to 7 days
  * on-failure destination: can use SQS/SNS as failure destination
  * Configure an OnFailure destination on Lambda so that when a data record reaches the MaximumRetryAttempts or MaximumRecordAge,
    you can send its metadata, such as shard ID and stream ARN to SQS/SNS
  * Check Iterator-Age metric for oldest messages
  * Can return partial success - check PowerTools batching

S3:
- StorageLens, AccessPoints, 2-buckets multi-region APs, S3 Select/Express/MountPoints, Athena/Glue Databew
- EventBridge can better filter & transform S3 events but more expensive(enable CloudTrail data events)
- Use multi-part uploads & byte range fetches for efficiency
- Ideal object size: 12-16MB
- 3500TPS PUT/POST/DELETE vs 5000TPS HEAD/GET. 100K TPS for Express One Zone

CloudFormation:
- Utilize rollback config based on CW alarms
- git sync, CF hooks, cfn-lint, timeline view(

Cognito:
- OpenID providers, sync lambda triggers, AI powered fraud detection

Redis:
- Key/Value, Sets, SortedSets great for real-time leaderboards, Geolocation, Multi-AZ
- Valkey %30 price, same SDK and features

<br/>

# General AWS Best Practices

Security & Ops
- Enable password rotation/policies & MFA for root & save the QR code. - IAM supports PCI DSS
- Delete root user access keys & create custom login alias URL
- Enable IAM Identity Center(formerly SSO), Identity Federation thru Octa/Oauth/AD etc
- Set up Organization & Service/Resource Control Policies, TagPolicies & BackupPolicies per account
- Enable ControlTower on the Organization account & use account factory
- Deploy Landing Zone Accelerator to configure the new accounts
- Enable CloudTrail for all accounts for management events & put logs to CW & S3
- Use PowerUserAccess role for admins instead of Administrator (no IAM/org/account)
- Organization account Security Hub -> Enable SecurityHub, GuardDuty, Detective, Macie, ControlTower, Config etc (https://youtube.com/watch?v=jPGERcPM5G4)
- Enable AWS Chatbot to receive SecurityHub/CW Alert etc notifications in Slack/Chime
- To detect PII data, use Macie for S3 buckets, and Comprehend/Glue Studio transform for anything else
- AWS Artifact & Landing Zone Accelerator for PCI/HIPAA etc certifications & improve overall architectural security
- Setup conformance packs (PCI-DSS etc) in AWS Config
- Setup log & trail collection & S3 buckets replication to security account CW & S3
- Enable IAM Access Advisor & Analyzer on all accounts
- Enable VPC flow logs for ECS/CF/API GW/ELB/S3 access logs on all VPCs on all accounts
- Set up Systems Manager Parameter Store & Secrets Manager with rotation windows
- No public buckets - use bucket policies, not IAM
- Check insecure API GW endpoints
- Check public EC2 / RDS access
- Encrypt & TLS
- Use Inspector for EC2/ECR scans, CodeWhisperer, CodeGuru & Lambda Extensions with Sync-SQ/Github actions
- Use WAF with API GW & AppSync & ELB. Use AWS Firewall Manager for multi-account
- Use Proton & ServiceCatalog for pre-defined provisioning
- AWS Backup - backup DBs, S3
- Enable AWS Health to see multi-account service status
- Add Route53 healthchecks
- Enable monitoring & access logging for API GW
- Enable DevOps Guru Serverless for Lambda concurrency & DynamoDB throttling (along with CW Contributor Insights)
- Enable ResillienceHub to meet RTO-RPO requirements
- Create a custom KMS key for encryption - use for S3, RDS, EBS backups etc. Set key rotations
- Lambda env vars, Dynamo, S3 - secure with own KMS keys

CW:
  - Setup custom dashboards & myApplications on home page & mobile app
  - Set up lifecycle rules & CW IA to optimize costs
  - Use synthetic canaries & RUM
  - Set alerts for HTTP 500, 429 etc errors on API GW, CloudFront etc
  - CW Metrics -> Set recommended alarms (CW alarms can trigger Lambda) 
  - CW Metrics - > Set up business metrics
  - Create CW alarms for any CW metric needed i.e. SQS ApproxNoOfMessages
  - CW -> Setup ApplicationSignals with SLOs (p99, p95 etc) 
  - Use CW patterns & anomaly detection for logs & lambda trigger/SysMgr for alarms
  - Utilize metric filters from CW logs to get alerts from the logs
  - Stream metrics to managed Prometheus & display on Grafana
  - Setup CW Subscription Filters -> Kinesis->S3/ES/Lambda & CloudTrail Lake or Organization access
  - Enable & use ContainerInsights to track ECS/Fargate utilization
  - Enable X-Ray on Lambda & Application-Lambda-Container Insights

RDS
- Use custom RDS reader/writer endpoints
- Launch DB clusters in separate, dedicated VPCs
- Use RDS Proxy with IAM authentication (Aurora MySQL, PostreSQL)
- Aurora Serverless v2(scales to 0), Aurora Global Database
- Aurora Data API (SQL over HTTP)

Costs:
- Set up budgets, check new savings advisor & saving plans. Set up billing alarms & cost anomaly detection
- Set up Compute Optimizer - analyses EC2, EBS, Lambda & generates recommendations
- Use reserved / spot instances & fleets as necessary
- Set up Costs Usage Report with Athena & Glue
- API GW cache costs based on total size * hour, not utilization
- Use ELB/functionURL instead of API GW if possible for lambda for high TPS, much cheaper
  (1MB request limit -> 413 Request Entity Too Large)
- Check unused RDS - use provisioned instead of on-demand
- Check unused EC2, block storage, backups
- Check S3 storage lens, utilize lifecycle rules & glacier, content serving out of S3
- Check use of public IPs & unused elastic IPs
- Check unused ELBs & multi-az communication (free for ALB, costs for NLB)
- Check network out data
- Check cloudFront origin retrieval
- Use graviton based Lambda & ECS-Fargate
- Use spot instances with EC2(EC2 & ECS agent, can SSH) & Fargate(no GPU instances, containerD)

<br/>

# re-Invent'24 - Simplexity:
https://www.youtube.com/watch?v=aim5x73crbM
https://aws.amazon.com/blogs/aws/top-announcements-of-aws-reinvent-2024/
https://theburningmonk.com/2024/11/best-preinvent-2024-serverless-announcements
https://www.youtube.com/watch?v=5wokwEtddtc


# What's new (since the start of re-Invent'24)
Serverless:
- DynamoDB: Price cut on-demand %50 global tables %67, warm throughput for tables & indexes(4k WPS & 12k RPS initially), 
            Global Tables Strong Consistency(DSQL), Attribute based access control(RBAC - based on table/user/policy tags)
            zero-ETL integration to OpenSearch & RedShift, PITR now configurable between 1 and 35 days, DynamoDB local available in CloudShell
- API GW: Custom domain names for private endpoints
- Lambda: Python 3.13 & Node 22, snapstart Python & .Net(not free), S3 as failure destination(async/streaming),
          VSCode-like editor(up to 50MB editable), SAM export, ApplicationSignals/SLAs & FaultInjectionService support, 
          Top-10 Lambda Metrics in Lambda Dashboard, new metrics for EventSourceMappings
- EventBridge: Avg latency down to 130ms from 2.2s, VPC Lattice+PrivateLink VPC access, API dest. proactive OAuth token refresh,
               event source discovery(console)
- SFs: Export as SAM/InfrastructureComposer from console, Variables & JSONata support, VPC Lattice+PrivateLink VPC access
- Kinesis: on-Demand now supports 5x throughtput - 10GB/s for writers 20GB/s for consumers per stream, tagging,
           attribute based access control
- Cognito: New landing page/managed login, pricing tiers (Lite/Essentials/Plus), passkey auth, refresh key rotation, 
           OIDC prompt parameter support
- S3: Conditional writes(if-none-match/if-match bucket policy), ExpressOneZone append data, DirectoryBuckets, 1M buckets, TransferFamily web apps, 
      AWS Backup S3 cross-region bucket replication, GeneralPurpose/Directory buckets, Table buckets for ApacheIceberg Metadata(S3 tables)
- Amplify: Amplify AI kit, StorageBrowser for S3, WAF Support(IP filtering, geo-restriction etc)
- AppSync: EventsAPI(EventBridge->Appsync Async+WebSockets), cross-account API access with RAM
- CodeBuild: Test splitting/parallelizm, remote Docker server support, 
- CodePipeline: DeploySpec file in EC2 deploy action, lambda linear/canary deployments,  
      
AI:
- Bedrock: Nova FMs, Marketplace, ConversationalBuilder, PromptMagr/Caching/Optimizer/Router, Flows, BatchInference(50% cheaper), 
           custom models, ConverseAPI, Rerank API, DataAutomation, cross-region inference, Guardrails up to 85% discount, IntelligentPromptRouting, 
           multi-model & multi-agent collaboration, autogenereated query filters, model & RAG evaluation - human & LLM-as-judge, distillation,
           custom intervention using agents, latency-optimized inference for FMs, automatic reasoning checks & multimodal toxicity detection
           for image content, JPEG/PNG 3.75MB limit
           Knowledge Bases - chat with document, Structred Data Retrieval(Redshift & SageMakerLakehouse), Aurora(Postgre) as vector store,
           web crawler/custom data sources(Salesforce, Confluence, Sharepoint..) & realtime data sync, Kendra GenAI Indexes, GraphRAG(Neptune) 
- Other AI: AppStudio, Sagamaker Unified Studio, Sagemaker realtime endpoints scale down to 0 & multi-adapter inference,
            Q developer: code review, inline chat, console/Datadog integration, Q Business new goodies

Others:
- CloudFormation: Lambda/Guard/ChangeSet/CloudControlAPI(Terraform) hooks, timeline view, github sync, user notifications,
                  IaC generator selective resource scanning, stack refactoring
- CloudFront: SaaS manager, ALB support with WAF(preconfig ACLs & SG), VPC origins(egress EC2 in private subnet w/out a public IP/ALB), 
              new access log formats & destinations, gRPC support, Anycast static IPs, origin/header modification using functions
- CloudWatch: Search all log groups(LogInsights), live logs in VS Code, tiered pricing, lambda->kinesis direct logs,
              network monitor multi-account flow monitors
- Compute: I8g(IO optimized), I7ie(storage optimized), U7ie(6&8TiB high-memory), P5en, F2(FPGA), TR2 Instances & UltraServers, 
           EBS time-based snapshot copy(15m-48h), instant start Capacity Blocks, future reservations, provisioned rate for volume init,
           EFS cross-account replication & up to 2.5 million IOPS per file system(x10),
           EC2 Optimized CPU config during autoscaling for licensing, zonal shift for autoscaling,  EC2 bandwith config for EBS & VPC,
           S3 auto mountpoints at EC2 startup
- Network: VPC block public access, PrivateLink private subnets(VPC endpoints & RAM) and cross-region support,
           SecurityGroup sharing(same account & region), ALB Header Modification, Route53 DNS Resolver Firewall Advanced
- RDS: Aurora DSQL - Postgre16, no FKs/triggers/extensions/vectors, single-region %99.99% multi-region 99.999% availability, 
       Aurora Serverless V2 scales down to 0% (needs to be <0.5CUs, scale-up ~15sec), Aurora as vector store, 
       CW DatabaseInsights for Aurora, MemoryDB multi-region with 99.999% availability & Valkey, zero-ETL integration to RedShift
       RDS live volume shrink using Blue/Green Deployments
- SystemManager: Manage EC2 and hybrid nodes across ALL accounts and regions in your AWS Organization
                 Superhero mode: Instantly spot unmanaged EC2 instances, JIT node access
                 Auto-fix: SysMgr now diagnoses and remedies issues to bring nodes to managed state
- ECS/EKS: ECS deployment history, 1-click rollback, predictive scaling, enhanced ContainerInsights, Fargate network fault injection,
           EKS AutoMode & Hybrid Nodes, node health monitoring & auto-repair, ESK Dashboard
- Other: Organizations/RootUser mgmt, ResourceControlPolicies(RCP), EC2 DeclarativePolicies(VPC block public access),
         MSK Express, Amazon Keyspaces(Cassandra) reduced prices up to 75%, 
         OpenSearch Serverless BinaryVector & PIT Search, ingestion Lambda support for transformation,
         CloudMap SLAs, TimeSyncService, DataTransferTerminals, CleanRooms multi-cloud, Inspector maps ECR images to running containers in ECS/EKS, 
         BillingConductor/InvoiceConfiguration/CostCategories/CustomBillingViews, Elasticache ServiceQuotas & global datastore,
         Console Multi-Session Support, DMS serverless support for files with an S3 source endpoint, Transform, Simulearn
         