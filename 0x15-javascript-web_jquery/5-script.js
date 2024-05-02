$('#add_item').click(function() {
    let newItem = $('<li>Item</li>');
    $('ul.my_list').append(newItem);
});
