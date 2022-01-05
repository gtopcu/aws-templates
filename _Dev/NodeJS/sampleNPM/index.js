
/*
npm -v
npm install -g nodemon (live output)
npm i moment (datetime pretty print - momentjs.com)

npm init
nodemon index.js

npm i -g browserify
npm i uniq

*/

var author = "hukanege";
var myDate = new Date();

console.log(author);
console.log(myDate);

var moment = require('moment');
console.log(moment(myDate).format());
console.log(moment(myDate).format("YYYY-MM-DD"));
console.log(moment(myDate).format("LL"));

var myArray = [1, 2, 2, 3, 3, 3];
var unique = require("uniq");
console.log(unique());

