

var myFunc = function() {
    console.log("in function 1");
};

var myFunc2 = () => {
    console.log("in function 2");
};

setTimeout(myFunc, 2000);
setTimeout(myFunc2, 4000);
