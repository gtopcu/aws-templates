
/*
let p = new Promise((resolve, reject) => {
	if(1 == 1) resolve('success');
	else reject('fail');
});
p.then(result => console.log(result))
 .catch(err => console.log(err));

return Promise.all([f1, f2]); //waits for all tasks to finish
return Promise.race([f1, f2]); //first one to finish returns
*/

//Async functions return Promise
const myAsync = async() => {
	return "helo";
}
myAsync().then(result => console.log(result));

/*

//Event loop - microtask
//setTimeout & setInterval -> executed at next event loop
//promise -> called before the start of the next event loop
//https://www.youtube.com/watch?v=vn3tm0quoqE

console.log("synch 1");
setTimeout(_ => console.log("timeout") , 0);
Promise.resolve().then(_ => console.log("promise")); //executes before setTimeout
console.log("sync 2");

//Promise-then-catch-finally
const fetch = require('node-fetch');
fetch('https://jsonplaceholder.typicode.com/todos/1')
    .then(res => res.json())
    .then(user => console.log(user.title))
    .catch(err => console.log(err))
    .finally(console.log("fetch finally"));

//Function returning promise - resolve runs on main thread
const myPromisingFunction = () => {
	return new Promise((resolve, reject) => {
		let i = 0;
		while(i < 1000000000) {
			i++;
		}
		resolve('resolve1 done'); //runs on the main thread
	})
};
myPromisingFunction().then(str => console.log(str));

//Same function running as a separate mikrotask
const myPromisingFunction2 = () => {
	return Promise.resolve('resolve2 done')
		.then( v => { 
			let i = 0;
			while(i < 1000000000) {
				i++;
			}
		});
};
myPromisingFunction2().then(str => console.log(str));


//Async functions - returns Promise
const getFruit = async(name) => {
	const fruits = {
		peach: 1,
		apple: 2,
		banana: 3
	}
	return fruits[name];
};
//getFruit('banana').then(res => console.log(res));
/*
//Execute & wait each step
async function getFruits() {
	let f1 = await getFruit('banana');
	let f2 = await getFruit('apple');
	return [f1, f2];
}
getFruits().then(res => console.log(res));

//Execute in parallel
async function getFruitsParallel() {
	try {
		let f1 = await getFruit('banana');
		let f2 = await getFruit('apple');
		//throw 'boo';
		return Promise.all([f1, f2]); //waits for all tasks to finish
		return Promise.race([f1, f2]); //first one to finish returns
	}
	catch(err) {
		throw err;
	}
}
getFruitsParallel().then(res => console.log(res)).catch(err => console.log(err));

let fruits = ['peach', 'apple', 'banana'];
const smoothie = fruits.map(v => getFruit(v));
console.log(smoothie);

const fruitLoop = async() => {
	for (const f of fruits) {
		const fruitID = await getFruit(f);
		console.log(fruitID);
	}
}
fruitLoop().then();

//for / of with await
const fruitLoop2 = async() => {
	for await (const f of smoothie) {
		console.log(f);
	}
}
fruitLoop2().then();


//if with await
const fruitInspection = async() => {
	if (await getFruit('apple') == 1) {
		console.log("if with await")
	}
}

console.log("done");
*/

