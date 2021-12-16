var port = 80;
var http = require("http");
http.createServer(function (request, response) {
    
    // Log the request
    console.log('Request received');

    // Send the HTTP header 
    // HTTP Status: 200 : OK
    // Content Type: text/plain
    response.writeHead(200, {'Content-Type': 'text/plain'});

    // Send the response body as "Hello World"
    response.end('Hello World\n');

 }).listen(port);
 
 // Console will print the message
 console.log('Server running at http://localhost:' + port);