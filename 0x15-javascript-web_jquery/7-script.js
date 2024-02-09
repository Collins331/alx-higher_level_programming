$.get('https://swapi-api.alx-tools.com/api/people/5/?format=json', (data, textResponse) => {
  $('#character').text(data.name);
});
