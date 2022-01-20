//npm i lodash
function capitilize (str) {
    var lowercasedStr = _.toLower();
    var firstLetter = _.chain(lowercasedStr).head().toUpper().value()
    var tail = _.chain(lowercasedStr).tail().join('').value();
    return firstLetter + tail; 
}


//npm i luxon
const luxon = require('luxon'); 
const oldDate = luxon.DateTime.local();
const result = oldDate.setZone("UTC+3").minus({ weeks:1 }).startOf('day').toISO();
console.log("Old Date: " + oldDate.toString());
console.log("New Date: " + result);


//npm i query-string
const { stringify } = require('querystring');
const apiURL = "https://api.com?version=1&param={1,2,3}"
const parsedURL = parseURL(apiURL);
const stringifiedParams = stringify( {limit, offset, parsedURL} );
const apiURLWithParams = `${parsedURL.url}?${stringifiedParams}`;