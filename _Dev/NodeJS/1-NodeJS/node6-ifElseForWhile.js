
const array = [1, 2, 3];

for (let index = 0; index < array.length; index++) {
    const element = array[index];
    console.log("For: " + element)
}

array.forEach(element => {
    console.log("ForEach: " + element)
});

if (1 in array) {
    console.log("in array");
} else {
    console.log("not in array");
}

var i = 2;
while (i > 0) {
    console.log("while: %d", i)
    i--;
}

