//API Key: 1c99702e78eef87053c045ba97358dbd

$(document).ready(function(){
    //console.log("jQuery loaded!")
    var baseURL = `https://api.openweathermap.org/data/2.5/weather`;
    var appId = "1c99702e78eef87053c045ba97358dbd";

    $(document).on('click', '#getDataButton', function(){
        var cityName = $('input[id=' + "inputCity" + ']').val();
        $.getJSON(`${baseURL}?q=${cityName}&appid=${appId}&units=imperial`, function(result){
            console.log(result);
            console.log(result.name);
            var contentHtml =   `
                            <p>
                                <h2>${result.name}</h2>
                                <br />
                                <h4>Temperature: ${result.main.temp}</h4>
                            </p>
                            `;

            $('#content').html(contentHtml);
        });
    });
});

