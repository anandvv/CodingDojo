$(document).ready(function(){
    console.log('jQuery loaded');
    // var pokemonSprites;
    var baseURL = "https://pokeapi.co/api/v2/pokemon/";
    $.getJSON(`${baseURL}?limit=16`, function(result){
        pokemonSprites = new Array(result.results.length);
        result.results.forEach(function(element) {
            $.getJSON(element.url, function(pokemonInfo){
                // pokemonSprites.push(pokemonInfo.sprites["front_default"]);
                $("#wrapper").append(   `<div id=${pokemonInfo.id} class="pokemon">
                                            <img src=${pokemonInfo.sprites["front_default"]} />
                                         </div>
                                        `);
            });
        }, this);
    });

    $(document).on('click', '.pokemon', function(){
        var id = $(this).attr('id');
        $.getJSON(`${baseURL}${id}`, function(pokemonInfo){
            $("#details").html( `<h2>Name: ${pokemonInfo.name}</h2>
                                 <p>Height: ${pokemonInfo.height}</p>
                                 <p>Weight: ${pokemonInfo.weight}</p> 
                                `);
        });
    });
});
