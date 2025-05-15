

RETURNING / HAVING 
ANY / ALL / EXISTS
UNION / INTERSECT / EXCEPT
TO_CHAR / CAST / CASE / COALESCE / NULLIF
JSON-JSONB / XML / BYTEA(1GB) 

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
