
/******************************************************************************* 
https://www.postgresqltutorial.com/postgresql-tutorial/postgresql-serial/
*/

SELECT version();
SELECT current_database();
SELECT inet_server_addr(), inet_server_port();
SELECT now();
SELECT gen_random_uuid()
date_trunc('hour', created_at) AS hour
LOWER() HIGHER() SUM()
NOW() - INTERVAL '30 days'

timing on

SMALLSERIAL	    2 bytes	    1 to 32,767
SERIAL	        4 bytes	    1 to 2,147,483,647
BIGSERIAL	    8 bytes	    1 to 9,223,372,036,854,775,807

CREATE TABLE table_name(
    id SERIAL
);

is equal to:

CREATE SEQUENCE table_name_id_seq;
CREATE TABLE table_name (
    id integer NOT NULL DEFAULT nextval('table_name_id_seq')
);
ALTER SEQUENCE table_name_id_seq
OWNED BY table_name.id;

CREATE TABLE weathers(
    id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY
)
CREATE TABLE order_items(
  order_id INT, 
  item_no SERIAL, 
  PRIMARY KEY (order_id, item_no)
);
ALTER TABLE products 
ADD PRIMARY KEY (product_id);

ALTER TABLE table_name 
DROP CONSTRAINT primary_key_constraint;

/******************************************************************************* 
https://www.postgresqltutorial.com/postgresql-tutorial/postgresql-date/
*/

SELECT NOW()         -> 2024-02-01 08:48:09.599933+07
SELECT NOW()::date   -> 2024-02-01
SELECT CURRENT_DATE  -> 2024-02-01

SELECT TO_CHAR(CURRENT_DATE, 'dd/mm/yyyy')      -> 01/02/2024
SELECT TO_CHAR(CURRENT_DATE, 'Mon dd, yyyy')    -> Feb 01, 2024

CREATE TABLE employees (
  employee_id SERIAL PRIMARY KEY, 
  first_name VARCHAR (255) NOT NULL, 
  last_name VARCHAR (255) NOT NULL, 
  birth_date DATE NOT NULL, 
  hire_date DATE NOT NULL
);
INSERT INTO employees (first_name, last_name, birth_date, hire_date)
VALUES ('Shannon','Freeman','1980-01-01','2005-01-01'),
       ('Sheila','Wells','1978-02-05','2003-01-01'),
       ('Ethel','Webb','1975-01-01','2001-01-01')
RETURNING *;

SELECT first_name, last_name, now() - hire_date as diff 
FROM employees;
diff -> 6970 days 08:51:20.824847

SELECT employee_id, first_name,last_name, AGE(birth_date) 
FROM employees;
age -> 45 years 11 mons 24 days
age('2015-01-01', birth_date)  -> age on given date

SELECT employee_id, first_name, last_name,
	EXTRACT (YEAR FROM birth_date) AS YEAR,
	EXTRACT (MONTH FROM birth_date) AS MONTH,
	EXTRACT (DAY FROM birth_date) AS DAY
FROM employees;


/******************************************************************************* 
https://www.postgresqltutorial.com/postgresql-tutorial/postgresql-timestamp/
https://www.postgresqltutorial.com/postgresql-tutorial/postgresql-time/

timestamp: a timestamp without a timezone one   - 8 bytes
timestamptz: timestamp with a timezone          - 8 bytes(converted & stored as UTC)
*/

SET timezone = 'America/Los_Angeles';

SELECT CURRENT_TIME         -> 21:02:13.648512-05  (= CURRENT_TIMESTAMP)
SELECT CURRENT_TIME(1)      -> 21:02:13.6
SELECT TIMEOFDAY()          -> Wed Jan 31 21:02:20.840159 2024 EST

SHOW TIMEZONE               -> America/New_York
SELECT timezone('America/Los_Angeles','2016-06-01 00:00')

SELECT LOCALTIME(0)                     -> 00:56:08
SELECT LOCALTIME AT TIME ZONE 'UTC-7'   -> 16:02:38.902271+07

SELECT
    LOCALTIME,
    EXTRACT (HOUR FROM LOCALTIME) as hour,
    EXTRACT (MINUTE FROM LOCALTIME) as minute, 
    EXTRACT (SECOND FROM LOCALTIME) as second,
    EXTRACT (milliseconds FROM LOCALTIME) as milliseconds; 


CREATE TABLE timestamp_demo (
    ts      TIMESTAMP   DEFAULT CURRENT_TIMESTAMP, 
    tstz    TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP
);
INSERT INTO timestamp_demo (ts, tstz)
VALUES('2016-06-22 19:10:25-07','2016-06-22 19:10:25-07')
RETURNING *;


column TIME(precision) - 8 bytes, precision 1 to 6, from 00:00:00 to 24:00:00
PostgreSQL accepts almost any reasonable TIME format including SQL-compatible & ISO 8601

HH:MI   
HH:MI:SS.pp
HHMISS

CREATE TABLE shifts (
    id serial PRIMARY KEY,
    shift_name VARCHAR NOT NULL,
    start_at TIME NOT NULL,
    end_at TIME NOT NULL
);  

INSERT INTO shifts(shift_name, start_at, end_at)
VALUES('Morning', '08:00:00', '18:00:00')

column TIME WITH TIME ZONE - 12 bytes
04:05:06 PST

SELECT time '10:00' - time '02:00' AS result
08:00:00

SELECT LOCALTIME + interval '2 hours' AS result;
03:16:18.020418


/******************************************************************************* 
https://www.postgresqltutorial.com/postgresql-tutorial/postgresql-interval/
*/

@ interval [ fields ] [ (p) ]   - 16 byte. @ optional, p: 0-6 fraction digits of seconds

INTERVAL '2 months ago';
INTERVAL '2 weeks ago';
INTERVAL '3 hours 20 minutes';
INTERVAL '1 year 2 months 3 days';

SELECT  now() - INTERVAL '1 year 3 hours 20 minutes' AS "3 hours 20 minutes ago of last year";


/******************************************************************************* 
https://www.postgresqltutorial.com/postgresql-tutorial/postgresql-uuid/ 
*/
SELECT gen_random_uuid();

CREATE TABLE contacts (
    contact_id uuid DEFAULT gen_random_uuid(),
)

/******************************************************************************* 
https://www.postgresqltutorial.com/postgresql-tutorial/postgresql-json/

JSON –  slower & larger, stores an exact copy of the JSON text, preserves ordering, allows duplicate keys, supports text-search
JSONB – faster, stores the JSON data in binary format

String: “Joe”
Number: 100, 9.99, …
Boolean: true | false
Null: null

{"title": "Chamber Italian", "release_year": 2006, "length": 117}
["Chamber Italian","Grosse Wonderful"," Airport Pollock"]
*/

CREATE TABLE products(
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    properties JSONB
);
INSERT INTO products(name, properties)
VALUES('Ink Fusion T-Shirt','{"color": "white", "size": ["S","M","L","XL"]}')
RETURNING *;

/* The -> operator extracts a JSON object field by a key. */
SELECT id, name, properties -> 'color' color FROM products;
"white"

/* The ->> operator extract a JSON object field by a key as text */
SELECT id, name, properties ->> 'color' color FROM products;
WHERE properties ->> 'color' IN ('black', 'white');
white


/* Storing JSON arrays */
CREATE TABLE contacts(
   id SERIAL PRIMARY KEY,
   name VARCHAR(255) NOT NULL,
   phones JSONB
);
INSERT INTO contacts(name, phones) 
VALUES
   ('John Doe','["408-111-2222", "408-111-2223"]'),
   ('Jane Doe','["212-111-2222", "212-111-2223"]')
RETURNING *;

/* The ->> 0 to extract the first elements in the phones array as text */
SELECT name, phones ->> 0 "work phone" 
FROM contacts;
   name   |  work phone
----------+--------------
 John Doe | 408-111-2222
 Jane Doe | 212-111-2222
 

/* ******************************************************************************* 
https://www.postgresqltutorial.com/postgresql-tutorial/postgresql-array/
*/

CREATE TABLE contacts (
  id SERIAL PRIMARY KEY, 
  name      VARCHAR (100), 
  phones    TEXT []
  /*two_dim   INT [][]*/
);
INSERT INTO contacts (name, phones)
VALUES('John Doe', ARRAY [ '(408)-589-5846','(408)-589-5555' ]);
/* or use curly braces: */
INSERT INTO contacts (name, phones)
VALUES('Lily Bush','{"(408)-589-5841"}'),
      ('William Gate','{"(408)-589-5842","(408)-589-58423"}');

SELECT name, phones [ 1 ] 
FROM contacts 
WHERE phones [ 2 ] = '(408)-589-58423';

UPDATE contacts
SET phones [2] = '(408)-589-5843'
WHERE ID = 3
RETURNING *;

SELECT name, phones 
FROM contacts 
WHERE '(408)-589-5555' = ANY (phones);

SELECT 
  name, 
  unnest(phones) 
FROM 
  contacts;

/* ******************************************************************************* 
https://www.postgresqltutorial.com/postgresql-tutorial/postgresql-enum/
*/

CREATE TYPE priority AS ENUM('low','medium','high');
SELECT enum_range(null::priority);
SELECT
  enum_first(NULL::priority) first_value,
  enum_last(NULL::priority)  last_value;

CREATE TABLE requests(
    id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    priority PRIORITY NOT NULL
)

ALTER TYPE enum_name 
ADD VALUE [IF NOT EXISTS] 'new_value'
[{BEFORE | AFTER } 'existing_enum_value';

ALTER TYPE priority
RENAME VALUE 'urgent' TO 'very high';


/* ******************************************************************************* 
https://www.postgresqltutorial.com/postgresql-tutorial/postgresql-user-defined-data-types/

DOMAINS
CREATE DOMAIN creates a user-defined data type with constraints such as NOT NULL, CHECK, etc

Get all domains for a schema:

SELECT typname 
FROM pg_catalog.pg_type 
  JOIN pg_catalog.pg_namespace 
  	ON pg_namespace.oid = pg_type.typnamespace 
WHERE 
	typtype = 'd' and nspname = '<schema_name>';
*/

/* Instead of using CHECK for each table like this: */
CREATE TABLE mailing_list (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR NOT NULL,
    last_name VARCHAR NOT NULL,
    email VARCHAR NOT NULL,
    CHECK (
        first_name !~ '\s'
        AND last_name !~ '\s'
    )
);
/* use re-usable domains: */
CREATE DOMAIN contact_name AS 
VARCHAR NOT NULL CHECK (value !~ '\s');

CREATE TABLE mailing_list (
    id serial PRIMARY KEY,
    first_name contact_name,
    last_name contact_name,
    email VARCHAR NOT NULL
);

/* 
TYPES
CREATE TYPE statement allows you to create a composite type, which can be used as the return type of a function
*/
CREATE TYPE film_summary AS (
    film_id INT,
    title VARCHAR,
    release_year SMALLINT
); 

CREATE OR REPLACE FUNCTION get_film_summary (f_id INT) 
    RETURNS film_summary AS 
$$ 
SELECT film_id, title, release_year
FROM film
WHERE film_id = f_id ; 
$$ 
LANGUAGE SQL;

SELECT * FROM get_film_summary (40);

/* ******************************************************************************* 
/* ******************************************************************************* 
/* ******************************************************************************* 