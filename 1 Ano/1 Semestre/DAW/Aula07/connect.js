var mongoose = require('mongoose');

var mongoDB = 'mongodb://127.0.0.1/DAW2020';

mongoose.connect(mongoDB, {userNewUrlParser: true, useUnifiedTopology: true});

var db = mongoose.connection;

db.on('error', console.error.bind(console, 'Mongodb connection error'));

db.once('open', function() {
    console.log("Succesfully connection!");
})