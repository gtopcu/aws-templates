

output "s3_bucket_name" {
  description = "Name of the S3 bucket storing the Lambda code"
  value       = aws_s3_bucket.lambda_bucket.id
}

output "lambda_function_arn" {
  description = "ARN of the Lambda function"
  value       = aws_lambda_function.processor.arn
}

output "sqs_queue_url" {
  description = "URL of the SQS queue"
  value       = aws_sqs_queue.trigger_queue.url
}