# variables.tf
variable "project_id" {
  description = "Google Cloud Project ID"
  type        = string
}

variable "region" {
  description = "Google Cloud region"
  type        = string
  default     = "us-central1"
}

variable "storage_bucket_name" {
  description = "Name of the Cloud Storage bucket to store function code"
  type        = string
}

variable "pubsub_topic_name" {
  description = "Name of the Pub/Sub topic"
  type        = string
}

variable "function_name" {
  description = "Name of the Cloud Function"
  type        = string
}

# main.tf
terraform {
  required_providers {
    google = {
      source  = "hashicorp/google"
      version = "~> 5.0"
    }
    archive = {
      source  = "hashicorp/archive"
      version = "~> 2.0"
    }
  }
}

provider "google" {
  project = var.project_id
  region  = var.region
}

# Create Cloud Storage bucket for function code
resource "google_storage_bucket" "function_bucket" {
  name     = var.storage_bucket_name
  location = var.region
  uniform_bucket_level_access = true
  
  versioning {
    enabled = true
  }
}

# Create Pub/Sub topic
resource "google_pubsub_topic" "function_topic" {
  name = var.pubsub_topic_name
}

# Create ZIP file containing function code
data "archive_file" "function_zip" {
  type        = "zip"
  output_path = "${path.module}/function.zip"
  source {
    content = <<EOF
import functions_framework
import base64
import json

@functions_framework.cloud_event
def process_pubsub_message(cloud_event):
    # Get Pub/Sub message from the CloudEvent
    if cloud_event.data:
        pubsub_message = base64.b64decode(cloud_event.data["message"]["data"]).decode()
        print(f"Received message: {pubsub_message}")
        
        try:
            # Parse JSON message
            message_json = json.loads(pubsub_message)
            print(f"Processed JSON: {message_json}")
        except json.JSONDecodeError:
            print("Message is not JSON format")
            
    return "OK"
EOF
    filename = "main.py"
  }
  source {
    content = <<EOF
functions-framework==3.*
EOF
    filename = "requirements.txt"
  }
}

# Upload function code to Cloud Storage
resource "google_storage_bucket_object" "function_code" {
  name   = "function-${data.archive_file.function_zip.output_md5}.zip"
  bucket = google_storage_bucket.function_bucket.name
  source = data.archive_file.function_zip.output_path
}

# Create service account for the function
resource "google_service_account" "function_account" {
  account_id   = "${var.function_name}-sa"
  display_name = "Service Account for ${var.function_name}"
}

# IAM binding for Pub/Sub to invoke the function
resource "google_project_iam_member" "pubsub_publisher" {
  project = var.project_id
  role    = "roles/run.invoker"
  member  = "serviceAccount:${google_service_account.function_account.email}"
}

# Cloud Function
resource "google_cloudfunctions2_function" "function" {
  name = var.function_name
  location = var.region

  build_config {
    runtime     = "python313"
    entry_point = "process_pubsub_message"
    source {
      storage_source {
        bucket = google_storage_bucket.function_bucket.name
        object = google_storage_bucket_object.function_code.name
      }
    }
  }

  service_config {
    max_instance_count = 1
    available_memory   = "256M"
    timeout_seconds    = 60
    service_account_email = google_service_account.function_account.email
  }

  event_trigger {
    trigger_region = var.region
    event_type    = "google.cloud.pubsub.topic.v1.messagePublished"
    pubsub_topic  = google_pubsub_topic.function_topic.id
    retry_policy  = "RETRY_POLICY_RETRY"
  }
}

# outputs.tf
output "bucket_name" {
  description = "Name of the Cloud Storage bucket storing the function code"
  value       = google_storage_bucket.function_bucket.name
}

output "function_uri" {
  description = "URI of the Cloud Function"
  value       = google_cloudfunctions2_function.function.service_config[0].uri
}

output "pubsub_topic" {
  description = "Name of the Pub/Sub topic"
  value       = google_pubsub_topic.function_topic.name
}