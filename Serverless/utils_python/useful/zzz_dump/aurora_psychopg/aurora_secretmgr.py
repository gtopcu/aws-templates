import os
import boto3
import json

from sqlalchemy import create_engine
from sqlalchemy.sql import text

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
        #"reader_endpoint": "secr-db.cluster-ro-c7brgyzxb8l0.eu-west-2.rds.amazonaws.com",
        #"port": 5432,
        "reader_endpoint": "127.0.0.1",
        "port": 3307,
        "database_name": "secr_data",
        "master_user_secret_arn": "arn:aws:secretsmanager:eu-west-2:092241524551:secret:rds!cluster-56371737-ad2b-405e-ab00-ef1f31d885ac-aGssFX",
    }

    # Test getting credentials
    # print(get_credentials_from_secret("arn:aws:secretsmanager:eu-west-2:092241524551:secret:rds!cluster-56371737-ad2b-405e-ab00-ef1f31d885ac-aGssFX"))

    # Set environment variables from cluster info
    # set_env_variables_from_cluster_info(cluster_info)

    # Test the database connection
    # test_db_connection()

    
    # Enable SSH Tunnel (add your PC's public key to bastion host's .ssh/authorized_hosts file first):
    # ssh -N -L 3307:secr-db.cluster-c7brgyzxb8l0.eu-west-2.rds.amazonaws.com:5432 ec2-user@ec2-18-169-210-161.eu-west-2.compute.amazonaws.com

    # Create SQLAlchemy engine
    engine = create_engine(
        f"postgresql+psycopg://postgres:PW@localhost:3307/secr_data"#,
        #connect_args={"options": creds.options},
    )
    try:
        with engine.connect() as connection:
            result = connection.execute(
                text("SELECT * from secr_data.processed_data_item LIMIT 1")
            )
            print(result.fetchone())
            print("Database connection test successful!")
    except Exception as e:
        print(f"Database connection test failed: {e}")
        raise
