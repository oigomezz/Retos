#include <bits/stdc++.h>
using namespace std;

const int N = 1e5 + 5;
const int sq = sqrtl(N);

struct Query
{
  int l, r, id;
  bool operator<(const Query &q) const
  {
    if (l / sq != q.l / sq)
    {
      return l < q.l;
    }
    if ((l / sq) & 1)
    {
      return r < q.r;
    }
    return r > q.r;
  }
};

template <typename T>
struct fenwick
{
  int n;
  vector<T> fen;
  fenwick(int n)
  {
    this->n = n + 1;
    fen.assign(n + 1, 0);
  }
  void update(int x, int val)
  {
    x++;
    while (x < n)
    {
      fen[x] += val;
      x += x & -x;
    }
  }
  T query(int x)
  {
    T res = 0;
    x++;
    while (x > 0)
    {
      res += fen[x];
      x -= x & -x;
    }
    return res;
  }
  T query(int l, int r)
  {
    return query(r) - query(l - 1);
  }
};

int main()
{
  ios_base::sync_with_stdio(false);
  cin.tie(0);

  int n, x;
  cin >> n >> x;

  vector<int> a(n), t;
  for (int i = 0; i < n; ++i)
  {
    cin >> a[i];
    t.push_back(a[i]);
  }

  vector<long long> res(x);

  vector<Query> q(x);
  for (int i = 0; i < x; ++i)
  {
    cin >> q[i].l >> q[i].r;
    q[i].l--, q[i].r--;
    q[i].id = i;
  }

  sort(q.begin(), q.end());

  sort(t.begin(), t.end());
  for (auto &xx : a)
  {
    xx = lower_bound(t.begin(), t.end(), xx) - t.begin() + 1;
  }

  fenwick<int> ds(n + 5);

  long long inv = 0;

  int l = 0, r = 0;

  for (int i = 0; i < x; ++i)
  {
    while (r <= q[i].r)
    {
      inv += ds.query(a[r] + 1, n + 4);
      ds.update(a[r], 1);
      r++;
    }
    while (r - 1 > q[i].r)
    {
      r--;
      ds.update(a[r], -1);
      inv -= ds.query(a[r] + 1, n + 4);
    }
    while (l > q[i].l)
    {
      l--;
      inv += ds.query(0, a[l] - 1);
      ds.update(a[l], 1);
    }
    while (l < q[i].l)
    {
      ds.update(a[l], -1);
      inv -= ds.query(0, a[l] - 1);
      l++;
    }
    res[q[i].id] = inv;
  }

  for (int i = 0; i < x; ++i)
  {
    cout << res[i] << '\n';
  }

  return 0;
}