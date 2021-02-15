const axios = require('axios');

axios.post('http://localhost:3000/pubs', {
    "id": "DAW2020",
    "title": "Aula05",
    "year": "2020"
})
.then(resp => {
    console.log(resp.data);
})
.catch(function (error) {
    console.log('Error' + error);
})