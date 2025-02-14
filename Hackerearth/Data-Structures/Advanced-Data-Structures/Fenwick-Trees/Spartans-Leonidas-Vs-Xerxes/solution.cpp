#include "bits/stdc++.h"
using namespace std;
typedef long long int ll;

struct node
{
  int len;
  int pre, suff, opt;
  ll first, last;
  node()
  {
    len = 0, pre = 0, suff = 0, opt = 0;
    first = -1e16, last = -1e16;
  }
  node(ll x)
  {
    len = 1, pre = 1, suff = 1, opt = 1;
    first = x, last = x;
  }
};

class SegTree
{
public:
  int n;
  node *t;
  node id = node();
  SegTree(int _n)
  {
    n = _n;
    t = new node[4 * n + 10];
    for (int i = 0; i < 4 * n + 10; ++i)
    {
      t[i] = id;
    }
  }
  node comb(node a, node b)
  {
    if (a.len == 0 and b.len == 0)
      return a;
    if (b.len and a.len == 0)
      return b;
    if (a.len and b.len == 0)
      return a;
    node x = id;
    x.pre = a.pre;
    if (a.len == a.pre and a.last < b.first)
    {
      x.pre = max(x.pre, a.len + b.pre);
    }

    x.suff = b.suff;
    if (b.len == b.suff and a.last < b.first)
    {
      x.suff = max(x.suff, b.len + a.suff);
    }
    x.len = a.len + b.len;
    x.first = a.first;
    x.last = b.last;
    int p = 0;
    if (a.last < b.first)
    {
      p = max(p, a.suff + b.pre);
    }
    x.opt = max({x.pre, x.suff, p, a.opt, b.opt});
    return x;
  }

  void build(vector<long long int> &v, int tl, int tr, int idx)
  {
    if (tl == tr)
    {
      if (tl < (int)v.size())
        t[idx] = v[tl];
      return;
    }
    int mid = tl + (tr - tl) / 2;
    build(v, tl, mid, 2 * idx);
    build(v, mid + 1, tr, 2 * idx + 1);
    t[idx] = comb(t[2 * idx], t[2 * idx + 1]);
  }

  void update(int tl, int tr, int idx, int index, node val)
  {
    if (tl == tr and tl == index)
    {
      t[idx] = val;
      return;
    }
    int mid = tl + (tr - tl) / 2;
    if (index <= mid)
      update(tl, mid, 2 * idx, index, val);
    else
      update(mid + 1, tr, 2 * idx + 1, index, val);
    t[idx] = comb(t[2 * idx], t[2 * idx + 1]);
  }

  node query(int qs, int qe, int tl, int tr, int idx)
  {
    // no overlap
    if (qe < tl or tr < qs)
      return id;
    // complete overlap
    if (qs <= tl and tr <= qe)
    {
      return t[idx];
    }
    int mid = tl + (tr - tl) / 2;
    auto lnode = query(qs, qe, tl, mid, 2 * idx);
    auto rnode = query(qs, qe, mid + 1, tr, 2 * idx + 1);
    return comb(lnode, rnode);
  }
};

int main()
{
  ios_base::sync_with_stdio(0);
  cin.tie(0);
  cout.tie(0);
  int T;
  cin >> T;
  while (T--)
  {
    int n, q;
    cin >> n >> q;
    vector<ll> v(n);
    for (auto &i : v)
      cin >> i;
    int d = 0;

    for (int i = 0;; ++i)
    {
      ll N = 1ll << i;
      if (N >= n)
      {
        d = i;
        break;
      }
    }
    d = 1ll << d;
    d--;
    SegTree seg(d);
    seg.build(v, 0, d, 1);
    while (q--)
    {
      int t;
      cin >> t;
      ll x, y;
      cin >> x >> y;
      if (t == 1)
      {
        x--;
        v[x] += y;
        node p = node(v[x]);
        seg.update(0, d, 1, x, p);
      }
      else
      {
        x--, y--;
        auto p = seg.query(x, y, 0, d, 1);
        cout << p.opt << "\n";
      }
    }
  }
}