function numbersOnly(array){
    var newArray = [];
    var j=0;
    for(var i=0; i<array.length; i++){
        if(typeof(array[i]) === "number"){
            newArray[j++] = array[i];
        }
    }

    return newArray;
}

var newArray = numbersOnly([1, "apple", -3, "orange", 0.5]);
console.log(newArray);