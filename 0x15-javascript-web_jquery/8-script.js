const url = 'https://swapi-api.hbtn.io/api/films/?format=json';
$.get(url, function (data) {
  for (const result of data.results) {
    $('UL#list_movies').append('<li>' + result.title + '</li>');
  }
});
