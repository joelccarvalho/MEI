var express = require('express')
var bodyParser = require('body-parser')
var app = express()

app.use(bodyParser.urlencoded({extended: false}))

app.use(bodyParser.json())

app.use(function (req, res, next) {
    console.log(JSON.stringify(req.body))
    next()
})

app.get('*', function (req, res) {
    if (req.body)
        res.send('Recebi um Get com informação:' + JSON.stringify(req.body))
    else
        res.send('Recebi um Get...')
})

app.post('*', function (req, res) {
    res.send('Recebi um Post ' + JSON.stringify(req.body))
})

app.listen(7700, () => console.log('Servidor na porta 7700..'))