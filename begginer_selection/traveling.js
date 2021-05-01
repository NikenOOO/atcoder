function Main(input) {
    input = input.split("\n");
    let n = parseInt(input[0], 10);
    input[0] = "0 0 0";
    let boolean = true;
    for ( let i = 0; i <= n-1; i++){
        var arrayI = number(input[i]);
        var arrayI1 = number(input[i+1]);
        var t = arrayI1[0] - arrayI[0]; 
        var x = arrayI1[1] - arrayI[1]; 
        var y = arrayI1[2] - arrayI[2];
        if (t < Math.abs(x) + Math.abs(y)) {
            boolean = false;
        } 
        if (arrayI[0] % 2 == 0 && (arrayI[1]+arrayI[2]) % 2 != 0 ) {
            boolean = false;
        } else if (arrayI[0] % 2 != 0 && (arrayI[1]+arrayI[2]) % 2 == 0 ){
            boolean = false;
        }
    }
    if (boolean){
        console.log("YES");
    } else {
        console.log("NO");
    }
}

function number(text){
    var array = text.split(" ");
    for (let i=0; i < array.length ; i++){
        array[i] = parseInt(array[i], 10);
    }
    return array;
}

Main(require("fs").readFileSync("/dev/stdin", "utf8"));