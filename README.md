# Serverless Notes

General:
- Enable CloudTrail management & data events(i.e.S3 put)
- Enable IAM AccessAdvisor & CloudTrail(90 days default) -> CW/S3 & Insights
- Utilize orgs, identitiy center, config, control tower, inspector, detective, guardduty, securityhub, codeguru, devopsguru
WAF, FirewallManager, ServiceQuotas, Health, Budgets, SavingPlans, ResourceExplorer
- Utilize metric filters & alerts

Lambda:
- 128MB-10GB memory, 256kb async/6MB sync payload, 15min timeout, /tmp 10GB ephemeral storage
- More memory = more vCPU + IO. 128MB-> 0.5vCPU, 256GB 1vCPU, 10GB 6vCPU, 1000 max concurrency limit per region
- 1 million requests & 400.000GB free. Pricing: number of requests & duration. Use Lambda Power Tuning SF to tune
- Invocations -> sync: API GW, Cognito, async: S3, EventBridge, SNS, polling: SQS, Kinesis/Dynamo Streams
- Lambda destinations -> success & fail for async, fail for polling
- Use reserved & provisioned concurrency as necessary. 3000 immediate, 500 burst concurrency per minute per region
- Use CW application insights & lambda insights (extension) for overall picture
- IAM PassRole -> Trust Policiy -> STS assumeRole

API GW:
- 10k req/s 30sec 10MB max, billed by request & cache size
- Regional, EdgeOptimized(CloudFront provides DDoS protection), Private(VPC endpoints)
- Log request_ids in your clients
- Direct service integration -> returns request_id for tracking
- API GW -> SQS -> SQS message_id -> can be tracked by client
- API Keys & usage plans, access logging, request validaton, throttling/caching, SDK generation, OIDC authentication, canary deployments per stage
- Set CW alarms using custom metrics & metric filters, utilize CW log insights & dashboards and X-Ray for tracing
- Use resource policies to restrict access to AWS accounts, IPs etc
- Documentation, API keys, testing, monitization -> apiable.com, AWS DataExchange
- Lambda Authorizer uses lambda concurrency, use auth caching - 5 min to 1 hour
- IAM auth useful for internal APIs, use WAF for public APIs

DynamoDB:
- 400kb max item size, 2KB for PK 1KB for SK, String, Number. Binary, Boolean, List, Map, Set
- on-Demand can scale x2 previous read/write peaks within 30 minutes. Provisioned can use auto-scaling
- DynamoDB global secondary indexes -> Key does not have to be unique
- Enable CW ContributorInsights for throttling & monitoring & hot PKs
- Use Global Tables, TTL expiration, streams, DeletionProtection, LeadingKeys IAM action on PKs for owner access
- Dynamo IA -> %60 cheaper on storage, %25 more expensive on reads & writes
- Consider Redis for sorted sets (i.e. realtime leaderboard), OpenSearch for TextSearch

SQS:
- 256KBs, 1-14 days storage, visibility timeout 30sec default - 12 hours max (set 6 x Lambda timeout)
- maxReceiveCount 1-1000, 10 messages max per batch
- Only use MaximumConcurrency setting on the queue with lambda, do not use ReservedConcurrency(leads to overpolling)
- Lambda timeout = batch size x avg message processing time
- SQS Batching works in 5 concurrent lambdas max, scales down in case of errors, scales up if more messages
(up to 1000 baches max, increases 60 parallel pollers per min)
- SQS FIFO can deduplicate by deduplication_id, order guaranteed within the same group_id
- SQS errors -> ApproximateAgeOfOldestMessage CloudWatch Metric + Alarm, queue redrive + event forking pipeline

SNS: 
- Can filter/retry to 3rd party HTTP. Fan-out to multiple SQS, FIFO can deliver to non-FIFO, can filter PII data
- SNS ->  Lambda retries 3 times for execution errors. Invocation errors: 6 hours default 
(not enough concurrency/throttling/large size/timeout etc). Performs 3 immediate tries, 2 at 1 second apart, 10 backing off from 
1 second to 20 seconds, and 100,000 at 20 seconds apart

EventBridge:
- 400ms latency avg, 24 hour retry, 1$ per 1 million events, free delivery to AWS services
- Use EventBridge scheduler & pipes as necessary

StepFunctions:
- StartExecution, WaitForCallback, retry/catch(States.ALL), retry jitter, no default timeout, wait(sleep), intrinsic functions
- Standard billed per no. of state transitions, express billed by duration. 256KB max payload limit
- Sync/Async execution, Map & DistributedMap for parallel data processing
- Choice states do not have catch/retry
- Use SFs if cannot guarantee idempotent lambdas

Kinesis:
- DataStreams PartitionKey & SequenceNumber(unique per partition), ordered, exactly once, replays, multiple consumers, errors 
block the shard until record duration
- DataStreams Write 1000 RPS & 1MB/sec, Read GetRecords 5t/sec 2MB per request (shared between consumers)
- Enhanced fan-out - more consumers, push instead of pull, each consumer gets 2MB, 50-70 milisecs latency, 5min timeout max, uses HTTP/2
- DataStreams - 1 day duraction default. Errors -> iterator age, bisect batch, max retry, max record age, on-failure destination
- ParallelizationFactor(default 1 - max 10) setting defines number of batches to process concurrently from each shard
- DataStreams aggregation to send/receive multiple records per record -> Kinesis Aggregation Library for Lambda
- Firehose -> S3, OpenSearch, buffers, transform/filter/enrich, no order guarantee, at least once, single target, does 3 retries
- Track Lambda IterationAge metric to see how far behing the processing is

S3:
- StorageLens, AccessPoints, S3 Select, Athena/Glue usefull stuff
- EventBridge can better filter & transform S3 events but more expensive (enable CloudTrail data events)

Cognito:
- OpenID providers, sync lambda triggers, AI powered fraud detection

Redis: 
- Great for real-time leaderboards