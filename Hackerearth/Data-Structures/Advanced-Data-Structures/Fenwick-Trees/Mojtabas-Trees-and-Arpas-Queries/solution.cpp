#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef long double ld;

const int maxn = 3e5 + 10;
const int maxl = 22;

int n, par[2][maxn][maxl], h[2][maxn], st[2][maxn], ft[2][maxn], Time[2];
vector<int> t[2][maxn];
vector<int> vec[maxn];

int x[maxn], y[maxn], answer[maxn];

int fen[maxn];

int get(int idx)
{
  idx++;
  int ret = 0;
  for (; idx; idx -= idx & -idx)
    ret += fen[idx];
  return ret;
}

void add(int idx, int val)
{
  idx++;
  for (; idx <= n; idx += idx & -idx)
    fen[idx] += val;
}

int lca(bool w, int v, int u)
{
  if (h[w][v] > h[w][u])
    swap(v, u);
  for (int i = 19; i >= 0; i--)
    if (h[w][u] - (1 << i) >= h[w][v])
      u = par[w][u][i];
  if (v == u)
    return v;
  for (int i = 19; i >= 0; i--)
  {
    if (par[w][v][i] != par[w][u][i])
    {
      v = par[w][v][i];
      u = par[w][u][i];
    }
  }
  return par[w][v][0];
}

void dfs(int v, int parent = -1)
{
  add(st[1][v], +1);
  add(ft[1][v], -1);
  for (auto it : vec[v])
  {
    int sign = 1;
    int idx = it;
    int ans = 0;
    if (it < 0)
    {
      idx *= -1;
      sign *= -1;
    }
    if (st[1][x[idx]] > st[1][y[idx]])
      swap(x[idx], y[idx]);
    if (ft[1][x[idx]] >= ft[1][y[idx]])
    {
      ans += get(st[1][y[idx]]);
      if (x[idx] != 1)
        ans -= get(st[1][par[1][x[idx]][0]]);
      answer[idx] += sign * ans;
    }
    else
    {
      int z = lca(1, x[idx], y[idx]);
      ans += get(st[1][x[idx]]);
      ans += get(st[1][y[idx]]);
      ans -= get(st[1][z]);
      if (z != 1)
        ans -= get(st[1][par[1][z][0]]);
      answer[idx] += sign * ans;
    }
  }
  for (auto u : t[0][v])
    if (u != parent)
      dfs(u, v);
  add(st[1][v], -1);
  add(ft[1][v], +1);
}

void dfs1(int v, bool w, int parent = -1)
{
  par[w][v][0] = parent;
  for (int i = 1; par[w][v][i - 1] != -1 and i <= 19; i++)
    par[w][v][i] = par[w][par[w][v][i - 1]][i - 1];
  st[w][v] = Time[w]++;
  for (auto u : t[w][v])
  {
    if (u != parent)
    {
      h[w][u] = h[w][v] + 1;
      dfs1(u, w, v);
    }
  }
  ft[w][v] = Time[w];
}

int main()
{
  ios_base::sync_with_stdio(false);
  int m;
  cin >> n >> m;
  for (int i = 1; i <= n - 1; i++)
  {
    int v, u;
    cin >> v >> u;
    t[0][v].push_back(u);
    t[0][u].push_back(v);
  }
  for (int i = 1; i <= n - 1; i++)
  {
    int v, u;
    cin >> v >> u;
    t[1][v].push_back(u);
    t[1][u].push_back(v);
  }
  memset(par, -1, sizeof par);
  dfs1(1, 0);
  dfs1(1, 1);
  for (int i = 1; i <= m; i++)
  {
    int a, b;
    cin >> a >> b >> x[i] >> y[i];
    if (st[a] > st[b])
      swap(a, b);
    if (ft[b] <= ft[a])
    {
      vec[b].push_back(i);
      if (a != 1)
        vec[par[0][a][0]].push_back(-i);
    }
    else
    {
      int c = lca(0, a, b);
      vec[a].push_back(i);
      vec[b].push_back(i);
      vec[c].push_back(-i);
      if (c != 1)
        vec[par[0][c][0]].push_back(-i);
    }
  }
  dfs(1);
  for (int i = 1; i <= m; i++)
    cout << answer[i] << '\n';
}