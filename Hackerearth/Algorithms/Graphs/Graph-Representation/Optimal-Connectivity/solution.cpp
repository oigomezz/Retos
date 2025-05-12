#include <bits/stdc++.h>
#define MAX 100005
using namespace std;

const int logN = 20;
int f[MAX][logN], mval[MAX][logN], depth[MAX];
vector<pair<int, int>> v[100005];

void dfs(int u)
{
  for (int i = 1; i < logN; i++)
  {
    f[u][i] = f[f[u][i - 1]][i - 1];
    mval[u][i] = max(mval[u][i - 1], mval[f[u][i - 1]][i - 1]);
  }
  for (auto &[ver, w] : v[u])
  {
    if (!depth[ver])
    {
      f[ver][0] = u;
      mval[ver][0] = w;
      depth[ver] = depth[u] + 1;
      dfs(ver);
    }
  }
}

int lca(int x, int y)
{
  if (depth[y] > depth[x])
    swap(x, y);
  int ans = 0;
  for (int i = logN - 1; i >= 0; i--)
  {
    if (depth[f[x][i]] >= depth[y])
    {
      ans = max(ans, mval[x][i]);
      x = f[x][i];
    }
  }
  if (x == y)
    return ans;
  for (int i = logN - 1; i >= 0; i--)
  {
    if (f[x][i] != f[y][i])
    {
      ans = max(ans, max(mval[x][i], mval[y][i]));
      x = f[x][i];
      y = f[y][i];
    }
  }
  return max(ans, max(mval[x][0], mval[y][0]));
}

int main()
{
  int n;
  cin >> n;
  for (int i = 1; i < n; i++)
  {
    int x, y, z;
    cin >> x >> y >> z;
    v[x].push_back({y, z});
    v[y].push_back({x, z});
  }
  depth[1] = 1;
  dfs(1);
  int q;
  cin >> q;
  while (q--)
  {
    int x, y, z;
    cin >> x >> y >> z;
    int val = lca(x, y);
    if (val > z)
      cout << "YES\n";
    else
      cout << "NO\n";
  }
  return 0;
}