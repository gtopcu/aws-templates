
//OS
const os = require("os");
console.log(
    os.hostname  + " - " +
    os.platform  + " - " +
    //os.cpus      + " - " +
    os.freemem   + " - " +
    os.uptime
);

