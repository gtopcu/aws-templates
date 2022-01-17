
// https://www.w3schools.com/nodejs/nodejs_events.asp

//Objects in Node.js can fire events, like the readStream object fires events when opening and closing a file:
var fs = require("fs");
var rs = fs.createReadStream("./demofile.txt");
rs.on("open", function () {
    console.log("The file is open");
});

/*
Node.js has a built-in module, called "Events", where you can create-, fire-, and listen for- your own events.
All event properties and methods are an instance of an EventEmitter object. To be able to access these properties 
and methods, create an EventEmitter object.

You can assign event handlers to your own events with the EventEmitter object.
In the example below we have created a function that will be executed when a "scream" event is fired.
To fire an event, use the emit() method
*/
var events = require('events');
var eventEmitter = new events.EventEmitter();

//Create an event handler:
var myEventHandler = function () {
  console.log('I hear a scream!');
}

//Assign the event handler to an event:
eventEmitter.on('scream', myEventHandler);

//Fire the 'scream' event:
eventEmitter.emit('scream');
