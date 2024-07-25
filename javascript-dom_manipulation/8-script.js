const URL = "https://hellosalut.stefanbohacek.dev/?lang=fr";

fetch(URL)
    .then(response => response.json())
    .then(function(data){
        hello.textContent = data.hello;
    })
    .catch(error => console.error(error));
