var mongoose = require('mongoose');

var mongoDB = 'mongodb://127.0.0.1/DAW2020';

mongoose.connect(mongoDB, {userNewUrlParser: true, useUnifiedTopology: true});

var db = mongoose.connection;

db.on('error', console.error.bind(console, 'Mongodb connection error'));

db.once('open', function() {
    console.log("Succesfully connection!");
})

var studentSchema = new mongoose.Schema({
    numero: String,
    nome: String,
    git: String,
    tpc: [Number]
});

// colocar no singular pq ele transforma em plural e transforma
var studentModel = mongoose.model('student', studentSchema)

var data = [
    {
        numero: "A34900",
        nome: "Cecília Soares"
    },
    {
        numero: "PG42844",
        nome: "Maria Barbosa"
    }
]

studentModel.create(data)

console.log("Inserido!!");