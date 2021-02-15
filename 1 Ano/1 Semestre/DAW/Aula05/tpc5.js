var http = require('http');
const axios = require('axios');

http.createServer(function (req, res) {
    console.log(req.method +  " " + req.url);

    if (req.method == 'GET') {
        if (req.url == '/') {
            res.writeHead(200, {'Content-Type': 'text/html; charset=utf8'});
            res.write('<h2>Escola de Música</h2>');
            res.write('<ul>');
            res.write('<li><a href="/alunos">Lista de Alunos</a></li>');
            res.write('<li><a href="/cursos">Lista de Cursos</a></li>');
            res.write('<li><a href="/instrumentos">Lista de Instrumentos</a></li>');
            res.write('</ul>');
            res.end(); 
        }
        else if (req.url == '/alunos') {
            axios.get('http://localhost:3001/alunos')
                .then(resp => {
                    alunos = resp.data;

                    res.writeHead(200, {'Content-Type': 'text/html; charset=utf8'});
                    res.write('<h2>Escola de Música: Lista de Alunos</h2>');
                    res.write('<ul>');

                    alunos.forEach(element => {
                        res.write('<li>' + element.id + '-' + element.nome + '</li>');
                    });

                    res.write('</ul>');
                    res.write('<address>[<a href="/">Voltar</a>]</address>');
                    res.end();
                })
                .catch(function (error) {
                    console.log('Erro na obtenção na lista de alunos: ' + error);
                })
        }
        else if (req.url == 'cursos') {

        }
        else if (req.url == 'instrumentos') {

        }
        else {
            res.writeHead(200, {'Content-Type': 'text/html'});
            res.write("<p>Pedido não suportado:" + req.method + " " + req.url + " </p>");
            res.end(); 
        }
    }
    else {
        res.writeHead(200, {'Content-Type': 'text/html'});
        res.write("<p>Pedido não suportado:" + req.method + " " + req.url + " </p>");
        res.end(); 
    }

}).listen(4000);

console.log('Servidor na porta 4000...');