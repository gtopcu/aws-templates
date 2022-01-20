/*
    https://www.youtube.com/watch?v=vjf774RKrLc
    https://www.youtube.com/watch?v=pKd0Rpw7O48
    https://mongoosejs.com/
    
    npm init
    npm install nodemon
    npm install express
    npm install mongoose
    npm install dotenv
    npm install body-parser
    npm install cors

    npm build 
    
    npm start/stop

    https://editor.swagger.io/
    https://www.npmjs.com/package/swagger-ui
    https://www.npmjs.com/package/swagger-jsdoc
    https://www.npmjs.com/package/swagger-ui-express
    npm i swagger-ui
    npm i swagger-jsdoc
    npm i swagger-ui-express
*/

require('dotenv/config') //Sets environment vars from .env file

const mongoose = require('mongoose')
mongoose.connect(process.env.DB_CONNECTION, () => console.log("Connected to Mongo!"))

const express = require('express');
const app = express();

//------------------------------------------------------------------------------------
//Middleware/hook -> Can check auth i.e. JWT, or route to sub routes
//app.use(auth);
//------------------------------------------------------------------------------------

const cors = require('cors');
app.use(cors());

const bodyParser = require('body-parser');
app.use(bodyParser.json());

/*
app.use('/customers', () => {
        console.log("Customers hook");
    }
);
*/

const customersRoute = require('./routes/customer');
app.use('/customer', customersRoute);

//------------------------------------------------------------------------------------
//Routes
//------------------------------------------------------------------------------------
app.get('/', (req, resp) => {
        resp.send("Home Dir");
    }
);


//Swagger - Auto-generating OpenAPI 3.0 doc example
/**
 * @openapi
 * /:
 *   get:
 *     description: Welcome to swagger-jsdoc!
 *     responses:
 *       200:
 *         description: Returns a mysterious string.
 */
app.get('/api', (req, resp) => {
        resp.send("Swagger enabled API!");
    }
);

//Swagger sample - jsDoc creates OpenAPI 3.0 spec
//import swaggerJsdoc from 'swagger-jsdoc';
const swaggerJsdoc = require('swagger-jsdoc');

async function surveSwaggerSpecification(req, res) {
  // Swagger definition
  // You can set every attribute except paths and swagger
  // https://github.com/swagger-api/swagger-spec/blob/master/versions/2.0.md
  const swaggerDefinition = {
    info: {
      // API informations (required)
      title: 'Hello World', // Title (required)
      version: '1.0.0', // Version (required)
      description: 'A sample API', // Description (optional)
    },
    //host: `localhost:${PORT}`, // Host (optional)
    basePath: '/', // Base path (optional)
  };
  // Options for the swagger docs
  const options = {
    // Import swaggerDefinitions
    swaggerDefinition,
    // Path to the API docs
    // Note that this path is relative to the current directory from which the Node.js is ran, not the application itself.
    //apis: [`${__dirname}/routes*.js`, `${__dirname}/parameters.yaml`],
    apis: [`${__dirname}/app.js`, ],
  };
  const swaggerSpec = await swaggerJsdoc(options);

  // And here we go, we serve it.
  res.setHeader('Content-Type', 'application/json');
  res.send(swaggerSpec);
}
app.get('/api-docs.json', surveSwaggerSpecification);

/*
//Serve using express
//https://www.npmjs.com/package/swagger-ui-express
const swaggerUi = require('swagger-ui-express');
const swaggerDocument = require('./swagger.json');
app.use('/api-docs', swaggerUi.serve, swaggerUi.setup(swaggerDocument));
*/


/*
router.get('/customer', (req, resp) => {
    resp.send("Get customers");
});
*/

//Start
const port = process.env.PORT || 8080;
app.listen(port, () => console.log("Running on port: " + port));

//console.log("Running!");

