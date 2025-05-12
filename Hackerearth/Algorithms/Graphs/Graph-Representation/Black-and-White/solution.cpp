#include <bits/stdc++.h>
using namespace std;

#define pb push_back
#define mp make_pair
#define X first
#define Y second
#define zero 1001
#define black 0
#define white 1
#define ini(a) memset(a, -1, sizeof(a))

vector<pair<int, int>> g[1005];
int control[1005];
int dp[1005][2005];

int dijkstra(int source, int n)
{
  ini(dp);
  set<pair<int, pair<int, int>>> s;
  int index = (control[source] == black) ? (zero - 1) : (zero + 1);
  dp[source][index] = 0;
  s.insert(mp(0, mp(source, index)));
  while (!s.empty())
  {
    int u = s.begin()->Y.X;
    int dif = s.begin()->Y.Y;
    s.erase(s.begin());
    for (int i = 0; i < g[u].size(); i++)
    {
      int v = g[u][i].X;
      int w = g[u][i].Y;
      int ind = (control[v] == black) ? (dif - 1) : (dif + 1);
      if (dp[v][ind] == -1 || dp[v][ind] > dp[u][dif] + w)
      {
        s.erase(mp(dp[v][ind], mp(v, ind)));
        dp[v][ind] = dp[u][dif] + w;
        s.insert(mp(dp[v][ind], mp(v, ind)));
      }
    }
  }
  int ans = INT_MAX;
  for (int i = -1; i <= 1; i++)
  {
    if (dp[n][zero + i] != -1)
      ans = min(ans, dp[n][zero + i]);
  }
  return ans;
}

int main()
{
  int n, m;
  scanf("%d%d", &n, &m);
  for (int i = 0; i < m; i++)
  {
    int u, v, l;
    scanf("%d%d%d", &u, &v, &l);
    g[u].pb(mp(v, l));
  }
  for (int i = 1; i <= n; i++)
  {
    scanf("%d", &control[i]);
  }
  int ans = dijkstra(1, n);
  if (ans == INT_MAX)
    ans = -1;
  printf("%d\n", ans);
}