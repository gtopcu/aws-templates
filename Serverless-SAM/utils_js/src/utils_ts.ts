//https://www.w3schools.com/typescript/typescript_intro.php

/* 

17-03-2024
Version 5.4.2
tsc: The TypeScript Compiler - Version 5.4.2      

npm install typescript --save-dev

npx tsc --init
npx tsc

tsconfig.json:
{
  "include": ["src"],
  "compilerOptions": {
    "outDir": "./build"
  }
}

There are three main primitives in JavaScript and TypeScript:
    - boolean - true or false values
    - number - whole numbers and floating point values
    - string - text values like "TypeScript Rocks"

There are also 2 less common primitives used in later versions of Javascript and TypeScript:
    - bigint - whole numbers and floating point values, but allows larger negative and positive numbers
    - symbol are used to create a globally unique identifier.

Explicit/Implicit typing:
let firstName: string = "Dylan";
let firstName = "Dylan";

TypeScript may not always properly infer what the type of a variable may be. In such cases, 
it will set the type to any which disables type checking. This behavior can be disabled by 
enabling noImplicitAny:

// Implicit any as JSON.parse doesn't know what type of data it returns so it can be "any" thing...
const json = JSON.parse("55");
// Most expect json to be an object, but it can be a string or a number like this example
console.log(typeof json);

Setting any to the special type any disables type checking:
let v: any = true;

unknown is a similar, but safer alternative to any. TypeScript will prevent unknown types from being used
never effectively throws an error whenever it is defined
undefined and null are types that refer to the JavaScript primitives undefined and null respectively.
let y: undefined = undefined;
let z: null = null;

--------------------------------------------------------------------------------
Arrays:
--------------------------------------------------------------------------------
const names: string[] = [];
names.push("Dylan"); // no error
names.push(3); // Error

The readonly keyword can prevent arrays from being changed:
const names: readonly string[] = ["Dylan"];
names.push("Jack"); // Error

TypeScript can infer the type of an array if it has values:
const numbers = [1, 2, 3]; // inferred to type number[]

--------------------------------------------------------------------------------
Tuples:
--------------------------------------------------------------------------------
// define our tuple
let ourTuple: [number, boolean, string];

// initialize correctly
ourTuple = [5, false, 'Coding God was here'];

const ourReadonlyTuple: readonly [number, boolean, string] = [5, true, 'The Real Coding God'];
ourReadonlyTuple.push('Coding God took a day off'); // Error

const graph: [x: number, y: number] = [55.2, 41.3]; //named tuple

const graph: [number, number] = [55.2, 41.3];
const [x, y] = graph; //destructuring tuples

--------------------------------------------------------------------------------
Objects:
--------------------------------------------------------------------------------

const car: { type: string, model: string, year: number } = {
  type: "Toyota",
  model: "Corolla",
  year: 2009
};

//Example with optional property
const car: { type: string, mileage?: number } = { // no error
  type: "Toyota"
};
car.mileage = 2000;

Index signatures can be used for objects without a defined list of properties:

const nameAgeMap: { [index: string]: number } = {};
nameAgeMap.Jack = 25; // no error
nameAgeMap.Mark = "Fifty"; // Error: Type 'string' is not assignable to type 'number'

--------------------------------------------------------------------------------
Enums:
--------------------------------------------------------------------------------

Numeric Enums - Default
By default, enums will initialize the first value to 0 and add 1 to each additional value
You can set the value of the first numeric enum and have it auto increment from that

enum CardinalDirections {
  North = 1,
  East,
  South,
  West
}
let currentDirection = CardinalDirections.North;

String Enums:

enum CardinalDirections {
  North = 'North',
  East = "East",
  South = "South",
  West = "West"
};
// logs "North"
console.log(CardinalDirections.North);

--------------------------------------------------------------------------------

Type Aliases can be used for primitives like string or more complex types such as objects and arrays:

type CarYear = number
type Car = {
  year: CarYear
}
const carYear: CarYear = 2001
const car: Car = {
  year: carYear
};

Interfaces are similar to type aliases, except they only apply to object types:

interface Rectangle {
  height: number,
  width: number
}
const rectangle: Rectangle = {
  height: 20,
  width: 10
};

Interfaces can extend each other's definition:

interface ColoredRectangle extends Rectangle {
  color: string
}
const coloredRectangle: ColoredRectangle = {
  height: 20,
  width: 10,
  color: "red"
};

Union types are used when a value can be more than a single type:

function printStatusCode(code: string | number) {
  console.log(`My status code is ${code}.`)
}

--------------------------------------------------------------------------------
Functions:
--------------------------------------------------------------------------------

// the `: number` here specifies that this function returns a number
function getTime(): number {
  return new Date().getTime();
}
function multiply(a: number, b: number):number {
  return a * b;
}
function printHello(): void {
  console.log('Hello!');
}
// the `?` operator here marks parameter `c` as optional
function add(a: number, b: number, c?: number) {
  return a + b + (c || 0);
}
function pow(value: number, exponent: number = 10) {
  return value ** exponent;
}

Named Parameters
function divide({ dividend, divisor }: { dividend: number, divisor: number }) {
  return dividend / divisor;
}

Rest parameters - type must be an array as rest parameters are always arrays:
function add(a: number, b: number, ...rest: number[]) {
  return a + b + rest.reduce((p, c) => p + c, 0);
}

--------------------------------------------------------------------------------

Type Alias:
type Negate = (value: number) => number;
// in this function, the parameter `value` automatically gets assigned the type `number` from the type `Negate`
const negateFunction: Negate = (value) => value * -1;

Casting:
let x: unknown = 'hello';
console.log((x as string).length);

Using <> works the same as casting with as:
let x: unknown = 'hello';
console.log((<string>x).length);

--------------------------------------------------------------------------------
Classes:
--------------------------------------------------------------------------------

class Person {
  name: string;
}
const person = new Person();
person.name = "Jane";

class Person {
  private name: string;
  public constructor(name: string) {
    this.name = name;
  }
  public getName(): string {
    return this.name;
  }
}
const person = new Person("Jane");

class Person {
  // name is a private member variable
  public constructor(private name: string) {}
  public getName(): string {
    return this.name;
  }
}

class Person {
  private readonly name: string;
  public constructor(name: string) {
    // name cannot be changed after this initial definition, 
    // which has to be either at it's declaration or in the constructor
    this.name = name;
  }
  public getName(): string {
    return this.name;
  }
}

--------------------------------------------------------------------------------
Inheritence:
--------------------------------------------------------------------------------

Implements:

interface Shape {
  getArea: () => number;
}

class Rectangle implements Shape {
  public constructor(protected readonly width: number, protected readonly height: number) {}

  public getArea(): number {
    return this.width * this.height;
  }
}

Extends:

interface Shape {
  getArea: () => number;
}

class Rectangle implements Shape {
  public constructor(protected readonly width: number, protected readonly height: number) {}

  public getArea(): number {
    return this.width * this.height;
  }
}

class Square extends Rectangle {
  public constructor(width: number) {
    super(width, width);
  }
  // getArea gets inherited from Rectangle

  // override: this toString replaces the toString from Rectangle
  public override toString(): string {
    return `Square[width=${this.width}]`;
  }
}


Abstract Classes:

abstract class Polygon {
  public abstract getArea(): number;

  public toString(): string {
    return `Polygon[area=${this.getArea()}]`;
  }
}

class Rectangle extends Polygon {
  public constructor(protected readonly width: number, protected readonly height: number) {
    super();
  }

  public getArea(): number {
    return this.width * this.height;
  }
}


--------------------------------------------------------------------------------
Generics:
--------------------------------------------------------------------------------

function createPair<S, T>(v1: S, v2: T): [S, T] {
  return [v1, v2];
}
console.log(createPair<string, number>('hello', 42)); // ['hello', 42]


Generics can be used to create generalized classes, like Map:

class NamedValue<T> {
  private _value: T | undefined;

  constructor(private name: string) {}

  public setValue(value: T) {
    this._value = value;
  }

  public getValue(): T | undefined {
    return this._value;
  }

  public toString(): string {
    return `${this.name}: ${this._value}`;
  }
}

let value = new NamedValue<number>('myNumber');
value.setValue(10);
console.log(value.toString()); // myNumber: 10


Generics in type aliases allow creating types that are more reusable:

type Wrapped<T> = { value: T };
const wrappedValue: Wrapped<number> = { value: 10 };


Generics can be assigned default values which apply if no other value is specified or inferred:

class NamedValue<T = string> {
  private _value: T | undefined;

  constructor(private name: string) {}

  public setValue(value: T) {
    this._value = value;
  }

  public getValue(): T | undefined {
    return this._value;
  }

  public toString(): string {
    return `${this.name}: ${this._value}`;
  }
}

let value = new NamedValue('myNumber');
value.setValue('myValue');
console.log(value.toString()); // myNumber: myValue


Extends
Constraints can be added to generics to limit what's allowed. The constraints make it possible to 
rely on a more specific type when using the generic type:

function createLoggedPair<S extends string | number, T extends string | number>(v1: S, v2: T): [S, T] {
  console.log(`creating pair: v1='${v1}', v2='${v2}'`);
  return [v1, v2];
}


--------------------------------------------------------------------------------
Utility Types:
--------------------------------------------------------------------------------

Partial changes all the properties in an object to be optional:

interface Point {
  x: number;
  y: number;
}
let pointPart: Partial<Point> = {}; // `Partial` allows x and y to be optional
pointPart.x = 10;


Required changes all the properties in an object to be required:

interface Car {
  make: string;
  model: string;
  mileage?: number;
}

let myCar: Required<Car> = {
  make: 'Ford',
  model: 'Focus',
  mileage: 12000 // `Required` forces mileage to be defined
};


Record is a shortcut to defining an object type with a specific key type and value type:
Record<string, number> is equivalent to { [key: string]: number }

const nameAgeMap: Record<string, number> = {
  'Alice': 21,
  'Bob': 25
};


Omit removes keys from an object type:

interface Person {
  name: string;
  age: number;
  location?: string;
}

const bob: Omit<Person, 'age' | 'location'> = {
  name: 'Bob'
  // `Omit` has removed age and location from the type and they can't be defined here
};


Pick removes all but the specified keys from an object type"

interface Person {
  name: string;
  age: number;
  location?: string;
}

const bob: Pick<Person, 'name'> = {
  name: 'Bob'
  // `Pick` has only kept name, so age and location were removed from the type and they can't be defined here
};


Exclude removes types from a union:

type Primitive = string | number | boolean
const value: Exclude<Primitive, string> = true; // a string cannot be used here since Exclude removed it from the type.


ReturnType extracts the return type of a function type:

type PointGenerator = () => { x: number; y: number; };
const point: ReturnType<PointGenerator> = {
  x: 10,
  y: 20
};


Parameters extracts the parameter types of a function type as an array:

type PointPrinter = (p: { x: number; y: number; }) => void;
const point: Parameters<PointPrinter>[0] = {
  x: 10,
  y: 20
};


Readonly is used to create a new type where all properties are readonly, meaning they cannot be 
modified once assigned a value. Keep in mind TypeScript will prevent this at compile time, 
but in theory since it is compiled down to JavaScript you can still override a readonly property.

interface Person {
  name: string;
  age: number;
}
const person: Readonly<Person> = {
  name: "Dylan",
  age: 35,
};
person.name = 'Gokhan'; // prog.ts(11,8): error TS2540: Cannot assign to 'name' because it is a read-only property


--------------------------------------------------------------------------------
keyof:
--------------------------------------------------------------------------------

keyof is a keyword in TypeScript which is used to extract the key type from an object type.

keyof with explicit keys
When used on an object type with explicit keys, keyof creates a union type with those keys:

interface Person {
  name: string;
  age: number;
}
// `keyof Person` here creates a union type of "name" and "age", other strings will not be allowed
function printPersonProperty(person: Person, property: keyof Person) {
  console.log(`Printing person property ${property}: "${person[property]}"`);
}
let person = {
  name: "Max",
  age: 27
};
printPersonProperty(person, "name"); // Printing person property name: "Max"


keyof with index signatures
keyof can also be used with index signatures to extract the index type:

type StringMap = { [key: string]: unknown };
// `keyof StringMap` resolves to `string` here
function createStringPair(property: keyof StringMap, value: string): StringMap {
  return { [property]: value };
}


--------------------------------------------------------------------------------
Null & Undefined:
--------------------------------------------------------------------------------

By default null and undefined handling is disabled, and can be enabled by setting strictNullChecks to true

null and undefined are primitive types and can be used like other types, such as string:

let value: string | undefined | null = null;
value = 'hello';
value = undefined;

When strictNullChecks is enabled, TypeScript requires values to be set unless undefined is explicitly added to the type.


Optional Chaining
This is a JavaScript feature that works well with TypeScript's null handling. It allows accessing properties on an 
object, that may or may not exist, with a compact syntax. It can be used with the ?. operator when accessing properties:

interface House {
  sqft: number;
  yard?: {
    sqft: number;
  };
}
function printYardSize(house: House) {
  const yardSize = house.yard?.sqft;
  if (yardSize === undefined) {
    console.log('No yard');
  } else {
    console.log(`Yard is ${yardSize} sqft`);
  }
}

let home: House = {
  sqft: 500
};

printYardSize(home); // Prints 'No yard'


Nullish Coalescence
This is another JavaScript feature that also works well with TypeScript's null handling. It allows writing 
expressions that have a fallback specifically when dealing with null or undefined. This is useful when other 
falsy values can occur in the expression but are still valid. It can be used with the ?? operator in an expression, 
similar to using the && operator:

function printMileage(mileage: number | null | undefined) {
  console.log(`Mileage: ${mileage ?? 'Not Available'}`);
}
printMileage(null); // Prints 'Mileage: Not Available'
printMileage(0); // Prints 'Mileage: 0'


Null Assertion
TypeScript's inference system isn't perfect, there are times when it makes sense to ignore a value's possibility
of being null or undefined. An easy way to do this is to use casting, but TypeScript also provides the ! operator 
as a convenient shortcut:

function getValue(): string | undefined {
  return 'hello';
}
let value = getValue();
console.log('value length: ' + value!.length);


Array bounds handling
Even with strictNullChecks enabled, by default TypeScript will assume array access will never return undefined 
(unless undefined is part of the array type)

The config noUncheckedIndexedAccess can be used to change this behavior:

let array: number[] = [1, 2, 3];
let value = array[0]; // with `noUncheckedIndexedAccess` this has the type `number | undefined`


--------------------------------------------------------------------------------
Using non-typed NPM packages in TypeScript
--------------------------------------------------------------------------------

Using untyped NPM packages with TypeScript will not be type safe due to lack of types.
To help TypeScript developers use such packages, there is a community maintained project called Definitely Typed:
http://definitelytyped.org/

Definitely Typed is a project that provides a central repository of TypeScript definitions for NPM packages 
which do not have types.

Example:
npm install --save-dev @types/jquery

No other steps are usually needed to use the types after installing the declaration package, TypeScript will 
automatically pick up the types when using the package itself


--------------------------------------------------------------------------------
Updates - ver 5+
--------------------------------------------------------------------------------

Template Literal Types
Template Literal Types now allows us to create more precise types using template literals. 
We can define custom types that depend on the actual values of strings at compile time:

type Color = "red" | "green" | "blue";
type HexColor<T extends Color> = `#${string}`;

// Usage:
let myColor: HexColor<"blue"> = "#0000FF";


Index Signature Labels
Index Signature Labels allows us to label index signatures using computed property names. 
It helps in providing more descriptive type information when working with dynamic objects:

type DynamicObject = { [key: string as `dynamic_${string}`]: string };

// Usage:
let obj: DynamicObject = { dynamic_key: "value" };


*/