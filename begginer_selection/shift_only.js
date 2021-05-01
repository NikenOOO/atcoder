function Main(input) {
	input = input.split("\n");
	const blackboard = input[1].split(" ");
    var n = parseInt(input[0], 10);
    var count = [];
    for (i = 0; i < n; i++){
    blackboard[i] = parseInt(blackboard[i], 10);
    count.push(0);
        while (blackboard[i] % 2 === 0){
            count[i]++
            blackboard[i] = blackboard[i]/2;
        }
    }

	console.log('%d %s',Math.max.apply(null, count));
}
Main(require("fs").readFileSync("/dev/stdin", "utf8"));
