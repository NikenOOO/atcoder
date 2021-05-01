function Main(input) {
    input = input.replace(/\n/, "");
    let [r, x, y] = input.split(" ").map(Number);
    let euclid = Math.sqrt(x**2+y**2);
    let answer;
    
    if (euclid < r){
        answer = 2;
    } else {
       answer = Math.ceil(euclid/r);
    }
    
    console.log(answer);
}
Main(require("fs").readFileSync("/dev/stdin", "utf8"));