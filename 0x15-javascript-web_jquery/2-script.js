document.querySelector('head').style.color = '#FF0000';

$('#red_header').click(function() {
    $('header').css('color', '#FF0000'); //Update the color of the <header> element using jQuery
})