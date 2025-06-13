#include <bits/stdc++.h>

using namespace std;

#define GODSPEED           \
  ios::sync_with_stdio(0); \
  cin.tie(0);              \
  cout.tie(0);             \
  cout << fixed;           \
  cout << setprecision(15);
#define pb push_back
#define mset(a, x) memset(a, x, sizeof(a))
#define deb1(a) cout << a << "\n";

typedef long long ll;
const ll N = 5e5 + 5;
const ll LEVEL = log2(N) + 1;

ll n, m, dp[N], d[N], p[N], bridge[N], val[N], st[N][LEVEL], up[N], down[N], w[N];
vector<pair<int, int>> g[N];
vector<int> adj[N];

void dfs(int x, int ind)
{
  for (auto [it, i] : g[x])
  {
    if (i == ind)
      continue;
    if (d[it] == -1)
    {
      p[it] = x;
      d[it] = d[x] + 1;
      dfs(it, i);
      dp[x] += dp[it];
      if (dp[it] == 0)
      {
        bridge[it] = 1;
        val[it] = w[i];
      }
      adj[x].pb(it);
    }
    else if (d[it] < d[x])
    {
      dp[x]++;
      dp[it]--;
    }
  }
}

void fill_st()
{
  mset(st, -1);
  for (int i = 1; i <= n; i++)
  {
    if (p[i])
      st[i][0] = p[i];
  }
  for (int j = 1; j < LEVEL; j++)
  {
    for (int i = 1; i <= n; i++)
    {
      if (st[i][j - 1] != -1)
        st[i][j] = st[st[i][j - 1]][j - 1];
    }
  }
}

int lca(int u, int v)
{
  if (d[u] < d[v])
    swap(u, v);
  for (int i = LEVEL - 1; i >= 0; i--)
  {
    if (d[u] - (1 << i) >= d[v])
      u = st[u][i];
  }
  if (u == v)
    return u;
  for (int i = LEVEL - 1; i >= 0; i--)
  {
    if (st[u][i] != st[v][i])
    {
      u = st[u][i];
      v = st[v][i];
    }
  }
  return p[u];
}

ll calcans(int x)
{
  ll res = 0;
  for (auto it : adj[x])
  {
    res += calcans(it);
    up[x] += up[it];
    down[x] += down[it];
  }
  if (bridge[x])
  {
    res += min(up[x], down[x]) * val[x];
  }
  return res;
}

int main()
{
  GODSPEED;
  cin >> n >> m;
  for (int i = 1; i <= m; i++)
  {
    int x, y;
    cin >> x >> y >> w[i];
    g[x].pb({y, i});
    g[y].pb({x, i});
  }
  mset(d, -1);
  for (int i = 1; i <= n; i++)
  {
    if (d[i] == -1)
    {
      d[i] = 0;
      p[i] = 0;
      dfs(i, 0);
    }
  }
  fill_st();
  int q;
  cin >> q;
  for (int i = 1; i <= q; i++)
  {
    int u, v;
    cin >> u >> v;
    int l = lca(u, v);
    up[u]++;
    up[l]--;
    down[v]++;
    down[l]--;
  }
  ll ans = 0;
  for (int i = 1; i <= n; i++)
  {
    if (p[i] == 0)
    {
      ans += calcans(i);
    }
  }
  deb1(ans)
}