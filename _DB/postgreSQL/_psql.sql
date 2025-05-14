

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
(SERIAL PRIMARY KEY AUTOINCREMENT)
UNIQUE DEFAULT NOT NULL 
BOOLEAN CHAR(20) VARCHAR(20) TEXT TEXT[] 
SMALLINT INT INT4 BIGINT 
FLOAT(2)  NUMERIC(10,2) REAL FLOAT8 | DOUBLEPRECISION
DATE TIME(2) TIMESTAMP TIMESTAMPTZ Interval
UUID JSON JSONB XML ENUM BYTEA(1GBmax) hstore Array(int/str etc) 
UserDefined/Composite types
LIMIT FETCH OFFSET AND OR BETWEEN IN LIKE ISNULL  
UPSERT MERGE COUNT GROUPBY ORDERBY HAVING UNION INTERSECT
CASE COALESCE NULLIF CAST ANY ALL EXISTS

-----------------------------------------------------------------------------------------------------

pgAdmin

psql -U postgres <-h localhost> -> Will ask for password
psql --dbname $DB_NAME --host $ENDPOINT --username $DB_USER --set sslmode=require -c "SELECT * FROM myschema.mytable" 

sudo -u postgres psql

\l                    -> List all databases
\c otherdatabase      -> Switch database
\dt                   -> List all tables under the current database
\dt schema.*          -> List objects with any name under schema
\q | exit             -> Exit
\include ~/script.sql -> Execute the given SQL file

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
CREATE USER my_user WITH PASSWORD '<password>' IN ROLE my_role
ALTER USER postgres PASSWORD '<password>';

CREATE ROLE my_role WITH LOGIN;
GRANT USAGE ON my_schema TO my_role;
GRANT SELECT, INSERT, UPDATE ON ALL TABLES IN SCHEMA my_schema TO my_role;

-----------------------------------------------------------------------------------------------------

https://neon.tech/postgresql/postgresql-getting-started/load-postgresql-sample-database
pg_restore -U postgres -d mydatabase D:\sampledb\postgres\data.tar


AlloyDB
SET google_columnar_engine.enable_columnar_scan=off;
SHOW google_columnar_engine.enable_columnar_scan;

-----------------------------------------------------------------------------------------------------

