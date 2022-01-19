/*
https://www.youtube.com/watch?v=ahCwqrYpIuM

npm i -g typescript

tsc --version - 4.5.4
tsc index.ts - convert to js
touch tsconfig.json + tcs
*/

console.log("helo from TS!");

let anyType: any = 23;
//let numType: number = '23';
let strType: string = 'heloo';

let i = 1;
//i = '1';

//type Style = string;
type Style = 'bold || italic || 23';
let font: Style; 

const arr: number[] = [];
arr.push(1);
//arr.push('1');

async () => {
    console.log("async func");
}

//return can be void
function add(x: number, y: number): string {
    return (x + y).toString();
}

const url = new URL("google.com");

//Generics
class Observable<T> {
    constructor(public value: T) {}
}
let x: Observable<number>;
let y = new Observable(1);