$(document).ready(function () {
  $('INPUT#btn_translate').click(fetchTranslation);
  $('INPUT#language_code').keyup(function (event) {
    if (event.keyCode === 13) {
      fetchTranslation();
    }
  });

  function fetchTranslation () {
    const languageCode = $('INPUT#language_code').val();
    $.getJSON(
        `https://fourtonfish.com/hellosalut/hello/?lang=${languageCode}`,
        function (data) {
          $('#hello').text(data.hello);
        }
    );
  }
});
