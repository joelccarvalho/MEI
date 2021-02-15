const axios = require('axios');

axios.get('http://localhost:3001/cursos')
    .then(resp => {
        var cursos = resp.data;

        for (let i = 0; i < cursos.length; i++) {
            axios.post('http://localhost:3000/pubs', {
                "id": cursos[i].id,
                "title": cursos[i].designacao,
                "year": "2020"
            })
            .then(r => {
                console.log("Inseri o registo:" + r.data.id);
            })
            .catch(function (er) {
                console.log('Erro no POST' + er);
            })
        }
    })
    .catch(function (error) {
        console.log('Erro no GET' + error);
    })