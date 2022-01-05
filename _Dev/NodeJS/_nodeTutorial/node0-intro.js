/*
    nodejs.org
    https://nodejs.org/dist/latest-v16.x/docs/api/

    /usr/local/bin/node
    /usr/local/bin/npm
    /usr/local/bin/npm-modules
    export PATH=$PATH:/usr/local/nodejs/bin

    node index.js
    nodemon index.js
    jshint index.js
    Quokka: Command+K -> Q 
    
    - Async, non-blocking architecture based on C++ wrapper around Google v8 Engine
    - Single threaded - distributes events - checks the event queue for new events
    - Perfect for IO intensive apps (file, network, DB) but not for CPU intensive apps (i.e. video encoding)

    https://www.youtube.com/watch?v=TlB_eWDSMt4
    https://codewithmosh.com/p/the-complete-node-js-course
*/

var myDate = new Date();
console.log(myDate);
console.log("hello");

var a = 1;
const json = { name:"john", age:32, languages:["en", "fr"] }
console.log(json);
const array = [1, 2, 3];
console.log(array);

function add(a, b) {
    if(a <= 0 || b <= 0) throw new Error("Input values should be > 0");
    console.log(a + b);
}
console.log(add(0+2));

function sayHello(name) {
    console.log("Hello " + name);
}
sayHello("Gokhan");

