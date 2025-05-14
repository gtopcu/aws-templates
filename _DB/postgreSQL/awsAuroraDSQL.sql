

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

CREATE SCHEMA example;

CREATE TABLE example.invoice(id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
                             created TIMESTAMP, department_id INT, amount FLOAT);
CREATE INDEX invoice_created_idx on example.invoice(created);

INSERT INTO example.invoice(created, purchaser, amount)
VALUES (now(), 1, 100.0),
       (now(), 2, 200.0),
       (now(), 3, 300.0),
       (now(), 3, 100.0);

SELECT * FROM example.invoice;

---------------------------------------------------------------------------------------------------------

ALTER TABLE example.invoice
RENAME COLUMN purchaser TO department_id;

CREATE TABLE example.department(id INT PRIMARY KEY UNIQUE, name TEXT, email TEXT);
INSERT INTO example.department(id, name, email)
VALUES (1, 'Engineering', 'engineering@example.com'),
       (2, 'Sales', 'engineering@example.com'),
       (3, 'Marketing', 'marketing@example.com'),
       (4, 'HR', 'hr@@example.com');

---------------------------------------------------------------------------------------------------------

SELECT dep.name, sum(inv.amount) AS spent
FROM example.department AS dep
    LEFT JOIN example.invoice inv ON dep.id = inv.department_id
GROUP BY dep.name
HAVING sum(inv.amount) > 0
ORDER BY spent DESC;

---------------------------------------------------------------------------------------------------------

---------------------------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------------------------