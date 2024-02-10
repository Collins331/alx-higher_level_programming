$('#btn_translate').on('click', () => {
  const langCode = $('#language_code').val();
  $.ajax({
    url: `https://www.fourtonfish.com/hellosalut/hello/?lang=${langCode}`,
    type: 'GET',
    dataType: 'json',
    success: function (data) {
      $('#hello').text(data.hello);
    },
    error: () => {
      $('#hello').text('Translation not Found');
    }
  });
});
