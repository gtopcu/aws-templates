/*
    https://www.youtube.com/watch?v=vjf774RKrLc
    npm init
    npm install nodemon
    npm install express
    npm install mongoose
    npm install dotenv
    npm install body-parser
    npm install cors
    
    npm start/stop
*/

require('dotenv/config')
const mongoose = require('mongoose')
mongoose.connect(process.env.DB_CONNECTION, () => console.log("Connected to Mongo!"))

const express = require('express');
const app = express();

//Middleware/hook -> Can check auth i.e. JWT, or route to sub routes
//app.use(auth);
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

//Routes
app.get('/', (req, resp) => {
        resp.send("Home Dir");
    }
);
/*
router.get('/customer', (req, resp) => {
    resp.send("Get customers");
});
*/

//Start
app.listen(8080);

console.log("Running!");

