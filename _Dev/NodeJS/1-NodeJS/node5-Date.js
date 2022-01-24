/*
Date.now();
Date.UTC();

var myDate = new Date();
console.log(myDate);
*/

function delay(miliseconds) {
	let start = Date.now();
	console.log(start);
	while((Date.now() - start) < miliseconds) {}
	console.log(Date.now());
}
delay(2000);

let delayMs = 3000;
let start = Date.now();
while((Date.now() - start) < delayMs) {}

//npm i luxon
const luxon = require('luxon'); 
const oldDate = luxon.DateTime.local();
const result = oldDate.setZone("UTC+3").minus({ weeks:1 }).startOf('day').toISO();
console.log("Old Date: " + oldDate.toString());
console.log("New Date: " + result);