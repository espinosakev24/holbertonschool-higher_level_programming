const url = 'https://swapi.co/api/people/5/?format=json';
jQuery.getJSON(url, function(data) {
    console.log(data);
    console.log(data.name, data.hair_color);
    $('header').text(data.name);
});