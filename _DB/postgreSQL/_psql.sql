

https://www.youtube.com/watch?v=-oHHwuFDKwE

export DB_NAME = "postgres"
export ENDPOINT = localhost
export DB_USER = "admin"
export DB_PORT = 5432
export PGPASSWORD=$(aws dsql generate-db-connect-admin-auth-token --hostname $ENDPOINT --expires_in 14400)

psql --dbname $DB_NAME --host $ENDPOINT --username $DB_USER --set sslmode=require -c "SELECT * FROM myschema.mytable" 

\q                              -> quit psql
\dt schema.*                    -> list objects with any name under the schema myschema
\include ~/src/myscript.sql     -> execute the given SQL file



