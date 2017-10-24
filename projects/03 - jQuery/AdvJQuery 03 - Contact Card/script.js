$(document).ready(function(){
    console.log("jQuery loaded");

    $('#addUserForm').on('submit', function(){
        var firstname = $('input[name=firstName]').val();
        var lastname = $('input[name=lastName]').val();
        var email = $('input[name=email]').val();
        var phoneNumber = $('input[name=phoneNumber]').val();
        var description = $('textarea[name=description]').val();

        htmlforContact =    "<div class='contactCard'>" + "First Name: " + firstname + "<br><br>" +
                            "Last Name: " + lastname + "<br><br>" +
                            "Email: " + email + "<br><br>" +
                            "Phone Number: " + phoneNumber + "<br><br>" +
                            "<p hidden class='hiddenDescription'>" + description + "</p>"
                            "</div>";

        console.log(htmlforContact);

        $('.contactCards').append(htmlforContact);

        return false;
    });


    $(document).on('click', '.contactCard', function(){
        event.stopPropagation();
        //console.log($(this).find('p').text);
        var desc = $(this).find('p').text();
        console.log(desc);
        $(this).html("<p class='contactDescription'>" + desc + "</p>");
    });

    // $('.contactCards').on('Click', function(){
    //     $(this).html("description!");
    // });
});
