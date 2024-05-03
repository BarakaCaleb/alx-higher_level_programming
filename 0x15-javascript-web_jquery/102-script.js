$(document).ready(function() {
    $('#btn_translate').click(function() {
        var languageCode = $('#language_code').val();
        $.getJSON('https://www.fourtonfish.com/hellosalut/hello/', { lang: languageCode })
            .done(function(data) {
                $('#hello').text(data.hello);
            })
            .fail(function(jqXHR, textStatus, errorThrown) {
                console.log('Error:', errorThrown);
            });
    });
});