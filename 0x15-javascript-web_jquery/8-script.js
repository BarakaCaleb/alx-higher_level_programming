$.getJSON('https://swapi-api.alx-tools.com/api/films/?format=json', function(data) {
    $.each(data.results, function(index, movie) {
        let movieTitle = movie.title;
        let listItem = $('<li>').text(movieTitle);
        $('#list_movies').append(listItem);
    });
});