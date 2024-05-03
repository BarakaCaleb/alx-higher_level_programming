$(document).ready(function() {
    $('#btn_translate').click(translateHello);
    $('#language_code').keypress(function(event) {
        if (event.which === 13) {
            translateHello();
        }
    });

    function translateHello() {
        var languageCode = $('#language_code').val();
        $.getJSON('https://www.fourtonfish.com/hellosalut/hello/', { lang: languageCode })
            .done(function(data) {
                $('#hello').text(data.hello);
            })
            .fail(function(jqXHR, textStatus, errorThrown) {
                console.log('Error:', errorThrown);
            });
    }
});