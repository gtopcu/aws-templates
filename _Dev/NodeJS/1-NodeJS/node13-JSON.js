
exports.handler = (event, context, callback) => {
    console.log('Received event:', JSON.stringify(event, null, 2));
    console.log('value1 =', event.key1);
    console.log('value2 =', event.key2);
    console.log('value3 =', event.key3);
    callback(null, event.key1);  // Echo back the first key value
    //callback('Something went wrong');
};

const json = { name:"john", age:32, languages:["en", "fr"] }
console.log(json);

var jsonStr = JSON.stringify(json);
var jsonObj = JSON.parse(jsonStr);


var userJSON = {
    "userId": 1,
    "id": 1,
    "title": "delectus aut autem",
    "completed": false
  };
  JSON.stringify(userJSON);







