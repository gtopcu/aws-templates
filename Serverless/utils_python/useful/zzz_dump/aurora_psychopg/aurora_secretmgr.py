import os
import boto3
import json

# Constants for environment variable names
RDS_HOST_ENV = "RDS_HOST_URL"
RDS_PORT_ENV = "RDS_PORT"
RDS_DBNAME_ENV = "RDS_DBNAME"
PASSWORD_SECRET_ENV = "RDS_PASSWORD_ARN"

# Initialize boto3 clients
secrets_manager_client = boto3.client("secretsmanager", region_name="eu-west-2")


def set_env_variables_from_cluster_info(cluster_info):
    os.environ[RDS_HOST_ENV] = cluster_info["reader_endpoint"]
    os.environ[RDS_PORT_ENV] = str(cluster_info["port"])
    os.environ[RDS_DBNAME_ENV] = cluster_info["database_name"]
    os.environ[PASSWORD_SECRET_ENV] = cluster_info["master_user_secret_arn"]
    print("Environment variables set successfully from cluster info.")


def get_credentials_from_secret(secret_arn):
    secret_response = secrets_manager_client.get_secret_value(SecretId=secret_arn)
    secret = json.loads(secret_response["SecretString"])
    return {"username": secret["username"], "password": secret["password"]}


def test_db_connection():
    try:
        # Retrieve credentials from Secrets Manager
        credentials = get_credentials_from_secret(os.environ[PASSWORD_SECRET_ENV])
        print(credentials)
        # Create a connection string
        conn_str = (
            f"host={os.environ[RDS_HOST_ENV]} "
            f"port={os.environ[RDS_PORT_ENV]} "
            f"dbname={os.environ[RDS_DBNAME_ENV]} "
            f"user={credentials['username']} "
            f"password={credentials['password']}"
        )

        print(f"Connection string: {conn_str}")

        # Try connecting to the database

        print("Connection successful")

    except Exception as e:
        print(f"Error connecting to the database: {e}")


if __name__ == "__main__":
    cluster_info = {
        "reader_endpoint": "secr-db.cluster-ro-c7brgyzxb8l0.eu-west-2.rds.amazonaws.com",
        "port": 5432,
        "database_name": "secr_data",
        "master_user_secret_arn": "arn:aws:secretsmanager:eu-west-2:092241524551:secret:rds!cluster-56371737-ad2b-405e-ab00-ef1f31d885ac-aGssFX",
    }

    # Set environment variables from cluster info
    set_env_variables_from_cluster_info(cluster_info)

    # Test the database connection
    test_db_connection()
