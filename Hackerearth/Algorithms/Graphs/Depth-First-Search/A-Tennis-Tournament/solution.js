const readline = require("readline");

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

const lines = [];

rl.on("line", (input) => lines.push(input));

rl.on("close", () => {
  let l = 0;
  let t = 1;
  const output = [];
  for (let i = 0; i < t; i++) {
    const [n, m] = lines[l++].trim().split(" ").map(Number);
    const edges = lines
      .slice(l, l + m)
      .map((str) => str.trim().split(" ").map(Number));
    l += m;
    output[i] = solve(n, m, edges);
  }
  console.log(output.join("\n"));
});

function topo(n, adj, pre) {
  const q = [];
  for (let i = 1; i <= n; i++) if (!pre[i]) q.push(i);

  const chain = {};
  while (q.length) {
    const u = q.shift();
    chain[u] = 1;
    (adj[u] || []).forEach((v) => {
      pre[v]--;
      if (!pre[v]) q.push(v);
    });
  }
  return chain;
}

function solve(n, m, edges) {
  const adj = {};
  const radj = {};
  const pre = Array(n + 1).fill(0);
  const after = Array(n + 1).fill(0);
  edges.forEach(([a, b]) => {
    adj[a] = adj[a] || [];
    radj[b] = radj[b] || [];
    adj[a].push(b);
    radj[b].push(a);
    pre[b]++;
    after[a]++;
  });
  // find r
  const rs = [];
  for (let i = 1; i <= n; i++) {
    if (pre[i]) rs.push(i);
    else rs.unshift(i);
  }
  const chain1 = topo(n, adj, pre);
  const chain2 = topo(n, radj, after);
  if (Object.keys(chain1).length === n) return -1;
  const next = {};
  for (let i = 1; i <= n; i++) {
    if (!chain1[i] && !chain2[i]) {
      // skip the node after circle
      for (const element of adj[i]) {
        const v = element;
        if (!chain1[v] && !chain2[v]) {
          next[i] = v;
          break;
        }
      }
    }
  }
  const base = [];
  const used = {};
  for (let i = 1; i <= n; i++) {
    if (!chain1[i] && !chain2[i]) {
      let u = i;
      while (!used[u]) {
        used[u] = 1;
        u = next[u];
      }
      const v = u;
      base.push([u, next[u]]);
      u = next[u];
      while (u !== v) {
        base.push([u, next[u]]);
        u = next[u];
      }
      break;
    }
  }
  const fall = base.length + "\n" + base.map((x) => x.join(" ")).join("\n");
  let ans = Infinity;
  let bfirst;
  let blast; // best last
  let best;
  const skip = {};
  rs.forEach((r) => {
    if (skip[r]) return;
    const adj2 = bfs(adj, r, skip);
    dfs(adj2, r, {});
    const [min, visited, first, last] = bfs2(adj, r, skip);
    if (min < ans) {
      ans = min;
      bfirst = first;
      blast = last;
      best = visited;
    }
  });
  if (ans === Infinity) return fall;
  try {
    const es = [blast + " " + bfirst];
    let u = blast;
    while (u !== bfirst) {
      const p = best[u][1];
      es.unshift(p + " " + u);
      u = p;
    }
    return ans + "\n" + es.join("\n");
  } catch (e) {
    return fall;
  }
}

function bfs(adj, r, skip) {
  const q = [[r, 1, -1]];
  const visited = {};
  const adj2 = {};
  while (q.length) {
    const [u, d, p] = q.shift();
    if (skip[u]) continue;
    if (visited[u]) continue;
    visited[u] = [d, p];
    (adj[u] || []).forEach((v) => {
      if (visited[v]) {
        //
      } else {
        q.push([v, d + 1, u]);
        // keep
        adj2[u] = adj2[u] || [];
        adj2[u].push(v);
      }
    });
  }
  return adj2;
}

function bfs2(adj, r, skip) {
  const q = [[r, 1, -1]];
  let min = Infinity;
  let first;
  let last;
  const visited = {};
  while (q.length) {
    const [u, d, p] = q.shift();
    if (skip[u]) continue;
    if (visited[u]) continue;
    skip[u] = 1;
    visited[u] = [d, p];
    (adj[u] || []).forEach((v) => {
      if (visited[v]) {
        if (visited[v][0] < d && isp(v, u)) {
          const size = d + 1 - visited[v][0];
          if (size < min) {
            min = size;
            first = v;
            last = u;
          }
        }
      } else {
        q.push([v, d + 1, u]);
      }
    });
  }
  return [min, visited, first, last];
}
let TIMER, TIN, TOUT;
function dfs(adj, r, visited) {
  TIMER = 0;
  TIN = [];
  TOUT = [];

  const stack = [[r, 0, -1]];
  while (stack.length) {
    const [u, i, p] = stack[stack.length - 1];
    visited[u] = 1;

    const nb = adj[u] || [];
    if (!i) {
      // first visited
      TIN[u] = TIMER++;
    }
    if (i < nb.length) {
      stack[stack.length - 1][1]++;
      const v = nb[i];
      if (!visited[v]) {
        // has circle
        // if (v !== p) {
        stack.push([v, 0, u]);
      }
    } else {
      // last visited
      TOUT[u] = TIMER;
      stack.pop();
    }
  }
}

function isp(u, v) {
  return TIN[u] <= TIN[v] && TOUT[u] >= TOUT[v];
}
