
const mongoose = require('mongoose');

const CustomerSchema = mongoose.Schema({

    name: {
        type: String,
        required: true
    },
    
    age: Number,

    registerDate: {
        type: Date,
        default: Date.now
    }

});

module.exports = mongoose.model('Customer', CustomerSchema);