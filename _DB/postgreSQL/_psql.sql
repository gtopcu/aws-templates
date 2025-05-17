

/* 
https://neon.tech/postgresql/postgresql-getting-started/connect-to-postgresql-database

Install on Ubuntu/Debian/Redhat/CentOS:
https://neon.tech/postgresql/postgresql-getting-started/install-postgresql-linux

No FKs/triggers/extensions/vectors, single-region %99.99% multi-region 99.999% availability, 

neonDB timescale crudRestAPI
*/

/* official image. sets the DB password: */
docker run --name postgres17 -e POSTGRES_PASSWORD=postgres -dp 5432:5432 postgres:17
docker run --name local-db --env-file ./.env -dp 5432:5432 postgres:latest

sudo systemctl start stop enable disable postgresql
sudo service postgresql start stop enable disable
pg_ctl start stop
brew services start stop postgresql

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
SELECT gen_random_uuid()
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
DROP ROLE my_role;
pg_database_owner
pg_maintain
pg_monitor
pg_read_all_data | pg_write_all_data
pg

CREATE USER my_user WITH PASSWORD '<password>' IN ROLE my_role
ALTER USER postgres PASSWORD '<password>';

-----------------------------------------------------------------------------------------------------

https://neon.tech/postgresql/postgresql-getting-started/load-postgresql-sample-database
pg_restore -U postgres -d mydatabase D:\sampledb\postgres\data.tar

AlloyDB
SET google_columnar_engine.enable_columnar_scan=off;
SHOW google_columnar_engine.enable_columnar_scan;

-----------------------------------------------------------------------------------------------------

