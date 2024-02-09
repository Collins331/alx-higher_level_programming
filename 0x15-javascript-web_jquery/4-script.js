$('#toggle_header').on('click', () => {
  if ($('header').hasClass('green')) {
    $('header').removeClass('green').addClass('red');
  } else if ($('header').hasClass('red')) {
    $('header').removeClass('red').addClass('green');
  } else {
    $('header').addClass('green');
  }
});
