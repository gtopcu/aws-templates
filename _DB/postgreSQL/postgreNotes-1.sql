# [pytest]
# pythonpath = "D:\VSCode2\infra\lambdas\resolvers\supplier_data_request"
# pytest test_class.py::test_method
# addopts = -p no:warnings
# pythonpath = "./lambda-layers/secr-py-core-domain/python"

# PYTHONPATH=./infra/lambda-layers/secr-py-core-domain/python/secr
# PYTHONPATH=D:\VSCode2\infra\lambda-layers\secr-py-core-domain\python\secr
# set PYTHONPATH=%PYTHONPATH%;D:\VSCode2\infra\lambda-layers\secr-py-core-domain\python\secr
# import os; print(os.getenv("PYTHONPATH"));
# $env:PATH
# $env:PYTHONPATH

# ruff format .
# ruff check . --fix
# ruff check test.py --config ruff.toml
# ruff check test.py --fix

# docker info
# PreferencesUI -> workbench.editor.enablePreview  

# .gitignore
# secr

# Seach ignore
# secr/*, schema.graphql, schema copy.graphql, loading_scripts/*, loading-scripts/*, tests/*, test/*, test*,  local_tests/, *.csv

# git pull | docker
# git branch -a 
# git checkout -b new-branch
# git branch -m old-name new-name

# Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
# .\.venv\Scripts\Activate.ps1
# D:\VSCode2\infra\.venv\Scripts\Activate.ps1
# pip -V
# deactivate

# Remove-Item -Path "D:\VSCode2\infra\.venv\Lib\site-packages" -Recurse -Force

# Copy-Item -Path "D:\VSCode2\infra\lambda-layers\secr-py-core-domain\python\secr" -Destination "D:\VSCode2\infra\.venv\Lib\site-packages" -Recurse -Force
# Copy-Item -Path "D:\VSCode2\infra\lambdas" -Destination "D:\VSCode2\infra\.venv\Lib\site-packages" -Recurse -Force

# Remove-Item -Path "D:\VSCode2\infra\.venv\Lib\site-packages\secr" -Recurse -Force
# Remove-Item -Path "D:\VSCode2\infra\.venv\Lib\site-packages\lambdas" -Recurse -Force

# import os; 
# print(os.getenv("PYTHONPATH"));
# sys.path.append(os.getenv("PYTHONPATH"));

# import sys
# sys.path.append("infra/secr-py-core-domain/python/secr")
# print(sys.path)

# os.environ["AWS_ACCESS_KEY_ID"]=""
# os.environ["AWS_SECRET_ACCESS_KEY"]=""
# os.environ["AWS_SESSION_TOKEN"]=""

#    Create a `.env` file with necessary environment variables:
#    ```
#    AWS_DEFAULT_REGION=eu-west-2

#    RDS_PASSWORD_ARN="arn:aws:secretsmanager:eu-west-2:092241524551:secret:rds!cluster-56371737-ad2b-405e-ab00-ef1f31d885ac-aGssFX"
#    RDS_HOST_URL="127.0.0.1"
#    RDS_PORT=3307
#    RDS_DBNAME="secr_data"
#    ENV_DATA_TABLE = "CUSTOMER_DATA_SOURCE_TABLE"

#    COMPANY_DATA_TABLE="COMPANY_DATA"
#    DATA_BUCKET_NAME="dev-secr-customer-data-bucket"
#    DS_AGGREGATION_DATA_TABLE="DS_AGGREGATION_TABLE"
#    SEND_NOTIFICATION_SNS_ARN="arn:aws:sns:eu-west-2:092241524551:send_notification"
   
#    CUSTOMER_DATA_SOURCE_TABLE = "CUSTOMER_DATA_SRC_DATA"
#    DS_AGGREGATION_DATA_TABLE = "DS_AGGREGATION_TABLE"
#    QUESTIONNAIRES_TABLE = "QUESTIONNAIRES"


# ssh -N -L 3307:secr-db.cluster-c7brgyzxb8l0.eu-west-2.rds.amazonaws.com:5432 ec2-user@ec2-18-169-210-161.eu-west-2.compute.amazonaws.com
# aws secretsmanager get-secret-value --secret-id secr/rds/credentials --query SecretString --output text | jq -r '.password'
# Host: 127.0.0.1
# Port: 3307
# Username: postgres
# Password: Retrieve from AWS Secrets Manager
# Database: secr_data