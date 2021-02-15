var http = require('http');
var aux = require('./mymod.js');
var url = require('url');

http.createServer(function (req, res) {
    console.log(req.method +  " " + req.url +  " " + aux.myDateTime());
    var parsed = url.parse(req.url, true);
    var parsed2 = url.parse(req.url, false);

    res.writeHead(200, {'Content-Type': 'text/html; charset=utf-8'});
    res.write("<p>Hoje: " + aux.myDateTime() + "</p>");
    res.write("<pre> True:" + JSON.stringify(parsed.query) +"</pre>"); // Testar http://localhost:7777/as=1?a=1&b=2
    res.write("<pre> False:" + JSON.stringify(parsed2.query) +"</pre>"); // Testar http://localhost:7777/as=1?a=1&b=2

    var sum = parseInt(parsed.query.a) + parseInt(parsed.query.b);
    res.write('Resultado: ' + parsed.query.a + "+" + parsed.query.b + "=" + sum);
    res.end(); //res.end('Olá ' + aux.turma);
}).listen(7777);

console.log('Servidor na porta 7777...');