
const myFunc = function () {
	console.log("in function 1");
};

const myFunc2 = () => {
	console.log("in function 2");
};

const callbackFunc = (callback) => {
	callback('calling u back');
}
callbackFunc((message) => {console.log(message)});

