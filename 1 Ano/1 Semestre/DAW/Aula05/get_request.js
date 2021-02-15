const axios = require('axios');

axios.get('http://localhost:3000/pubs?_sort=year,title&order=desc,asc')
    .then(resp => {
        data = resp.data;
        data.forEach(element => {
            console.log(`${element.year}, ${element.id}, ${element.title}`);
        });
    })
    .catch(function (error) {
        console.log(error);
    })
    