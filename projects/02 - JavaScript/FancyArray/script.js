var arr = [ "James", "Jill", "Jane", "Jack" ];

function fancyArray(arr, symbol, reversed=false){
    
    if(reversed !== true){
        for (var i=0; i < arr.length; i++){
            console.log(i + " " + symbol + " " + arr[i]);
        }    
    }
    else {
        for (var i=arr.length-1; i >= 0; i--){
            console.log(i + " " + symbol + " " + arr[i]);
        }
    }
}

//test cases
fancyArray(arr, "--------", true);
fancyArray(arr, "=>");


