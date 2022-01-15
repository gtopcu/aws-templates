//Sample module to be loaded

var url = "http://api.com";

function logMessage(message) {
    console.log(message);
}

//export a variable
exports.endpoint = url; //can change the name

//export as an object
//module.exports.logMessage = logMessage;

//export as a single function 
//module.exports = logMessage;

//export directly
exports.myDateTime = function () {
  return Date();
};

