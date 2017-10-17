var amount = 0.01;
var earned = 0.01;
var isOver10k = false;
var isOver1Billion = false;
var isInfinity = false;

for (var i=1; i <=1031 ; i++){
    if(i==1){
        earned = 0.01;
    }
    amount *= 2;
    earned += amount;

    if(earned >= 10000 && isOver10k == false){
        console.log('It took ', i, 'days to make $10000');
        isOver10k = true;
    }

    if(earned >= 1000000000 && isOver1Billion == false){
        console.log('It took ', i, 'days to make $1 Billion');
        isOver1Billion = true;
    }
    
    if(earned >= Infinity && isInfinity == false){
        console.log('It took ', i, 'days to make infinity');
        isInfinity = true;
    }
}

console.log("Amount earned after 1031 days: " + earned);