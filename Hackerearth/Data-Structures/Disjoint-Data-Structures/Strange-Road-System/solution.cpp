#include <bits/stdc++.h>

using namespace std;

template <int X>
class LinearBasis
{
public:
  LinearBasis() : xs(X, 0), n(0)
  {
  }

  void add(int x)
  {
    for (int i = 0; i < n; ++i)
    {
      if ((x ^ xs[i]) < x)
      {
        x ^= xs[i];
      }
    }
    if (x == 0)
    {
      return;
    }

    xs[n++] = x;

    for (int i = 0; i < n - 1; ++i)
    {
      if (xs[i] < xs[i + 1])
      {
        swap(xs[i], xs[i + 1]);
      }
    }
  }

  int maximize(int x)
  {
    for (int i = 0; i < n; ++i)
    {
      if ((x ^ xs[i]) > x)
      {
        x ^= xs[i];
      }
    }
    return x;
  }

  void append(const LinearBasis &other)
  {
    for (int i = 0; i < other.n; ++i)
    {
      add(other.xs[i]);
    }
  }

protected:
  int n = 0;
  vector<int> xs;
};

class DisjointSet
{
public:
  DisjointSet(int n = 0) : N(n), pars(N, -1), lbs(N), dis(N, 0)
  {
  }

  void init(int n)
  {
    N = n;
    pars.resize(N);
    fill(pars.begin(), pars.end(), -1);
    lbs.clear();
    lbs.resize(N);
    dis.resize(N);
    fill(dis.begin(), dis.end(), 0);
  }

  int find(int x)
  {
    int p = pars[x];
    if (p < 0)
    {
      return x;
    }

    int root = find(p);

    dis[x] ^= dis[p];
    pars[x] = root;

    return root;
  }

  bool merge(int x, int y, int w)
  {
    int b = distance(x) ^ distance(y) ^ w;
    x = find(x);
    y = find(y);
    if (x == y)
    {
      lbs[x].add(b);
      return false;
    }

    if (-pars[x] > -pars[y])
    {
      swap(x, y);
    }
    dis[x] = b;
    pars[y] += pars[x];
    pars[x] = y;

    lbs[y].append(lbs[x]);

    return true;
  }

  int distance(int x)
  {
    find(x);
    return dis[x];
  }

  int query(int x, int y)
  {
    if (find(x) != find(y))
    {
      return -1;
    }
    int res = dis[x] ^ dis[y];
    return lbs[find(x)].maximize(res);
  }

private:
  int N;
  vector<int> pars;
  vector<LinearBasis<32>> lbs;
  vector<int> dis;
};

class Solution
{
public:
  void init(int n)
  {
    ds.init(n);
  }

  void update(int x, int y, int w)
  {
    ds.merge(x, y, w);
  }

  int query(int x, int y)
  {
    return ds.query(x, y);
  }

private:
  DisjointSet ds;
};

int main(int argc, char **argv)
{
  ios::sync_with_stdio(false);
  cin.tie(0);

  Solution sol;
  int n, q;
  cin >> n >> q;

  sol.init(n);

  while (q-- > 0)
  {
    int t, u, v, p;
    cin >> t >> u >> v;
    --u, --v;
    if (t == 1)
    {
      cin >> p;
      sol.update(u, v, p);
    }
    else
    {
      cout << sol.query(u, v) << "\n";
    }
  }

  return 0;
}