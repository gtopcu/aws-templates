
const express = require('express')
const router = express.Router();

const Customer = require('../models/Customer');

//GET /customer by query param name or get all customers if no query specified
//localhost:8080/customer?name=Alex
router.get('/', async (req, resp) => {
    console.log(req.query.name);
    //console.log(req.headers);
    try {
        if(req.query.name == undefined) {
            const customers = await Customer.find().limit(20);
            resp.status(200).json(customers);
        }
        else {
            const customers = await Customer.find({name: req.query.name}).limit(20);
            resp.status(200).json(customers);
        }
    } catch (err) {
        //resp.send("Error: " + err);  
        resp.status(500).json({ message: err });  
    }
    //resp.send("GET customer:" + req.query.id);
});

//GET customer by _id
//localhost:8080/61e48fd5fa141c40b3be09ba
router.get('/:id', async (req, resp) => {
    try {
        const customers = await Customer.findById(req.params.id);
        resp.status(200).json(customers);
    } catch (err) {
        //resp.send("Error: " + err);  
        resp.status(500).json({ message: err });  
    }
    //resp.send("GET customer:" + req.query.id);
});

//DELETE customer by _id
router.delete('/:id', async (req, resp) => {
    try {
        const removedCustomer = await Customer.remove({ _id : req.params.id });
        resp.status(200).json(removedCustomer);
    } catch (err) {
        //resp.send("Error: " + err);  
        resp.status(500).json({ message: err });  
    }
});

//PATCH customer by _id
router.patch('/:id', async (req, resp) => {
    try {
        const updatedCustomer = await Customer.updateOne(
            { _id : req.params.id },
            { $set: { name : req.body.name } }
        );
        resp.status(200).json(updatedCustomer);
    } catch (err) {
        //resp.send("Error: " + err);  
        resp.status(500).json({ message: err });  
    }
});

//POST /customer
//Needs body-parser to be installed
//localhost:8080/customer
/*
{
    "name": "Alex",
    "age": 21
}
*/
router.post('/', async (req, resp) => {
    console.log(req.body);
    const customer = new Customer({
        name : req.body.name,
        age : req.body.age
    });
    try {
        const savedCustomer = await customer.save();
        resp.status(200).json(savedCustomer);
    } catch (err) {
        resp.status(500).json({ err_message: err });  
    }
    //resp.send(req.body);
});

//GET /customer/address
router.get('/address', (req, resp) => {
    console.log(req.query);
    console.log(req.headers);
    resp.send("GET customer address:" + req.query.id);
});

module.exports = router;