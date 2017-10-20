$(document).ready(function(){
    // console.log('jQuery loaded!');

    $('img').click(function() {
        console.log('data-alt-src value is', $(this).attr('data-alt-src'));
        $(this).attr('src', $(this).attr('data-alt-src'));
    });
});