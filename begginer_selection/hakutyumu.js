function Main(input) {
    const eraser = input.replace(/eraser/, 'A');
    const erase = eraser.replace(/erase/, 'A');
    const dreamer = erase.replace(/dreamer/, 'A');
    const dream = dreamer.replace(/dream/, 'A');
    const string = dream.replace(/dream/, '');

    if ("") {
        console.log("true");
    } else {
        console.log("nil");
    }


}
Main(require("fs").readFileSync("/dev/stdin", "utf8"));
