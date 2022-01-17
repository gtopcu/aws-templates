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