function Main(input) {
    input = input.split(" ");
    var paper = parseInt(input[0], 10);
    var sum = parseInt(input[1], 10);
    var paper10 = 0;
    var paper5 = 0;
    outer:
    for (let i = 0; i <= paper; i++){
        for(let j = 0; j <= paper - i; j++){
            if (sum - 1000*paper == 4000*i + 9000*j){
                paper10 += j;
                paper5 += i;
                break outer;
            }
        }
    }
    if (paper10 == 0 && paper5 == 0 && paper * 1000 != sum){
        console.log("-1 -1 -1");
    } else {
    console.log(`${paper10} ${paper5} ${paper - paper10 - paper5}`);
    }
}
Main(require("fs").readFileSync("/dev/stdin", "utf8"));