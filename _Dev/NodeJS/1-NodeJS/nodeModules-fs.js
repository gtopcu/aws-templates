
//https://www.w3schools.com/nodejs/nodejs_filesystem.asp

//readFile()
var http = require("http");
var fs = require("fs");
var filename = "nodeModules-fs.js";
http.createServer(function (req, res) {
    fs.readFile(filename, function(err, data) {
        res.writeHead(200, {"Content-Type": "text/html"});
        res.write(data);
        return res.end();
    });
}).listen(8080);
console.log("Serving at http://127.0.0.1:8080/");

/* 
    ****************************************************************************************
    fs.appendFile() -> creates if doesn"t exist
    ****************************************************************************************    
    var fs = require("fs");
    fs.appendFile("mynewfile1.txt", "Hello content!", function (err) {
        if (err) throw err;
        console.log("Saved!");
    });

    ****************************************************************************************
    fs.open() ->    Takes a "flag" as the second argument, if the flag is "w" for "writing", 
                    If the file does not exist, an empty file is created:
    ****************************************************************************************
    var fs = require("fs");
    fs.open("mynewfile2.txt", "w", function (err, file) {
        if (err) throw err;
        console.log("Saved!");
    });

    ****************************************************************************************
    fs.writeFile() ->   Replaces the specified file and content if it exists. 
                        If the file does not exist, a new file will be created:
    ****************************************************************************************
    var fs = require("fs");
    fs.writeFile("mynewfile3.txt", "Hello content!", function (err) {
        if (err) throw err;
        console.log("Saved!");
    });

    ****************************************************************************************
    fs.unlink() -> Deletes the specified file:
    ****************************************************************************************
    var fs = require("fs");
    fs.unlink("mynewfile2.txt", function (err) {
        if (err) throw err;
        console.log("File deleted!");
    });

    ****************************************************************************************
    fs.rename() -> Renames the specified file:
    ****************************************************************************************
    var fs = require("fs");
    fs.rename("mynewfile1.txt", "myrenamedfile.txt", function (err) {
        if (err) throw err;
        console.log("File Renamed!");
    });
*/