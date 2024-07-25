const moviesList = document.querySelector('#list_movies');
const URL = 'https://swapi-api.hbtn.io/api/films/?format=json';
fetch(URL)
    .then(response => response.json())
    .then(function(data){
        const movies = data.results;
              movies.forEach((movie)=>{
                const movieTitle = movie.title;
                const listItem = document.createElement("li");
                listItem.textContent = movieTitle
                moviesList.appendChild(listItem);
            })})
    .catch(error => console.error(error));
