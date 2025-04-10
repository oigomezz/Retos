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
    const k = +lines[l++];
    const arr = lines[l++].trim().split(" ").map(Number);
    const edges = lines
      .slice(l, l + n - 1)
      .map((str) => str.trim().split(" ").map(Number));
    l += n - 1;
    output[i] = solve(n, k, arr, edges);
  }
  console.log(output.join("\n"));
});

function solve(n, k, arr, edges) {
  const adj = {};
  edges.forEach(([a, b]) => {
    adj[a] = adj[a] || [];
    adj[b] = adj[b] || [];
    adj[a].push(b);
    adj[b].push(a);
  });
  arr.unshift(0);

  const sum = arr.reduce((s, x) => s + x, 0);

  const [m1, d1] = dfs(adj, 1, {}, k, arr);
  const m2 = dfs2(adj, 1, {}, k, arr, d1);
  return sum + Math.max(m1, m2);
}

function dfs(adj, r, visited, k, arr) {
  const stack = [[r, 0, -1]];
  const delta = [];
  let max = 0;
  while (stack.length) {
    const [u, i, p] = stack[stack.length - 1];
    visited[u] = 1;

    const nb = adj[u] || [];
    if (!i) {
      // first visited
    }
    if (i < nb.length) {
      stack[stack.length - 1][1]++;
      const v = nb[i];
      if (v !== p) stack.push([v, 0, u]);
    } else {
      // last visited
      delta[u] = (arr[u] ^ k) - arr[u];
      (adj[u] || []).forEach((v) => {
        if (v !== p) delta[u] += delta[v];
      });
      max = Math.max(max, delta[u]);
      stack.pop();
    }
  }
  return [max, delta];
}

function dfs2(adj, r, visited, k, arr, d1) {
  const stack = [[r, 0, -1, 0]];
  const agg = [];
  let max = 0;
  let now = 0; // the extra sum of the stack
  while (stack.length) {
    const [u, i, p, extra] = stack[stack.length - 1];
    visited[u] = 1;

    const nb = adj[u] || [];
    if (!i) {
      // first visited
      now += extra;

      agg[u] = [];
      nb.forEach((v, j) => {
        const add = v === p ? 0 : d1[v];
        agg[u][j] = j ? agg[u][j - 1] + add : add;
        if (v === p) max = Math.max(max, now);
      });
    }
    if (i < nb.length) {
      stack[stack.length - 1][1]++;
      const v = nb[i];
      // if (!visited[v]) { // has circle
      if (v !== p) {
        const temp =
          (arr[u] ^ k) -
          arr[u] +
          agg[u][nb.length - 1] -
          agg[u][i] +
          (i ? agg[u][i - 1] : 0);
        stack.push([v, 0, u, temp]);
      }
    } else {
      // last visited
      now -= extra;
      stack.pop();
    }
  }

  return max;
}
