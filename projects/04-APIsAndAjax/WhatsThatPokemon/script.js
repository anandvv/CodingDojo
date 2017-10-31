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
                                            <img id="pokemonImage" src=${pokemonInfo.sprites["front_default"]} />
                                         </div>
                                        `);
            });
        }, this);
    });

    $(document).on('click', '.pokemon', function(){
        var id = $(this).attr('id');
        var imgURL = $(this).children('#pokemonImage').attr('src');
        $.getJSON(`${baseURL}${id}`, function(pokemonInfo){
            var types = pokemonInfo.types;
            var unorderedListHTML = `<ul>`;
            types.forEach(function(element) {
                unorderedListHTML += `<li>${element.type.name}</li>
                                    `;
            }, this);
            unorderedListHTML += `</ul>`;
            
            $("#details").html( `<h2>Name: ${pokemonInfo.name}</h2>
                                 <p>Height: ${pokemonInfo.height}</p>
                                 <p>Weight: ${pokemonInfo.weight}</p> 
                                 <img src=${imgURL} />
                                `);
            $("#details").append(unorderedListHTML);
        });
    });
});
