

https://blog.datachef.co/aurora-dsql-a-new-boring-aws-serverless-postgres-compatible-database
https://www.youtube.com/watch?v=-oHHwuFDKwE

export DB_NAME = "postgres"
export DB_ENDPOINT = localhost
export DB_USER = "admin"
export DB_PORT = 5432
export PGPASSWORD=$(aws dsql generate-db-connect-admin-auth-token --hostname $DB_ENDPOINT --expires_in 14400)

psql --dbname $DB_NAME --host $ENDPOINT --username $DB_USER --set sslmode=require -c "SELECT * FROM myschema.mytable" 
psql =U postgres -h <hostname>

---------------------------------------------------------------------------------------------------------

-- Create the role
CREATE ROLE dsql_role WITH LOGIN;

-- Assign permissions to the role
GRANT USAGE ON myschema TO dsql_role;
GRANT SELECT, INSERT, UPDATE ON ALL TABLES IN SCHEMA myschema TO dsql_role;

-- Create the DB role to IAM role mapping
AWS IAM GRANT dsql_role TO 'arn:aws:iam::111122223333:role/dsql_role';

---------------------------------------------------------------------------------------------------------



