const readline = require("readline");

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

const lines = [];
const MOD = 1e9 + 7;
const MOD_CUT = ((1 << 20) * (1 << 20)) % MOD;

function add(a, b) {
  return (a + b) % MOD;
}

function mul(a, b) {
  let r =
    (a >> 20) * (b >> 20) * MOD_CUT +
    (a & 0xfff00000) * (b & 0xfffff) +
    (a & 0xfffff) * b;
  return r % MOD;
}

function lmul(...args) {
  return args.reduce((s, x) => mul(s, x), 1);
}

function initDSU(n) {
  const p = Array(n); // parent
  for (let i = 0; i < n; i++) p[i] = i;

  const r = Array(n).fill(1); // rank
  return [p, r];
}

function find(u, p) {
  if (p[u] !== u) {
    p[u] = find(p[u], p);
    return p[u];
  }
  return u;
}

rl.on("line", (input) => {
  lines.push(input);
});

rl.on("close", () => {
  let l = 0;
  let t = 1;
  const output = [];
  for (let i = 0; i < t; i++) {
    const n = +lines[l++];
    const edges = lines
      .slice(l, l + n - 1)
      .map((str) => str.trim().split(" ").map(Number));
    l += n - 1;
    output[i] = solve(n, edges);
  }
  console.log(output.join("\n"));
});

function solve(n, edges) {
  edges.sort((a, b) => a[2] - b[2]);

  const sum = Array(n + 1);
  for (let i = 1; i <= n; i++) sum[i] = i;

  const [p, r] = initDSU(n + 5);
  let ans = 0;
  for (let [u, v, w] of edges) {
    u = find(u, p);
    v = find(v, p);

    if (u === v) continue;

    const temp = lmul(sum[u], sum[v], w);
    ans = add(ans, temp);

    if (r[u] < r[v]) [u, v] = [v, u];

    p[v] = u;
    r[u] += r[v];

    sum[u] = add(sum[u], sum[v]);
  }
  return ans;
}
