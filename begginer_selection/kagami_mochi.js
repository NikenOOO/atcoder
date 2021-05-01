function Main(input) {
    input = input.split("\n")
    input.shift();
    input.pop();
    var mochi = input.map(x => parseInt(x, 10));
    var mochiSet = Array.from(new Set(mochi));
    console.log(mochiSet.length);
}
Main(require("fs").readFileSync("/dev/stdin", "utf8"));