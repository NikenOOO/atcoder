function Main(input) {
	input = input.split(" ");
    var a = parseInt(input[0], 10);
    var b = parseInt(input[1], 10);
    var text = (a * b)  % 2 === 0 ? "Even" : "Odd";
	console.log(text);
}
Main(require("fs").readFileSync("/dev/stdin", "utf8"));
