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
  let t = +lines[l++];
  const output = [];
  for (let i = 0; i < t; i++) {
    const n = +lines[l++];
    const arr = lines[l++].trim().split(" ").map(Number);
    const edges = lines
      .slice(l, l + n - 1)
      .map((str) => str.trim().split(" ").map(Number));
    l += n - 1;
    const q = +lines[l++];
    const qs = lines
      .slice(l, l + q)
      .map((str) => str.trim().split(" ").map(Number));
    l += q;
    output[i] = solve(n, arr, edges, qs);
  }
  console.log(output.join("\n"));
});

let TIN, TOUT, TIMER;
function solve(n, arr, edges, qs) {
  const adj = {};
  edges.forEach(([a, b]) => {
    adj[a] = adj[a] || [];
    adj[b] = adj[b] || [];
    adj[a].push(b);
    adj[b].push(a);
  });
  arr.unshift(0);

  TIN = [];
  TOUT = [];
  TIMER = 0;
  const subs = dfs(adj, 1, {}, arr);
  return qs
    .map(([u, v, x]) => {
      if (isP(u, v) || isP(v, u)) return subs[x];
      if (x === u || x === v) return subs[x];
      if (isP(x, u) && isP(x, v)) return subs[x];
      if (isP(x, u)) return subs[x] - subs[u] + subs[v];
      if (isP(x, v)) return subs[x] - subs[v] + subs[u];
      return subs[x];
    })
    .join(" ");
}

function isP(u, v) {  // u is v's
  return TIN[u] <= TIN[v] && TOUT[u] >= TOUT[v];
}

function dfs(adj, r, visited, arr) {
  const stack = [[r, 0, -1]];
  const subs = [];
  while (stack.length) {
    const [u, i, p] = stack[stack.length - 1];
    visited[u] = 1;

    const nb = adj[u] || [];
    if (!i) TIN[u] = TIMER++; // first visited

    if (i < nb.length) {
      stack[stack.length - 1][1]++;
      const v = nb[i];
      if (v !== p) stack.push([v, 0, u]);
    } else {
      // last visited
      TOUT[u] = TIMER;
      let sum = arr[u];
      adj[u].forEach((v) => {
        if (v !== p) sum += subs[v];
      });
      subs[u] = sum;
      stack.pop();
    }
  }
  return subs;
}
