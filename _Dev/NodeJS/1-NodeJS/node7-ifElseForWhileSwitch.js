
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

exports.handler = async function(event) {
    console.log('Request event: ', event);
    let response;
    switch(true) {
      case event.httpMethod === 'GET' && event.path === healthPath:
        response = buildResponse(200);
        break;
      case event.httpMethod === 'GET' && event.path === productPath:
        response = await getProduct(event.queryStringParameters.productId);
        break;
      case event.httpMethod === 'GET' && event.path === productsPath:
        response = await getProducts();
        break;
      case event.httpMethod === 'POST' && event.path === productPath:
        response = await saveProduct(JSON.parse(event.body));
        break;
      case event.httpMethod === 'PATCH' && event.path === productPath:
        const requestBody = JSON.parse(event.body);
        response = await modifyProduct(requestBody.productId, requestBody.updateKey, requestBody.updateValue);
        break;
      case event.httpMethod === 'DELETE' && event.path === productPath:
        response = await deleteProduct(JSON.parse(event.body).productId);
        break;
      default:
        response = buildResponse(404, '404 Not Found');
    }
    return response;
  }