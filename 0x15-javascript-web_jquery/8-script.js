$.ajax({
  url: 'https://swapi-api.alx-tools.com/api/films/?format=json',
  type: 'GET',
  dataType: 'json',
  success: function (data) {
    const movies = data.results;
    const list = $('#list_movies');
    $.each(movies, (index, movie) => {
      list.append('<li>' + movie.title + '</li>');
    });
  }
});
