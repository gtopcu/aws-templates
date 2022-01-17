
/*
const myArray = [1, 2, 3];
console.log(myArray[0]);
Array.from();
myArray.length();
myArray.map();
myArray.filter();
myArray.forEach();
myArray.keys();
myArray.values();
myArray.find();
myArray.push(4);
myArray.pop();
myArray.concat();
myArray.find();
myArray.findIndex();
myArray.copyWithin();
myArray.indexOf();
myArray.lastIndexOf();
myArray.join();
myArray.reverse();
myArray.sort();
myArray.toString();
myArray.fill();
*/

const getFruit = (name) => {
	const fruits = {
		peach: 1,
		apple: 2,
		banana: 3
	}
	return fruits[name];
};
let fruits = ['peach', 'apple', 'banana'];
console.log(fruits.map(v => getFruit(v)));
