
//https://www.w3schools.com/nodejs/nodejs_mysql.asp

//npm install mysql

var mysql = require('mysql');

//Connect
var con = mysql.createConnection({
    host: "localhost",
    user: "yourusername",
    password: "yourpassword"
});

con.connect(function(err) {
  if (err) throw err;
  console.log("Connected!");
});


//Query
con.connect(function(err) {
    if (err) throw err;
    console.log("Connected!");
    con.query(sql, function (err, result) {
      if (err) throw err;
      console.log("Result: " + result);
    });
});


//Create DB
con.connect(function(err) {
    if (err) throw err;
    console.log("Connected!");
    con.query("CREATE DATABASE mydb", function (err, result) {
      if (err) throw err;
      console.log("Database created");
    });
  });


//Create table
var con = mysql.createConnection({
  host: "localhost",
  user: "yourusername",
  password: "yourpassword",
  database: "mydb"
});

con.connect(function(err) {
  if (err) throw err;
  console.log("Connected!");
  var sql = "CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))";
  con.query(sql, function (err, result) {
    if (err) throw err;
    console.log("Table created");
  });
});

con.connect(function(err) {
    if (err) throw err;
    console.log("Connected!");
    var sql = "CREATE TABLE customers (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), address VARCHAR(255))";
    con.query(sql, function (err, result) {
      if (err) throw err;
      console.log("Table created");
    });
  });


//INSERT
con.connect(function(err) {
    if (err) throw err;
    console.log("Connected!");
    var sql = "INSERT INTO customers (name, address) VALUES ('Company Inc', 'Highway 37')";
    con.query(sql, function (err, result) {
      if (err) throw err;
      console.log("1 record inserted");
    });
  });


//UPDATE
con.connect(function(err) {
    if (err) throw err;
    var sql = "UPDATE customers SET address = 'Canyon 123' WHERE address = 'Valley 345'";
    con.query(sql, function (err, result) {
      if (err) throw err;
      console.log(result.affectedRows + " record(s) updated");
    });
  });


//SELECT
con.connect(function(err) {
    if (err) throw err;
    con.query(  "SELECT * FROM customers WHERE address = 'Park Lane 38' LIMIT 5 OFFSET 2 ORDER BY name", 
                //"SELECT * FROM customers WHERE address LIKE 'S%'" - Starts with S
                //"SELECT * FROM customers WHERE address = "" + mysql.escape(adr); - for preventing SQL Injection

        function (err, result) {
            if (err) throw err;
            console.log(result);
        });
  });

//Escape query variables
var name = 'Amy';
var adr = 'Mountain 21';
var sql = 'SELECT * FROM customers WHERE name = ? OR address = ?';
con.query(sql, [name, adr], function (err, result) {
  if (err) throw err;
  console.log(result);
});

//DELETE
con.connect(function(err) {
    if (err) throw err;
    var sql = "DELETE FROM customers WHERE address = 'Mountain 21'";
    con.query(sql, function (err, result) {
      if (err) throw err;
      console.log("Number of records deleted: " + result.affectedRows);
    });
  });
  /*
    The result object returned from the example above looks like this:
    {
        fieldCount: 0,
        affectedRows: 1,
        insertId: 0,
        serverStatus: 34,
        warningCount: 0,
        message: '',
        protocol41: true,
        changedRows: 0
    }
  */


//DROP TABLE
con.connect(function(err) {
    if (err) throw err;
    var sql = "DROP TABLE IF EXISTS customers";
    con.query(sql, function (err, result) {
        if (err) throw err;
        console.log(result);
    });
    });   


//JOIN
con.connect(function(err) {
    if (err) throw err;
    var sql = "SELECT users.name AS user, products.name AS favorite FROM users JOIN products " +
                + "ON users.favorite_product = products.id";
    con.query(sql, function (err, result) {
      if (err) throw err;
      console.log(result);
    });
  });