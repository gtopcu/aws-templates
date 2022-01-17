
//https://mongoosejs.com/docs/guide.html
//https://www.youtube.com/watch?v=pKd0Rpw7O48
//Can also use the joi package - has better validation

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