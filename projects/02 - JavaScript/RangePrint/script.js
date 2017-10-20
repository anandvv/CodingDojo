function rangePrint(x, y, skip=1){
    if(y == undefined){
        y=x;
        x=0;
    }
    for(var i=x; i < y; i+=skip){
        console.log(i);
    }
}

rangePrint(-10, 20, 3);
console.log('--------------');
rangePrint(2, 6);
console.log('--------------');
rangePrint(10);