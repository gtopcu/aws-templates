
async function init() {
	console.log(1);
	await sleep(3000);
	console.log(2);
}

function sleep(ms) {
	return new Promise((resolve) => {
		setTimeout(resolve, ms);
	});
}

init();
console.log("Done!");
