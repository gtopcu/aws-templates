
//https://www.w3schools.com/nodejs/nodejs_http.asp

var http = require("http");
var url = require("url");

http.createServer(function(request, response) {
        
        //Log the request
        console.log("Request received");
        
        //Read query string
        console.log("Request URL: " + request.url);
        //Split the query string using the URL module
        var q = url.parse(request.url, true).query;
        console.log("Query string name attr: " + q.name);

        // Send the HTTP header 
        // HTTP Status: 200 : OK
        // Content Type: text/plain
        response.writeHead(200, {"Content-Type": "text/plain"});
        // Send the response body as "Hello World"
        response.end("Hello World\n");

    }
    ).listen(8080);
 
 // Console will print the message
 console.log("Server running at http://127.0.0.1:8080/");