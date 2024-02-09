$.ajax({
  url: 'https://hellosalut.stefanbohacek.dev/?lang=fr',
  type: 'GET',
  dataType: 'json',
  success: (data) => {
    $('#hello').text(data.hello);
  }
});
