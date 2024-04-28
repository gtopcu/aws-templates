
https://www.postgresqltutorial.com/postgresql-tutorial/postgresql-bytea-data-type/

RETURNING / HAVING 
ANY / ALL / EXISTS
UNION / INTERSECT / EXCEPT
TO_CHAR / CAST / CASE / COALESCE / NULLIF
JSON-JSONB / XML / BYTEA(1GB) 

SELECT typname, typlen 
FROM pg_type 
WHERE typname ~ '^timestamp';

SHOW TIMEZONE;
SET timezone = 'America/Los_Angeles';

CREATE TABLE mailing_list (
    first_name VARCHAR NOT NULL,
    last_name VARCHAR NOT NULL,
    CHECK (
        first_name !~ '\s'
        AND last_name !~ '\s'
    )
);

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