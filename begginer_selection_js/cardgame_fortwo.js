function Main(input) {
    input = input.split("\n");
    var n = parseInt(input[0], 10);
    var cardText = input[1].split(" ");
    var cardNumebers = cardText.map(x => parseInt(x, 10));
    cardNumbers = cardNumebers.sort(
        function(a, b){
            return (a < b ? 1 : -1);
        }
    );
    var alice = 0;
    for (let i = 0; i < n; i += 2 ){
        if (cardNumebers[i]){
            alice += cardNumebers[i];
        } 
        if (cardNumebers[i+1]){
            alice -= cardNumebers[i+1];
        }
    }
    console.log(alice);
}

Main(require("fs").readFileSync("/dev/stdin", "utf8"));