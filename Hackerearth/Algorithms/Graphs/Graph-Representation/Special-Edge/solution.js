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
    const [n, m] = lines[l++].trim().split(" ").map(Number);
    const arr = lines[l++].trim().split(" ").map(Number);
    const edges = lines
      .slice(l, l + m)
      .map((str) => str.trim().split(" ").map(Number));
    l += m;
    output[i] = solve(n, arr, edges);
  }
  console.log(output.join("\n"));
});
class Queue {
  constructor() {
    this.map = {};
    this.first = 0;
    this.last = -1;
  }
  push(...args) {
    let i = 0;
    if (!this.length) {
      this.first = this.last = 0;
      this.map[this.first] = args[i++];
    }
    for (; i < args.length; i++) {
      this.map[++this.last] = args[i];
    }
  }
  unshift(...args) {
    let i = 0;
    if (!this.length) {
      this.first = this.last = 0;
      this.map[this.first] = args[i++];
    }
    for (; i < args.length; i++) {
      this.map[--this.first] = args[i];
    }
  }
  pop() {
    const r = this.map[this.last];
    delete this.map[this.last];
    this.last--;
    return r;
  }
  shift() {
    const r = this.map[this.first];
    delete this.map[this.first];
    this.first++;
    return r;
  }
  get length() {
    if (this.first > this.last) return 0;
    return this.last - this.first + 1;
  }
  getLast() {
    return this.map[this.last];
  }
  get(x) {
    return this.map[this.first + x];
  }
  forEach(fn) {
    for (let i = this.last; i >= this.first; i--) {
      if (fn(this.map[i], i - this.first) === false) return;
    }
  }
}

function solve(n, arr, edges) {
  arr.unshift(0);

  const adj = {};
  edges.forEach(([a, b], i) => {
    if (a > b) {
      [a, b] = [b, a];
      edges[i] = [a, b];
    }
    adj[a] = adj[a] || [];
    adj[b] = adj[b] || [];
    adj[a].push([b, i]);
    adj[b].push([a, i]);
  });

  const bad = Array(edges.length);
  const dp = Array(n + 1).fill(0);
  dfs(1, {});
  const total = arr.reduce((s, x) => s + x, 0);
  const sum = Array(n + 1);
  const ans = dfs2(1, {});
  return ans.join(" ");

  function dfs(r, visited) {
    const stack = new Queue();
    stack.push([r, 0, -1, -1]);
    while (stack.length) {
      const [u, i, p, ei] = stack.getLast();
      visited[u] = 1;

      const nb = adj[u] || [];
      if (!i) {
        // first visited
      }

      if (i < nb.length) {
        stack.getLast()[1]++;
        const [v, cei] = nb[i];
        if (!visited[v]) {
          stack.push([v, 0, u, cei]);
        } else if (v !== p && !bad[cei]) {
          bad[cei] = 1;
          mark(v, u);
        }
      } else {
        // last visited
        stack.pop();
      }
    }
  }

  function mark(u, v) {
    dp[u] += 1;
    dp[v] += 1;
    dp[u] -= 2;
  }

  function dfs2(r, visited) {
    const stack = new Queue();
    stack.push([r, 0, -1, -1]);
    let max,
      mei = -1;
    while (stack.length) {
      const [u, i, p, ei] = stack.getLast();
      visited[u] = 1;

      const nb = adj[u] || [];
      if (!i) {
        // first visited
        sum[u] = arr[u];
      }
      if (i < nb.length) {
        stack.getLast()[1]++;
        const [v, cei] = nb[i];
        if (!visited[v]) {
          stack.push([v, 0, u, cei]);
        }
      } else {
        // last visited
        stack.pop();
        if (p > 0) {
          sum[p] += sum[u];
          dp[p] += dp[u];
        }
        if (!dp[u] && !bad[ei]) {
          const temp = BigInt(sum[u]) * BigInt(total - sum[u]);
          if (mei < 0 || temp > max) {
            mei = ei;
            max = temp;
          } else if (temp === max) {
            mei = smallerEdge(mei, ei);
            max = temp;
          }
        }
      }
    }
    return edges[mei] || [n + 1, n + 1];
  }

  function smallerEdge(i, j) {
    if (i < 0) return j;

    let [a, b] = edges[i];
    // if (a > b) [a, b] = [b, a]
    let [c, d] = edges[j];
    // if (c > d) [c, d] = [d, c]

    if (a === c) return b < d ? i : j;
    else return a < c ? i : j;
  }
}
