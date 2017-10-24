$(document).ready(function(){
    // console.log("jQuery loaded");

    //this prevents the form from going elsewhere
    $('#userForm').submit(function(){
        var firstname = $('#userForm').find('input[name=firstname]').val();
        var lastname = $('input[name=lastname]').val();
        var email = $('input[name=email]').val();
        var phoneNumber = $('input[name=phoneNumber]').val();
        var tableRowHtml =  "<tr>" + 
                                "<td>" +
                                firstname +
                                "</td>" + 
                                "<td>" +
                                lastname +
                                "</td>" + 
                                "<td>" +
                                email +
                                "</td>" + 
                                "<td>" +
                                phoneNumber +
                                "</td>" + 
                            "</tr>";
        // console.log(tableRowHtml);
        $('table').append(tableRowHtml);

        return false;
    });
    
});
