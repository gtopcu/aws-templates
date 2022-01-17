
if (err) throw err;

try {
    throw 'this is an error!'    
} catch(err) {

}
if(a <= 0 || b <= 0) throw new Error("Input values should be > 0");

//Promise-then-catch-finally
const fetch = require('node-fetch');
fetch('https://jsonplaceholder.typicode.com/todos/1')
    .then(res => res.json())
    .then(user => console.log(user.title))
    .catch(err => console.log(err))
    .finally(console.log("Done"));