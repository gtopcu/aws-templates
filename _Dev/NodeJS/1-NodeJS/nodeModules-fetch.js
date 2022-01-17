
//https://www.npmjs.com/package/node-fetch
//https://stackabuse.com/making-http-requests-in-node-js-with-node-fetch/
//npm install node-fetch@2.0

/*
The url parameter is simply the direct URL to the resource we wish to fetch. It has to be an absolute URL 
or the function will throw an error. The optional options parameter is used when we want to use fetch() 
for anything other than a simple GET request

The function returns a Response object that contains useful functions and information about the HTTP response, 
such as:

text() - returns the response body as a string
json() - parses the response body into a JSON object, and throws an error if the body can't be parsed
status and statusText - contain information about the HTTP status code
ok - equals true if status is a 2xx status code (a successful request)
headers - an object containing response headers, a specific header can be accessed using the get() function.
*/

/*  if using ES Module - npm install node-fetch@3.0
    import fetch from 'node-fetch';
    const promise = fetch('https://jsonplaceholder.typicode.com/todos/1');
    promise.then(res => res.json())
       .then(user => console.log(user.title))
       .catch(err => console.log(err))
       .finally(console.log("Done"));
*/

const fetch = require('node-fetch');

var userJSON = {
  "userId": 1238231234,
  "id": 1324912312321,
  "title": "delectus aut autem",
  "completed": false
};

//GET
fetch('https://jsonplaceholder.typicode.com/todos/1')
    .then(res => res.json())
    .then(user => console.log(user.title))
    .catch(err => console.log(err))
    .finally(console.log("Get Done"));

//POST
fetch('https://jsonplaceholder.typicode.com/todos', {
    method: 'POST',
    body: JSON.stringify(userJSON),
    headers: { 'Content-Type': 'application/json' }
}).then(res => res.json())
  .then(json => console.log(json))
  .catch(err => console.log(err))
  .finally(console.log("POST Done"));

//Error handling
function checkResponseStatus(res) {
  if(res.ok){
      return res
  } else {
      throw new Error(`The HTTP status of the reponse: ${res.status} (${res.statusText})`);
  }
}
fetch('https://jsonplaceholder.typicode.com/MissingResource')
  .then(checkResponseStatus)
  .then(res => res.json())
  .then(json => console.log(json))
  .catch(err => console.log(err));