

/* https://www.postgresqltutorial.com/postgresql-tutorial/postgresql-data-types/ */

CREATE TABLE IF NOT EXISTS "person" (
     id                  INT PRIMARY KEY GENERATED ALWAYS AS IDENTITY, /*SERIAL PRIMARY KEY,*/
     contact_id          uuid DEFAULT gen_random_uuid(),
     name                VARCHAR(100) NOT NULL,
     AGE                 INT,
     gender              CHAR(1),
     money               NUMERIC(10, 2) DEFAULT 0,
     phones              TEXT [],
     single_digit        REAL,
     remaining           FLOAT(2), /* = FLOAT8, DOUBLE PRECISION) */
     logo                BYTEA,
     json_data           JSON,
     is_active           BOOLEAN, 
     birth_date          DATE DEFAULT CURRENT_DATE,
     created_at          TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP,
     create_time         TIME(2), 
     employee_id         INT,
     CONSTRAINT fk_emp FOREIGN KEY (employee_id) REFERENCES "employee"(id)
)
CREATE UNIQUE INDEX indx1 ON "person" (name)

SELECT "person".*, "employee".title AS emp_title FROM "person"
JOIN "employee" ON "employee".id = "person".employee_id

SELECT * FROM user WHERE name LIKE '%Jen%'

/*

BOOLEAN = BOOL
CHAR(n) | VARCHAR(n) | TEXT
SMALLINT                           -> 2 bytes
INT=INT4=INTEGER                   -> 4 bytes
NUMERIC(n,p) | DECIMAL(n,p)
REAL                                              -> 4 byte, single precision
FLOAT(n) = FLOAT8(n) = DOUBLE PRECISION           -> 8 byte, double precision
DATE | TIME | TIMESTAMP | TIMESTAMPTZ | INTERVAL
JSON | JSONB
XML
BYTEA (max 1GB)
UUID
Array
hstore

Special data types:
box – a rectangular box
line – a set of points
point – a geometric pair of numbers
lseg – a line segment
polygon – a closed geometric
inet – an IP4 address
macaddr– a MAC address


Boolean
A Boolean data type can hold one of three possible values: true, false, or null. You use boolean or bool keyword to declare a 
column with the Boolean data type. When you insert data into a Boolean column, PostgreSQL converts it to a Boolean value
- 1, yes, y, t, true values are converted to true
- 0, no, false, f values are converted to false.
When you select data from a Boolean column, PostgreSQL converts the values back e.g., t to true, f to false and space to null.

Character:
CHAR(n) is the fixed-length character with space padded. If you insert a string that is shorter than the length of the column, 
PostgreSQL pads spaces. If you insert a string that is longer than the length of the column, PostgreSQL will issue an error.
VARCHAR(n) is the variable-length character string. The VARCHAR(n) allows you to store up to n characters. 
PostgreSQL does not pad spaces when the stored string is shorter than the length of the column.
TEXT is the variable-length character string. Theoretically, text data is a character string with unlimited length.

Integer:
Small integer (SMALLINT) -> 2-byte signed integer that has a range from -32,768 to 32,767.
INT = INT4 = INTEGER     -> 4-byte integer that has a range from -2,147,483,648 to 2,147,483,647.

Floating-point number:
float(n)  is a floating-point number whose precision, is at least, n, up to a maximum of 8 bytes.
real -> single precision
float=float8=DOUBLE PRECISION -> 4-byte floating-point number
numeric or numeric(p,s) is a real number with p digits with s number after the decimal point. This numeric(p,s) is the exact number.

Temporal data types:
DATE stores the dates only.
TIME stores the time of day values.
TIMESTAMP stores both date and time values.
TIMESTAMPTZ is a timezone-aware timestamp data type. It is the abbreviation for timestamp with the time zone.
INTERVAL stores periods.
The TIMESTAMPTZ is PostgreSQL’s extension to the SQL standard’s temporal data types.

Arrays
In PostgreSQL, you can store an array of strings, an array of integers, etc., in array columns. The array comes in handy 
in some situations e.g., storing days of the week, and months of the year.

JSON
JSON  -> plain JSON data that requires reparsing for each processing
JSONB -> JSON data in a binary format which is faster to process but slower to insert. supports indexing

UUID
The UUID data type allows you to store Universal Unique Identifiers defined by RFC 4122 The UUID values guarantee a better 
uniqueness than SERIAL and can be used to hide sensitive data exposed to the public such as values of id in URL.

*/