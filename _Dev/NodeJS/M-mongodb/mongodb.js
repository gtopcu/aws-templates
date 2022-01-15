
//https://www.w3schools.com/nodejs/nodejs_mongodb.asp

//npm install mongodb

var mongo = require('mongodb');

//Create Database
var MongoClient = require('mongodb').MongoClient;
var url = "mongodb://localhost:27017/mydb";

MongoClient.connect(url, function(err, db) {
  if (err) throw err;
  console.log("Database created!");
  db.close();
});


//Create Collection
var MongoClient = require('mongodb').MongoClient;
var url = "mongodb://localhost:27017/";

MongoClient.connect(url, function(err, db) {
  if (err) throw err;
  var dbo = db.db("mydb");
  dbo.createCollection("customers", function(err, res) {
    if (err) throw err;
    console.log("Collection created!");
    db.close();
  });
});


//Insert
var MongoClient = require('mongodb').MongoClient;
var url = "mongodb://localhost:27017/";
MongoClient.connect(url, function(err, db) {
    if (err) throw err;
    var dbo = db.db("mydb");
    var myobj = { name: "Company Inc", address: "Highway 37" };
    dbo.collection("customers").insertOne(myobj, function(err, res) {
      if (err) throw err;
      console.log("1 document inserted");
      db.close();
    });
  });


//Insert Multiple
var MongoClient = require('mongodb').MongoClient;
var url = "mongodb://localhost:27017/";

MongoClient.connect(url, function(err, db) {
  if (err) throw err;
  var dbo = db.db("mydb");
  var myobj = [
    { name: 'John', address: 'Highway 71'},
    { name: 'Peter', address: 'Lowstreet 4'},
    { name: 'Amy', address: 'Apple st 652'},
    { name: 'Hannah', address: 'Mountain 21'},
    { name: 'Michael', address: 'Valley 345'},
    { name: 'Sandy', address: 'Ocean blvd 2'},
    { name: 'Betty', address: 'Green Grass 1'},
    { name: 'Richard', address: 'Sky st 331'},
    { name: 'Susan', address: 'One way 98'},
    { name: 'Vicky', address: 'Yellow Garden 2'},
    { name: 'Ben', address: 'Park Lane 38'},
    { name: 'William', address: 'Central st 954'},
    { name: 'Chuck', address: 'Main Road 989'},
    { name: 'Viola', address: 'Sideway 1633'}
  ];
  dbo.collection("customers").insertMany(myobj, function(err, res) {
    if (err) throw err;
    console.log("Number of documents inserted: " + res.insertedCount);
    db.close();
  });
});

/*
When executing the insertMany() method, a result object is returned.
The result object contains information about how the insertion affected the database.
The object returned from the example above looked like this:
{
  result: { ok: 1, n: 14 },
  ops: [
    { name: 'John', address: 'Highway 71', _id: 58fdbf5c0ef8a50b4cdd9a84 },
    { name: 'Peter', address: 'Lowstreet 4', _id: 58fdbf5c0ef8a50b4cdd9a85 },
    { name: 'Amy', address: 'Apple st 652', _id: 58fdbf5c0ef8a50b4cdd9a86 },
    { name: 'Hannah', address: 'Mountain 21', _id: 58fdbf5c0ef8a50b4cdd9a87 },
    { name: 'Michael', address: 'Valley 345', _id: 58fdbf5c0ef8a50b4cdd9a88 },
    { name: 'Sandy', address: 'Ocean blvd 2', _id: 58fdbf5c0ef8a50b4cdd9a89 },
    { name: 'Betty', address: 'Green Grass 1', _id: 58fdbf5c0ef8a50b4cdd9a8a },
    { name: 'Richard', address: 'Sky st 331', _id: 58fdbf5c0ef8a50b4cdd9a8b },
    { name: 'Susan', address: 'One way 98', _id: 58fdbf5c0ef8a50b4cdd9a8c },
    { name: 'Vicky', address: 'Yellow Garden 2', _id: 58fdbf5c0ef8a50b4cdd9a8d },
    { name: 'Ben', address: 'Park Lane 38', _id: 58fdbf5c0ef8a50b4cdd9a8e },
    { name: 'William', address: 'Central st 954', _id: 58fdbf5c0ef8a50b4cdd9a8f },
    { name: 'Chuck', address: 'Main Road 989', _id: 58fdbf5c0ef8a50b4cdd9a90 },
    { name: 'Viola', address: 'Sideway 1633', _id: 58fdbf5c0ef8a50b4cdd9a91 } ],
  insertedCount: 14,
  insertedIds: [
    58fdbf5c0ef8a50b4cdd9a84,
    58fdbf5c0ef8a50b4cdd9a85,
    58fdbf5c0ef8a50b4cdd9a86,
    58fdbf5c0ef8a50b4cdd9a87,
    58fdbf5c0ef8a50b4cdd9a88,
    58fdbf5c0ef8a50b4cdd9a89,
    58fdbf5c0ef8a50b4cdd9a8a,
    58fdbf5c0ef8a50b4cdd9a8b,
    58fdbf5c0ef8a50b4cdd9a8c,
    58fdbf5c0ef8a50b4cdd9a8d,
    58fdbf5c0ef8a50b4cdd9a8e,
    58fdbf5c0ef8a50b4cdd9a8f
    58fdbf5c0ef8a50b4cdd9a90,
    58fdbf5c0ef8a50b4cdd9a91 ]
}
*/


//Insert with _id
var MongoClient = require('mongodb').MongoClient;
var url = "mongodb://localhost:27017/";

MongoClient.connect(url, function(err, db) {
  if (err) throw err;
  var dbo = db.db("mydb");
  var myobj = [
    { _id: 154, name: 'Chocolate Heaven'},
    { _id: 155, name: 'Tasty Lemon'},
    { _id: 156, name: 'Vanilla Dream'}
  ];
  dbo.collection("products").insertMany(myobj, function(err, res) {
    if (err) throw err;
    console.log(res);
    db.close();
  });
});


//FindOne
var MongoClient = require('mongodb').MongoClient;
var url = "mongodb://localhost:27017/";

MongoClient.connect(url, function(err, db) {
  if (err) throw err;
  var dbo = db.db("mydb");
  dbo.collection("customers").findOne({}, function(err, result) {
    if (err) throw err;
    console.log(result.name);
    db.close();
  });
});


//FindAll
var MongoClient = require('mongodb').MongoClient;
var url = "mongodb://localhost:27017/";

MongoClient.connect(url, function(err, db) {
  if (err) throw err;
  var dbo = db.db("mydb");
  dbo.collection("customers").find({}).toArray(function(err, result) {
    if (err) throw err;
    console.log(result);
    db.close();
  });
});


//Find with projection
var MongoClient = require('mongodb').MongoClient;
var url = "mongodb://localhost:27017/";

MongoClient.connect(url, function(err, db) {
  if (err) throw err;
  var dbo = db.db("mydb");
  dbo.collection("customers").find({}, { projection: { _id: 0, name: 1, address: 1 } }).toArray(function(err, result) {
    if (err) throw err;
    console.log(result);
    db.close();
  });
});
