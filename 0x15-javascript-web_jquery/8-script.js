const url = 'https://swapi.co/api/films/?format=json'
jQuery.getJSON(url, function(data) {
    data.results.forEach(element => {
        console.log(element.title);
        $('UL#list_movies').append(`<li>${element.title}</li>`);
    });;
});