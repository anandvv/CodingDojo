$(document).ready(function(){
    console.log("jQuery loaded");

    var prevSrc, prevAltSrc;

    $('img').hover(function(){
        prevSrc = $(this).attr('src');
        prevAltSrc = $(this).attr('data-alt-src');
        $(this).attr('src', $(this).attr('data-alt-src'));
    }, function(){
        $(this).attr('src', prevSrc);
        $(this).attr('data-alt-src', prevAltSrc);
    });
});
