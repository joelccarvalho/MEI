var http = require('http');
var aux = require('./mymod.js');
var fs = require('fs');

http.createServer(function (req, res) {
    console.log(req.method +  " " + req.url +  " " + aux.myDateTime());

    if (req.url.match(/\/[1-3]$/)) {
        var num = req.url.split('/')[req.url.length-1];

        fs.readFile('pagina' + num + '.html', function(err, data) {
            res.writeHead(200, {'Content-Type': 'text/html; charset=utf-8'});
            res.write(data);
            res.end(); 
        });
    }
    else {
        res.writeHead(200, {'Content-Type': 'text/html; charset=utf-8'});
        res.write("O URL não corresponde ao esperado.");
        res.end(); 
    }

}).listen(7777);

console.log('Servidor na porta 7777...');