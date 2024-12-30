process.stdin.resume();
process.stdin.setEncoding("utf-8");

let stdin_input = "";

process.stdin.on("data", function (input) {
  stdin_input += input;
});

process.stdin.on("end", function () {
  main(stdin_input);
});

function main(input) {
  input = input.split("\n");
  input.shift();
  input.forEach((t) => {
    t = t.split(" ").map((x) => +x);
    let count = 0;

    for (let i = Math.min(t[0], t[1]); i <= Math.max(t[0], t[1]); i++) {
      for (let j = Math.min(t[2], t[3]); j <= Math.max(t[2], t[3]); j++) {
        i === j && count++;
      }
    }

    if (count === 0) console.log("Line");
    else if (count === 1) console.log("Point");
    else console.log("Nothing");
  });
}
