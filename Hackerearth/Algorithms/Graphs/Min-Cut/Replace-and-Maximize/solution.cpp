#include <bits/stdc++.h>

using namespace std;
typedef long long ll;

namespace F
{
  const int maxn = 1e4 + 14, maxm = 20 * maxn, inf = 1e9, so = maxn - 1, si = maxn - 2;
  int ptr[maxn], head[maxn], prv[maxm], to[maxm], cap[maxm], d[maxn], q[maxn], ec;

  void init()
  {
    memset(head, -1, sizeof head);
    ec = 0;
  }

  void add(int v, int u, int vu, int uv = 0)
  {
    to[ec] = u, prv[ec] = head[v], cap[ec] = vu, head[v] = ec++;
    to[ec] = v, prv[ec] = head[u], cap[ec] = uv, head[u] = ec++;
  }

  bool bfs()
  {
    memset(d, 63, sizeof d);
    d[so] = 0;
    int h = 0, t = 0;
    q[t++] = so;
    while (h < t)
    {
      int v = q[h++];
      for (int e = head[v]; e >= 0; e = prv[e])
        if (cap[e] && d[to[e]] > d[v] + 1)
        {
          d[to[e]] = d[v] + 1;
          q[t++] = to[e];
          if (to[e] == si)
            return 1;
        }
    }
    return 0;
  }

  int dfs(int v, int f = inf)
  {
    if (v == si || f == 0)
      return f;
    int r = 0;
    for (int &e = ptr[v]; e >= 0; e = prv[e])
      if (d[v] == d[to[e]] - 1)
      {
        int x = dfs(to[e], min(f, cap[e]));
        f -= x, r += x;
        cap[e] -= x, cap[e ^ 1] += x;
        if (!f)
          break;
      }
    return r;
  }

  int mf()
  {
    int ans = 0;
    while (bfs())
    {
      memcpy(ptr, head, sizeof ptr);
      ans += dfs(so);
    }
    return ans;
  }
};

const int MAX_N = 1e2 + 14;

int n;

int main()
{
  ios::sync_with_stdio(0), cin.tie(0);
  F::init();
  cin >> n;
  for (int i = 0; i < n; ++i)
  {
    for (int j = 0; j < n; ++j)
    {
      int x;
      cin >> x;
      x ^= x != 2 && (i + j) % 2;
      if (x == 0)
        F::add(F::so, i * n + j, F::inf);
      else if (x == 1)
        F::add(i * n + j, F::si, F::inf);
      if (i + 1 < n)
      {
        F::add(i * n + j, i * n + n + j, 1);
        F::add(i * n + n + j, i * n + j, 1);
      }
      if (j + 1 < n)
      {
        F::add(i * n + j, i * n + j + 1, 1);
        F::add(i * n + j + 1, i * n + j, 1);
      }
    }
  }
  cout << n * (n - 1) * 2 - F::mf() << '\n';
}