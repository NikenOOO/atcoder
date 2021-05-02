function Main(input) {
    input = input.split(/\n/);
    let [n, d, h] = input[0].split(" ").map(Number);
    let arrAB = [];
    let dh = [];
    let min = 1000;
    for (let i = 1; i < n; i++){
        let [d1, h1] = input[i].split(" ").map(Number);
        arrAB[i-1][0] = (h - h1)/(d - d1);
        arrAB[i-1][1] = h - (h - h1)/(d - d1)*d;
    }

    let a = h/d;
    arrAB.unshift([a, 0]);
    console.log(arrAB);
    let arrOk = [];

    for (let i = 0; i <= n; i++){
        let check = true;
        for (let j=0; j < n; j++){
            let [d1, h1] = input[j+1].split(" ").map(Number);
            if (arrAB[i][0]*d1 <= h1){
                check = false;
                break;
            }
        }
        if (check) {
            arrOk.unshift(arrAB[i][1]);
        }
    }

    console.log(min(arrOk));
}
// Main(require("fs").readFileSync("/dev/stdin", "utf8"));
Main(`1 10 10
3 5
`)