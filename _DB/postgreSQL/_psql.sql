

/* 
https://neon.tech/postgresql/postgresql-getting-started/connect-to-postgresql-database

Install on Ubuntu/Debian/Redhat/CentOS:
https://neon.tech/postgresql/postgresql-getting-started/install-postgresql-linux

neonDB timescale crudRestAPI
*/

/* official image. sets the DB password: */
docker run --name postgres17 -e POSTGRES_PASSWORD=postgres -dp 5432:5432 postgres:17 
docker run --name local-db --env-file ./.env -dp 5432:5432 postgres:latest

pg_ctl start stop
brew services start stop postgresql
sudo systemctl start stop enable disable postgresql
sudo service postgresql start stop enable disable

chmod +x myscript.sh
#!/bin/bash
sh myscript.sh

psql -U postgres
pg_ctl 
pg_restore 
pg-cron pg-vector pg-ai
psychopg2 
transaction logs 
unlogged tables

version() now() current_database() inet_server_addr() inet_server_port();

id INT PRIMARY KEY GENERATED ALWAYS AS IDENTITY
SERIAL PRIMARY KEY AUTOINCREMENT
UNIQUE DEFAULT NOT NULL 

BOOLEAN|BOOL CHAR(20) VARCHAR(20) TEXT TEXT[] 
SMALLINT INT INT4 BIGINT 
FLOAT(2) NUMERIC(10,2) DECIMAL(10, 2) REAL FLOAT8|DOUBLEPRECISION
DATE TIME(2) TIMESTAMP TIMESTAMPTZ INTERVAL
DATE DEFAULT CURRENT_DATE,
TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP,
UUID JSON JSONB XML ENUM BYTEA(1GBmax) hstore(key/value str only) Array(int/str etc) 
UserDefined/Composite types

COUNT DISTINCT ORDER BY 
AND OR LIMIT OFFSET FETCH IN BETWEEN LIKE IS NULL  
INNER JOIN LEFT JOIN RIGHT JOIN SELF JOIN FULL OUTER JOIN
GROUP BY HAVING RETURNING GROUPING SETS CUBE ROLLUP
UNION INTERSECT EXCEPT 
UPSERT MERGE  
ANY ALL EXISTS
AVG, MIN, MAX, FLOOR, CEIL, ROUND
SUM (CASE WHEN rental_rate = 0.99 THEN 1 ELSE 0 END) AS "Economy",
COALESCE (NULL, 2 , 1)  /* returns first non-null argument */
CAST ('100' AS INTEGER) CAST ('01-OCT-2015' AS DATE)
NULLIF (1, 1); -- return NULL /*  returns NULL if argument_1 == argument_2, otherwise argument_1 */

-----------------------------------------------------------------------------------------------------

pgAdmin

psql -U postgres <-h localhost> -> Will ask for password
psql --dbname $DB_NAME --host $ENDPOINT --username $DB_USER --set sslmode=require -c "SELECT * FROM myschema.mytable" 

sudo -u postgres psql

-- \l                    -> List all databases
-- \c otherdatabase      -> Switch database
-- \dt                   -> List all tables under the current database
-- \dt schema.*          -> List objects with any name under schema
-- \d my_table           -> Show structure of my_table
-- \q | exit             -> Exit
-- \include ~/script.sql -> Execute the given SQL file

-----------------------------------------------------------------------------------------------------

SELECT version();
SELECT current_database();
SELECT inet_server_addr(), inet_server_port();
SELECT now();

gen_random_uuid()
date_trunc('hour', created_at) AS hour
LOWER() HIGHER() SUM()
NOW() - INTERVAL '30 days'

timing on

SHOW TIMEZONE;
SET timezone = 'America/Los_Angeles';

CREATE DATABASE my_database;
CREATE SCHEMA my_schema;

CREATE ROLE my_role WITH LOGIN;
GRANT USAGE ON my_schema TO my_role;
GRANT SELECT, INSERT, UPDATE, DELETE ON ALL TABLES IN DATABASE my_database TO my_role;
GRANT SELECT, INSERT, UPDATE, DELETE ON ALL TABLES IN SCHEMA my_schema TO my_role;
DELETE ROLE my_role;

CREATE USER my_user WITH PASSWORD '<password>' IN ROLE my_role
ALTER USER postgres PASSWORD '<password>';
DELETE USER postgres;

-----------------------------------------------------------------------------------------------------

https://neon.tech/postgresql/postgresql-getting-started/load-postgresql-sample-database
pg_restore -U postgres -d mydatabase D:\sampledb\postgres\data.tar

AlloyDB
SET google_columnar_engine.enable_columnar_scan=off;
SHOW google_columnar_engine.enable_columnar_scan;

-----------------------------------------------------------------------------------------------------

