const readline = require("readline");

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

const lines = [];
rl.on("line", (input) => {
  lines.push(input);
});

rl.on("close", () => {
  let l = 0;
  let t = 1;
  const output = [];
  for (let i = 0; i < t; i++) {
    const w = +lines[l++];
    const n = +lines[l++];
    const arr = lines
      .slice(l, l + n)
      .map((str) => str.trim().split(" ").map(Number));
    l += n;
    output[i] = solve(w, n, arr);
  }
  console.log(output.join("\n"));
});

function solve(w, n, arr) {
  let max = 0,
    ans;
  for (let i = 0; i < arr.length; i++) {
    const [b, r, d] = arr[i];
    if (r > w || r > d) continue;
    if (b > max) {
      max = b;
      ans = i + 1;
    }
  }
  return `1\n${ans}`;
}
