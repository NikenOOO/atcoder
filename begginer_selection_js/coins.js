function Main(input) {
    input = input.split("\n");
    var a = parseInt(input[0], 10);
    var b = parseInt(input[1], 10);
    var c = parseInt(input[2], 10);
    var x = parseInt(input[3], 10);
    var count = 0;
    for (var i = 0; i <= a; i++){
        for (var j = 0; j <= b; j++){
            for (var k = 0; k <= c; k++){
                if ( (10*i + 2*j + k) == x/50 ){
                    count++;
                }
            }
        }

    }
    console.log(count);
}
Main(require("fs").readFileSync("/dev/stdin", "utf8"));