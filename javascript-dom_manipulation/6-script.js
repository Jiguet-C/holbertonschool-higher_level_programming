let character = document.querySelector('#character');
const URL = 'https://swapi-api.hbtn.io/api/people/5/?format=json';
fetch(URL)
    .then(response => response.json())
    .then(function(data){
        const char = data.name;
        character.textContent = char;
    })
    .catch(error => console.error(error));
