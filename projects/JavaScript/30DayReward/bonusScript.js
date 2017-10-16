var amount = 0.01;
var isOver10k = false;
var isOver1Billion = false;
var isInfinity = false;

for (var i=1; i <=1031 ; i++){
    amount *= 2;
    if(amount >= 10000 && isOver10k == false){
        console.log('It took ', i, 'days to make $10000');
        isOver10k = true;
    }

    if(amount >= 1000000000 && isOver1Billion == false){
        console.log('It took ', i, 'days to make $1 Billion');
        isOver1Billion = true;
    }
    
    if(amount >= Infinity && isInfinity == false){
        console.log('It took ', i, 'days to make infinity');
        isInfinity = true;
    }
}

console.log("Amount after 1031 days: " + amount);