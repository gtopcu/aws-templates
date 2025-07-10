import boto3
import json
import sys
from typing import Optional, List, Dict, Set

# --- Configuration ---

CREDENTIALS_FILE = "credentials.json"

# --- DynamoDB Helper Functions ---

def get_dynamodb_client(access_key: str, secret_key: str, session_token: str, region_name: str) -> Optional[boto3.client]:
    try:
        client = boto3.client(
            "dynamodb",
            aws_access_key_id=access_key,
            aws_secret_access_key=secret_key,
            aws_session_token=session_token,
            region_name=region_name,
        )
        return client
    except Exception as e:
        print(f"Error creating DynamoDB client for region {region_name}: {e}")
        return None

def list_dynamodb_tables(client: Optional[boto3.client], env_name: str) -> List[str]:
    """
    List all DynamoDB tables in the given environment.
    """
    if not client:
        print(f"Error: No DynamoDB client available for {env_name} to list tables.")
        return []
    try:
        tables = []
        paginator = client.get_paginator("list_tables")
        response_iterator = paginator.paginate()
        for page in response_iterator:
            tables.extend(page.get("TableNames", []))
        print(f"Found {len(tables)} DynamoDB tables in {env_name}: {', '.join(tables)}")
        return tables
    except Exception as e:
        print(f"Error listing DynamoDB tables in {env_name}: {e}")
        return []

def scan_dynamodb_table_attribute_keys(client: Optional[boto3.client], table_name: str, env_name: str) -> Set[str]:
    """
    Scan a DynamoDB table to collect unique top-level attribute names (keys) from all items.
    """
    if not client:
        print(f"Error: No DynamoDB client available for {env_name} to scan table {table_name}.")
        return set()
    try:
        attribute_keys = set()
        paginator = client.get_paginator("scan")
        response_iterator = paginator.paginate(
            TableName=table_name,
            Select="ALL_ATTRIBUTES",
            ReturnConsumedCapacity="NONE",
            ConsistentRead=True,
        )
        print(f"Scanning DynamoDB table {table_name} in {env_name} for attribute keys...")
        total_items = 0
        for page in response_iterator:
            for item in page.get("Items", []):
                attribute_keys.update(item.keys())
                total_items += 1
        print(f"Scanned {total_items} items in DynamoDB table {table_name} in {env_name}. Found {len(attribute_keys)} unique attribute keys.")
        return attribute_keys
    except client.exceptions.ResourceNotFoundException:
        print(f"Error: DynamoDB table '{table_name}' not found during scan in {env_name}.")
        return set()
    except Exception as e:
        print(f"Error scanning DynamoDB table {table_name} in {env_name}: {e}")
        return set()

# --- Main Execution ---

def main():
    try:
        with open(CREDENTIALS_FILE) as f:
            creds = json.load(f)
    except FileNotFoundError:
        print(f"Error: Credentials file '{CREDENTIALS_FILE}' not found.")
        sys.exit(1)
    except json.JSONDecodeError:
        print(f"Error: Could not decode JSON from '{CREDENTIALS_FILE}'. Check file format.")
        sys.exit(1)
    except Exception as e:
        print(f"An unexpected error occurred while loading credentials: {e}")
        sys.exit(1)

    environments = ["DEV", "STAGING", "PROD"]
    env_creds = {}
    dynamodb_clients = {}

    print("--- Setting up DynamoDB Clients ---")
    for env in environments:
        if env not in creds:
            print(f"Error: Environment section '{env}' not found in credentials.json. Skipping setup for this environment.")
            env_creds[env] = None
            dynamodb_clients[env] = None
            continue

        env_creds[env] = creds[env]
        env_creds[env]['_env_name'] = env

        print(f"Setting up DynamoDB for {env}...")
        dynamodb_clients[env] = get_dynamodb_client(
            env_creds[env].get("access_key"),
            env_creds[env].get("secret_key"),
            env_creds[env].get("session_token"),
            env_creds[env].get("region")
        )

    print("\n--- Setup Complete ---")

    dev_dynamodb_client = dynamodb_clients.get("DEV")
    if not dev_dynamodb_client:
        print("\nCritical Error: Could not create DynamoDB client for DEV. Attribute key comparison aborted.")
        return

    # List all tables in DEV
    print(f"\nDiscovering all DynamoDB tables in DEV...")
    dev_tables = list_dynamodb_tables(dev_dynamodb_client, "DEV")
    if not dev_tables:
        print("No DynamoDB tables found in DEV. Exiting.")
        return

    # Collect attribute keys for DEV tables
    dev_table_attribute_keys = {}
    for table_name in dev_tables:
        attribute_keys = scan_dynamodb_table_attribute_keys(dev_dynamodb_client, table_name, "DEV")
        dev_table_attribute_keys[table_name] = attribute_keys

    # Compare attribute keys across STAGING and PROD
    print("\n--- Comparing Attribute Keys Across Environments ---")
    for table_name, dev_attribute_keys in dev_table_attribute_keys.items():
        print(f"\nTable: {table_name}")
        print(f"DEV: {len(dev_attribute_keys)} unique attribute keys found: {', '.join(sorted(dev_attribute_keys))}")

        for env in ["STAGING", "PROD"]:
            client = dynamodb_clients.get(env)
            if not client:
                print(f"  {env}: No DynamoDB client available. Skipping table and attribute key checks.")
                continue

            # Check if table exists and get attribute keys
            env_attribute_keys = scan_dynamodb_table_attribute_keys(client, table_name, env)
            if not env_attribute_keys and not client.exceptions.ResourceNotFoundException:
                print(f"  {env}: Table '{table_name}' does not exist.")
                continue
            else:
                print(f"  {env}: Table '{table_name}' exists with {len(env_attribute_keys)} unique attribute keys.")

            # Compare attribute keys
            missing_keys = dev_attribute_keys - env_attribute_keys
            new_keys = env_attribute_keys - dev_attribute_keys

            if missing_keys:
                print(f"  {env}: {len(missing_keys)} attribute keys missing (present in DEV but not in {env}):")
                for key in sorted(missing_keys):
                    print(f"    - {key}")
            else:
                print(f"  {env}: No attribute keys missing from DEV.")

            if new_keys:
                print(f"  {env}: {len(new_keys)} new attribute keys (present in {env} but not in DEV):")
                for key in sorted(new_keys):
                    print(f"    - {key}")
            else:
                print(f"  {env}: No new attribute keys not present in DEV.")

    print("\n--- Attribute Key Comparison Complete ---")

if __name__ == "__main__":
    main()
 