$(document).ready(function(){
    // .click
    $('h1').click(function(){
        alert('jQuery Setup correctly!');
    });

    // .hide
    $('#buttonShowHide').click(function(){
        $('.hideMe').hide();
    });

    // .show
    $('#buttonShow').click(function(){
        $('.starthidden').show();
    });
    
    // .toggle
    $('#buttonToggleCat').click(function(){
        $('#toggleImage').toggle();
    });

    // .slideDown
    $('#buttonSlideDown').click(function(){
        $('#slidingImage').slideDown("slow");
    });

    // .slideUp
    $('#buttonSlideUp').click(function(){
        $('#slidingImage').slideUp("slow");
    });

    // .slideToggle
    $('#buttonSlideToggle').click(function(){
        $('#slidingImage').slideToggle("slow");
    });

    // .fadeIn
    $('#buttonFadeIn').click(function(){
        $('#fadingImage').fadeIn("slow");
    });

    // .fadeout
    $('#buttonFadeOut').click(function(){
        $('#fadingImage').fadeOut("slow");
    });

    // .addClass
    $('#buttonAddClassRed').click(function(){
        $('p').addClass("redText");
    });

    //look at this code to understand that we have switched the positions of the before and after blocks in code here
    $('#simplePara').before($('before'));
    $('#simplePara').after($("after"));
    
    $('#appendToSimplePara').click(function(){
        $('#simplePara').append('<p>This is some appended text!</p>');
    });

    // .html
    $('#replaceHTML').click(function(){
        $('#simplePara').html('<p>Complicated Para!! - Replacing simple para!</p>');
    });

    //.attr
    $('#buttonAttr').click(function(){
        $('button').addClass($('p').attr('class'));
    });

    //demonstrates .val and .text
    $( "input" )
    .keyup(function() {
      var value = $( this ).val();
      $( "#someValue" ).text( value );
    })
    .keyup();

    //demonstrates .data
    $( "div" ).data( "test", { first: 16, last: "pizza!" } );
    $( "span:first" ).text( $( "div" ).data( "test" ).first );
    $( "span:last" ).text( $( "div" ).data( "test" ).last );
});