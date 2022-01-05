# https://www.w3schools.com/python/python_mysql_getstarted.asp
# python -m pip install mysql-connector-python

import mysql.connector

# Connect and create DB
mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  password="yourpassword"
)
print(mydb)

mycursor = mydb.cursor()
mycursor.execute("CREATE DATABASE mydatabase")

# Connect to an existing DB
mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  password="yourpassword",
  database="mydatabase"
)

# List DBs
mycursor = mydb.cursor()
mycursor.execute("SHOW DATABASES")
for x in mycursor:
  print(x)

# List Tables
mycursor.execute("SHOW TABLES")
for x in mycursor:
  print(x)

# Create Table
mycursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")

# Create table with auto-incrementing INT PK
mycursor.execute("CREATE TABLE customers (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), address VARCHAR(255))")

# Alter table
mycursor.execute("ALTER TABLE customers ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY") 

# Insert
sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = ("John", "Highway 21")
mycursor.execute(sql, val)
mydb.commit()
print(mycursor.rowcount, "record inserted.") 

# Insert multiple  
sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = [
  ('Peter', 'Lowstreet 4'),
  ('Amy', 'Apple st 652'),
  ('Hannah', 'Mountain 21'),
  ('Michael', 'Valley 345'),
  ('Sandy', 'Ocean blvd 2'),
  ('Betty', 'Green Grass 1'),
  ('Richard', 'Sky st 331'),
  ('Susan', 'One way 98'),
  ('Vicky', 'Yellow Garden 2'),
  ('Ben', 'Park Lane 38'),
  ('William', 'Central st 954'),
  ('Chuck', 'Main Road 989'),
  ('Viola', 'Sideway 1633')
]
mycursor.executemany(sql, val)
mydb.commit()
print(mycursor.rowcount, "was inserted.")

# Get the id of the row inserted. If inserted multiple, last one is returned
sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = ("Michelle", "Blue Village")
mycursor.execute(sql, val)
mydb.commit()
print("1 record inserted, ID:", mycursor.lastrowid)

# Select all records from the "customers" table, and display the result:
mycursor.execute("SELECT * FROM customers LIMIT 5 ORDER BY name")
myresult = mycursor.fetchall()
for x in myresult:
  print(x)

# Select only the name and address columns:
mycursor.execute("SELECT name, address FROM customers")
myresult = mycursor.fetchall()
for x in myresult:
  print(x)


# Fetch only one row:
mycursor.execute("SELECT * FROM customers")
myresult = mycursor.fetchone()
print(myresult)

# Select record(s) where the address is "Park Lane 38" and limit to 4: 
sql = "SELECT * FROM customers WHERE address ='Park Lane 38' LIMIT 4"
mycursor.execute(sql)
myresult = mycursor.fetchall()
for x in myresult:
  print(x)

# OFFSET - if you want to return five records, starting from the third record:
mycursor.execute("SELECT * FROM customers LIMIT 5 OFFSET 2")
myresult = mycursor.fetchall()
for x in myresult:
  print(x)
   
# Select records where the address contains the word "way":
mycursor = mydb.cursor()
sql = "SELECT * FROM customers WHERE address LIKE '%way%'"
mycursor.execute(sql)
myresult = mycursor.fetchall()
for x in myresult:
  print(x)

# Prevent SQL Injection
# The mysql.connector module has methods to escape query values
# Escape query values by using the placholder %s method:
sql = "SELECT * FROM customers WHERE address = %s"
adr = ("Yellow Garden 2", )
mycursor.execute(sql, adr)
myresult = mycursor.fetchall()
for x in myresult:
  print(x)

# ORDER BY name descending
sql = "SELECT * FROM customers ORDER BY name DESC"
mycursor.execute(sql)
myresult = mycursor.fetchall()
for x in myresult:
  print(x)

# Delete any record where the address is "Mountain 21": 
sql = "DELETE FROM customers WHERE address = 'Mountain 21'"
mycursor.execute(sql)
mydb.commit()
print(mycursor.rowcount, "record(s) deleted")

# Drop Table
sql = "DROP TABLE customers"
mycursor.execute(sql) 

# Drop only if exists
sql = "DROP TABLE IF EXISTS customers"
mycursor.execute(sql)

# Update
sql = "UPDATE customers SET address = 'Canyon 123' WHERE address = 'Valley 345'"
mycursor.execute(sql)
mydb.commit()
print(mycursor.rowcount, "record(s) affected") 

"""
JOIN
users
{ id: 1, name: 'John', fav: 154},
{ id: 2, name: 'Peter', fav: 154},
{ id: 3, name: 'Amy', fav: 155},
{ id: 4, name: 'Hannah', fav:},
{ id: 5, name: 'Michael', fav:}

products
{ id: 154, name: 'Chocolate Heaven' },
{ id: 155, name: 'Tasty Lemons' },
{ id: 156, name: 'Vanilla Dreams' }

These two tables can be combined by using users' fav field and products' id field.
"""

# You can use JOIN instead of INNER JOIN. They will both give you the same result.
# INNER JOIN only shows the records where there is a match.
sql = "SELECT \
  users.name AS user, \
  products.name AS favorite \
  FROM users \
  INNER JOIN products ON users.fav = products.id"

mycursor.execute(sql)
myresult = mycursor.fetchall()
for x in myresult:
  print(x)

# LEFT JOIN
# If you want to show all users, even if they do not have a favorite product, use the LEFT JOIN statement:
sql = "SELECT \
  users.name AS user, \
  products.name AS favorite \
  FROM users \
  LEFT JOIN products ON users.fav = products.id"

# RIGHT JOIN
# If you want to return all products, and the users who have them as their favorite, even if no user have them 
# as their favorite, use the RIGHT JOIN statement:
sql = "SELECT \
  users.name AS user, \
  products.name AS favorite \
  FROM users \
  RIGHT JOIN products ON users.fav = products.id"

# OUTER JOIN, FULL JOIN




