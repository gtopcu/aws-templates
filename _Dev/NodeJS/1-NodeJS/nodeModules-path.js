
const path = require("path");
var filenamePath = path.parse(__filename);
console.log("Root: " + filenamePath.root);
console.log("Dir: " + filenamePath.dir);
console.log("Base: " + filenamePath.base);
console.log("Name: " + filenamePath.name);
console.log("Ext: " + filenamePath.ext);

