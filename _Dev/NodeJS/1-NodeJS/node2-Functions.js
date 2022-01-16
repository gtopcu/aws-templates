var myFunc = function () {
	console.log("in function 1");
};

var myFunc2 = () => {
	console.log("in function 2");
};

setTimeout(myFunc, 2000);
setTimeout(myFunc2, 4000);

async function myAsyncFunc() {
	console.log("my async function");
}

var result = await myAsyncFunc();
