
/*
https://www.sqlekibi.com/2025/05/26/postgresql-performans-iyilestirme-rehberi-autovacuum-indexler-ve-paralel-sorgular/

Case-insensitive search: ILIKE or citext

B-TREE: Check if equal / sorting
HASH: Check if equal
GIN: Full-text search & JSONB
BRIN: For sparse data in large tables
SP-GIST
GIST

CREATE UNLOGGED TABLE fast_table 
EXPLAIN (SELECT * FROM customers)

SELECT * FROM information_schema.tables;
SELECT * FROM pg_catalog.pg_settings
SELECT * FROM pg_catalog.pg_extension
SELECT * FROM pg_catalog.pg_user
SELECT * FROM pg_catalog.pg_group
SELECT * FROM pg_catalog.pg_policies
SELECT * FROM pg_catalog.pg_roles
SELECT * FROM pg_catalog.pg_trigger
SELECT * FROM pg_catalog.pg_views
SELECT * FROM pg_catalog.pg_matviews
SELECT * FROM pg_catalog.pg_database
SELECT * FROM pg_catalog.pg_namespace
SELECT * FROM pg_catalog.pg_foreign_table
SELECT * FROM pg_catalog.pg_tablespace
SELECT * FROM pg_catalog.pg_tables WHERE tablename = 'my_table';
SELECT * FROM pg_catalog.pg_indexes WHERE tablename = 'my_table';


SELECT table_schema, table_name 
FROM information_schema.tables 
WHERE table_schema NOT IN ('information_schema', 'pg_catalog')
# WHERE table_schema = 'public'
AND table_type = 'BASE TABLE'
ORDER BY table_schema, table_name;

SELECT datname AS database_name
FROM pg_database
WHERE datistemplate = false
ORDER BY datname;

SELECT 
    datname AS database_name,
    pg_catalog.pg_get_userbyid(datdba) AS owner,
    pg_encoding_to_char(encoding) AS encoding,
    datcollate AS collate,
    datctype AS ctype
FROM pg_database
WHERE datistemplate = false
ORDER BY datname;


-------------------------------------------------------------------------
SELECT * FROM pg_settings
-------------------------------------------------------------------------
max_connections = 1669
max_parallel_workers = 8
max_parallel_workers_per_gather = 2
max_worker_processes = 8
shared_buffers = 4GB
autovacuum = on
autovacuum_vacuum_scale_factor = 0.2
autovacuum_analyze_scale_factor = 0.1
autovacuum_vacuum_threshold = 50
autovacuum_analyze_threshold = 50
autovacuum_max_workers = 3
autovacuum_naptime = 1min
autovacuum_vacuum_cost_delay = 20ms
autovacuum_vacuum_cost_limit = 200
log_min_duration_statement = 500ms


*/

id INT PRIMARY KEY GENERATED ALWAYS AS IDENTITY
SERIAL PRIMARY KEY AUTOINCREMENT
UNIQUE DEFAULT NOT NULL 

BOOLEAN|BOOL CHAR(20) VARCHAR(20) TEXT TEXT[] 
SMALLINT INT INT4 BIGINT 
FLOAT(2) NUMERIC(10,2) DECIMAL(10, 2) REAL FLOAT8|DOUBLEPRECISION
DATE TIME(2) TIMESTAMP TIMESTAMPTZ INTERVAL
DATE DEFAULT CURRENT_DATE,
TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP,
UUID JSON JSONB(enables query) 
XML ENUM BYTEA(1GBmax) 
hstore(key/value str only) 
Array(int/str etc) 
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
TO_CHAR CAST ('100' AS INTEGER) CAST ('01-OCT-2015' AS DATE)
NULLIF (1, 1); -- return NULL /*  returns NULL if argument_1 == argument_2, otherwise argument_1 */


/* ------------------------------------------------------------------------------------------------ */

SELECT typname, typlen 
FROM pg_type 
WHERE typname ~ '^timestamp';

/* ------------------------------------------------------------------------------------------------ */

CREATE EXTENSION IF NOT EXISTS vector;
ALTER TABLE my_vectordb
ADD COLUMN embedding vector(1024);

/* ------------------------------------------------------------------------------------------------ */

CREATE OR REPLACE FUNCTION update_updated_at()
RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at = current_timestamp;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER department_updated_at_trigger
BEFORE UPDATE ON department
FOR EACH ROW
EXECUTE FUNCTION update_updated_at();

/* ------------------------------------------------------------------------------------------------ */

CREATE VIEW book_info
AS SELECT
    book_id,
    title,
    isbn,
    published_date,
    name
FROM
    books b
INNER JOIN publishers
    USING(publisher_id)
ORDER BY title;

/* ------------------------------------------------------------------------------------------------ */


SELECT date_trunc('hour', created_at) AS hour, COUNT(*) AS total_users
FROM users
GROUP BY hour
ORDER BY hour;

SELECT
    time_bucket('1 day', event_time) AS bucket,
    count(*) AS star_count
FROM events
WHERE
    NOW() - INTERVAL '30 days' <= event_time
    AND LOWER(repo_name) = 'timescale/timescaledb'
GROUP BY bucket
ORDER BY bucket DESC;


SELECT 
  (
    SUM (CASE WHEN gender = 1 THEN 1 ELSE 0 END) / NULLIF (
      SUM (CASE WHEN gender = 2 THEN 1 ELSE 0 END), 
      0
    )
  ) * 100 AS "Male/Female ratio" 
FROM 
  members;
