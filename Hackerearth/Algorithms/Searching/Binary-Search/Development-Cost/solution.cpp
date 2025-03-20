#include <bits/stdc++.h>
using namespace std;

const int N = 502;
const int M = 500002;

int n, m, q, k;
int a[N][N];
int st[M], e[M];
int dx[2] = {1, 0};
int dy[2] = {0, 1};

struct DSU
{
  int par[N * N], sz[N * N];
  DSU() {}
  DSU(int n)
  {
    for (int i = 0; i < n; i++)
    {
      par[i] = i;
      sz[i] = 1;
    }
  }
  int getPar(int k)
  {
    while (par[k] != par[par[k]])
      par[k] = par[par[k]];
    return par[k];
  }
  void unite(int u, int v)
  {
    int par1 = getPar(u), par2 = getPar(v);
    if (par1 == par2)
      return;
    if (sz[par1] > sz[par2])
    {
      sz[par1] += sz[par2];
      par[par2] = par[par1];
    }
    else
    {
      sz[par2] += sz[par1];
      par[par1] = par[par2];
    }
  }
};

int get(int y, int x)
{
  return y * m + x;
}

int get1(int y, int x)
{
  return (y - 1) * m + x - 1;
}

bool valid(int y, int x, int lim)
{
  if (y >= n || x >= m || a[y][x] > lim)
    return 0;
  return 1;
}

int check(int lim)
{
  DSU dsu(n * m);
  for (int i = 0; i < n; i++)
  {
    for (int j = 0; j < m; j++)
    {
      if (a[i][j] > lim)
        continue;
      for (int dir = 0; dir < 2; dir++)
      {
        int nx = i + dx[dir];
        int ny = j + dy[dir];
        if (valid(nx, ny, lim))
          dsu.unite(get(i, j), get(nx, ny));
      }
    }
  }
  int cnt = 0;
  for (int i = 0; i < q; i++)
  {
    cnt += dsu.getPar(st[i]) == dsu.getPar(e[i]);
    if (cnt >= k)
      return 1;
  }
  return 0;
}

int search(int lo, int hi)
{
  while (lo < hi)
  {
    int mid = (lo + hi) / 2;
    if (check(mid))
      hi = mid;
    else
      lo = mid + 1;
  }
  return lo;
}

int32_t main()
{
  ios::sync_with_stdio(0);
  cin.tie(0);
  cout.tie(0);
  ;
  cin >> n >> m >> q >> k;
  for (int i = 0; i < n; i++)
    for (int j = 0; j < m; j++)
      cin >> a[i][j];
  for (int i = 0; i < q; i++)
  {
    int xs, ys, xd, yd;
    cin >> ys >> xs >> yd >> xd;
    st[i] = get1(ys, xs);
    e[i] = get1(yd, xd);
  }
  int ans = search(1, 1e9);
  cout << ans << endl;
  return 0;
}