$(document).ready(function() {
    $.getJSON('https://hellosalut.stefanbohacek.dev/?lang=fr', function(data) {
        let helloTranslation = data.hello;
        $('#hello').text(helloTranslation);
    });
});
