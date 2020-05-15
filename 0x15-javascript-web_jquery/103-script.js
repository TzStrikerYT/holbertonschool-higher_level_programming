window.onload = function () {
  $('INPUT#btn_translate').click(function () {
    const lang = $('INPUT#language_code').val();
    const url = 'https://fourtonfish.com/hellosalut/?lang=' + lang;
    $.get(url, function (data) {
      $('DIV#hello').text(data.hello);
    });
  });

  $('INPUT#language_code').keypress(function (event) {
    const key = (event.keyCode ? event.keyCode : event.which);
    if (key === 13) {
      const lang = $('INPUT#language_code').val();
      const url = 'https://fourtonfish.com/hellosalut/?lang=' + lang;
      $.get(url, function (data) {
        $('DIV#hello').text(data.hello);
      });
    }
  });
};
