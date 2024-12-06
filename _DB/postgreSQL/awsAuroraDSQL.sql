

https://blog.datachef.co/aurora-dsql-a-new-boring-aws-serverless-postgres-compatible-database

---------------------------------------------------------------------------------------------------------

-- Create the role
CREATE ROLE example WITH LOGIN;

-- Create the DB role to IAM role mapping
AWS IAM GRANT example TO 'arn:aws:iam::111122223333:role/example';

-- Assign permissions to the role
GRANT USAGE ON myschema TO example;
GRANT SELECT, INSERT, UPDATE ON ALL TABLES IN SCHEMA myschema TO example;

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