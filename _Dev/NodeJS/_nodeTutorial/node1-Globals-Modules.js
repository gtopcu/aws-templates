/*
Globals:
    window/global.
        console
        setTimeout()    : Call function after delay
        clearTimeout()  : Clears timeout
        setInterval()   : Repeatedly call function with interval
        clearInterval() : Clears interval
*/

var myFunction = function() { //local to the module
    console.log("hello!");
};
//window.myFunction(); //available through window

//Every node app has one JS file, which is a module
console.log(global.module); //undefined, module is local
console.log(module);

setTimeout(myFunction, 3000);

//setting exports in a module:
//module.exports.endpoint = url;
//module.exports.logger = log;
//module.exports = logMessage;

//load and use the logger module
//const path = require("path"); - node assumes this is a built-in module
//const logger = require("../logger.js"); - parent folder
//const logger = require("./logger.js"); - no need for .js
const logger = require("./logger");
console.log(logger);
console.log(logger.endpoint);

//import a single function directly
//const logger2 = require("./logger");
//logger2("loaded as a function");

//Module Wrapper Function
//function(exports, require, module, __filename, __dirname) { }
console.log(__filename);
console.log(__dirname);

//Useful Built-in Modules - Path, OS, HTTP, Files, Process, QueryString etc
//https://nodejs.org/dist/latest-v16.x/docs/api/

//Path
const path = require("path");
var filenamePath = path.parse(__filename);
console.log("Root: " + filenamePath.root);
console.log("Dir: " + filenamePath.dir);
console.log("Base: " + filenamePath.base);
console.log("Name: " + filenamePath.name);
console.log("Ext: " + filenamePath.ext);

//OS
const os = require("os");
console.log(
    os.hostname  + " - " +
    os.platform  + " - " +
    //os.cpus      + " - " +
    os.freemem   + " - " +
    os.uptime
);


