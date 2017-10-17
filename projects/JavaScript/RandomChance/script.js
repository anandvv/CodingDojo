function randomChance(numberOfQuarters){
    
    //precondition
    if(numberOfQuarters <= 0){
        console.log("Invalid Input!");
        return;
    }

    while(numberOfQuarters > 0){
        //pick a new number
        var numberPicked = Math.random() * 100;

        if((Math.random() * 100) == numberPicked){
            //you won
            var coinsWon = (Math.random() * 50) + 51;
            numberOfQuarters += coinsWon;
            console.log("You won!!");
            console.log("Your coin count is now: " + numberOfQuarters);
        }
        
        numberOfQuarters--;
    }

    //all out of coins
    console.log("Game Over!");
}

randomChance(100);
