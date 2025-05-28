// npm init -y
// npm install express
// npm install --save-dev nodemon // Optional- for auto-restart during development

// node server.js
// nodemon server.js

// # Run with node (production)
// npm start

// # Or run with nodemon (development - auto-restart)
// npm run dev

// curl "http://localhost:3000/users/123?name=john&age=25"

// curl -X POST http://localhost:3000/users \
//   -H "Content-Type: application/json" \
//   -d '{"name": "John Doe", "email": "john@example.com"}'

//const express = require('express');
import express, { json } from 'express';
const app = express();
const PORT = 5000;

app.use(express.json());

// GET route with path and query parameters
app.get('/users/:id', (req, res) => {
    console.log('=== GET Request ===');
    console.log('Content-Type:', req.get('Content-Type'));
    console.log('Path Parameters:', req.params);
    console.log('Query Parameters:', req.query);
    console.log('URL:', req.originalUrl);
    
    res.json({
        message: 'GET request received',
        pathParams: req.params,
        queryParams: req.query
    });
});

// POST route - accepts JSON body
app.post('/users', (req, res) => {
    console.log('=== POST Request ===');
    console.log('Content-Type:', req.get('Content-Type'));
    console.log('Path Parameters:', req.params);
    console.log('Request Body:', req.body);
    
    res.json({
        message: 'POST request received',
        pathParams: req.params,
        receivedData: req.body
    });
});

// PUT route - accepts JSON body
app.put('/users/:id', (req, res) => {
    console.log('=== PUT Request ===');
    console.log('Content-Type:', req.get('Content-Type'));
    console.log('Path Parameters:', req.params);
    console.log('Request Body:', req.body);
    
    res.json({
        message: 'PUT request received',
        pathParams: req.params,
        receivedData: req.body
    });
});

// PATCH route - accepts JSON body
app.patch('/users/:id', (req, res) => {
    console.log('=== PATCH Request ===');
    console.log('Content-Type:', req.get('Content-Type'));
    console.log('Path Parameters:', req.params);
    console.log('Request Body:', req.body);
    
    res.json({
        message: 'PATCH request received',
        pathParams: req.params,
        receivedData: req.body
    });
});

// DELETE route
app.delete('/users/:id', (req, res) => {
    console.log('=== DELETE Request ===');
    console.log('Content-Type:', req.get('Content-Type'));
    console.log('Path Parameters:', req.params);
    console.log('Query Parameters:', req.query);
    
    res.json({
        message: 'DELETE request received',
        pathParams: req.params,
        queryParams: req.query
    });
});

// Root route
app.get('/', (req, res) => {
    res.json({
        message: 'Simple REST API is running!',
        endpoints: {
            'GET /users/:id': 'Get user with path and query params',
            'POST /users': 'Create user with JSON body',
            'PUT /users/:id': 'Update user with JSON body',
            'PATCH /users/:id': 'Partially update user with JSON body',
            'DELETE /users/:id': 'Delete user'
        }
    });
});

// Start the server
app.listen(PORT, () => {
    console.log(`Server is running on http://localhost:${PORT}`);
    console.log('Press Ctrl+C to stop the server');
});