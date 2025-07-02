
# https://www.youtube.com/watch?v=miEFm1CyjfM
# https://www.psycopg.org/docs/cursor.html
# https://www.postgresqltutorial.com/postgresql-tutorial/postgresql-data-types/
# https://neon.tech/postgresql/postgresql-python/connect

# pip install psycopg2
# pip install psycopg2-binary==2.9.9

# just like using sqlite3
import psycopg2
import psycopg2.extras

# conn = psycopg2.connect(
#     host="localhost",
#     database="XXXXXXXX",
#     user="XXXXXXXX",
#     password="XXXXXXXX")

# engine = create_engine(f"postgresql+psycopg://postgres:PWD@localhost:5432/my_database")
with psycopg2.connect(host="localhost", database="XXX", user="XXX", password="XXX", port=5432) as conn:
    with conn.cursor() as cur:
        cur.execute("""SELECT * FROM user""")
        records = cur.fetchall()
        for record in records:
            print(record)

# cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
# cur.execute("SELECT * FROM user")
# records = cur.fetchall() # list[DictRow]
# for record in records:
#     print(record["name"], record["age"])

# conn.autocommit = True
cur = conn.cursor()
# cur.binary_types
# cur.arraysize
# cur.scrollable
# cur.cast(None, None)
# cur.executemany(None, None)
# cur.itersize
# cur.lastrowid
# cur.pgresult_ptr
# cur.rowcount
# cur.rownumber
# cur.statusmessage

# conn.rollback()
# cur.close()
# conn.close()

# SELECT SELECT DISTINCT ORDER BY LIMIT OFFSET GROUP BY HAVING
# WHERE AND OR LIMIT FETCH IN BETWEEN LIKE IS NULL ANY ALL EXISTS
# CAST SUM, AVG, MIN, MAX, FLOOR, CEIL, ROUND, LIKE, COUNT, COUNT_DISTINCT, UNION/INTERSECT, 
# COUNT_ALL = range(8), range(8, 16), range(16, 24), range(24, 32), range(32, 40), range(40, 48), range(48, 56)

# "SELECT DISTINCT name FROM user WHERE name LIKE '%Jen%' AND age NOT BETWEEN 10 AND 15 LIMIT 10"
# cur.execute("""SELECT * FROM XXXXXXXX WHERE XXXXXXXX = XXXXXXXX""")
# rows = cur.fetchall() | fetchone() | fetchmany(size)
# for row in rows:
#     print(row)    # tuple
#     print(row[0])

# cur.execute("UPDATE user SET salary = (salary * 2) WHERE id = 1")
# cur.mogrify("INSERT INTO test (num, data) VALUES (%s, %s)", (42, 'bar'))

# insert_script = 'INSERT INTO test (num, data) VALUES (%s, %s)'
# insert_values = [(1, 'foo'), (2, 'bar')]
# for values in insert_values:
#     cur.execute(insert_script, values)
#     cur.execute(query=insert_script, vars=values, with_cols=False, with_rows=False, \
#       with_row_count=False, with_lastrowid=False, with_statusmessage=False)
#       conn.commit()

# cur.execute("""CREATE TABLE IF NOT EXISTS "person" (
#     id            SERIAL PRIMARY KEY NOT NULL,
#     uuid          UUID,
#     name          VARCHAR(100) NOT NULL,
#     AGE           INT,
#     gender        CHAR(1),
#     money         NUMERIC(10, 2) DEFAULT 0,
#     remaining     FLOAT(2),
#     description   TEXT,
#     logo          BYTEA,
#     json_data     JSON,
#     is_active     BOOLEAN, 
#     birth_date    DATE,
#     created_at    TIMESTAMPZ,
#     employee_id   INT,
#     CONSTRAINT fk_emp FOREIGN KEY (employee_id) REFERENCES "employee"(id)
#""")

# sql = cur.mogrify("SELECT * FROM person WHERE id = %s", (1,))
# sql = cur.mogrify("""SELECT * FROM person WHERE starts_with(name, %s) AND age < %s""", ("F", 10))
# cur.execute(sql)
# rows = cur.fetchall()
# print(rows)

# sql = "DELETE FROM user WHERE id = %s"
# ids = (1, )
# cur.execute(sql, ids)

# def insert(data : List[Tuple[str, str, str, bool]], host : str):
#     conn = psycopg2.connect(host=host, port=port, database=database, user=user, password=password) # type: ignore
#     cur = conn.cursor()
#     cleaned_data = [[elem if elem != '' else None for elem in row] for row in data]
#     args_str = b','.join(cur.mogrify("(%s, %s, %s, %s, CURRENT_TIMESTAMP)", row) for row in cleaned_data)
#     cur.execute(b'insert into labeled_phrases (phrase, category, wiki_entity_name, good_for_wiki, creation_date_time) values ' + args_str)
#     conn.commit()
#     cur.close()
#     conn.close()
#     return

# Insert/Read BYTEA
# https://www.postgresqltutorial.com/postgresql-python/blob/
# cur.execute("INSERT INTO part_drawings(part_id,file_extension,drawing_data) " +
#                             "VALUES(%s,%s,%s)",
#                             (part_id, file_extension, psycopg2.Binary(data)))
