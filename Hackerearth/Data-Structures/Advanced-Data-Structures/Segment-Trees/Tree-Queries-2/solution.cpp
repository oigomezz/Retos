#include "bits/stdc++.h"
#ifdef LOCAL
#include "pprint.hpp"
#else
#define trace
#endif

using namespace std;

template <typename Arg1>
void prn(Arg1 &&arg1)
{
  cout << arg1 << "\n";
}
template <typename Arg1, typename... Args>
void prn(Arg1 &&arg1, Args &&...args)
{
  cout << arg1 << " ";
  prn(args...);
}

template <typename Arg1>
void prs(Arg1 &&arg1)
{
  cout << arg1 << " ";
}
template <typename Arg1, typename... Args>
void prs(Arg1 &&arg1, Args &&...args)
{
  cout << arg1 << " ";
  prs(args...);
}

template <typename Arg1>
void read(Arg1 &&arg1)
{
  cin >> arg1;
}
template <typename Arg1, typename... Args>
void read(Arg1 &&arg1, Args &&...args)
{
  cin >> arg1;
  read(args...);
}

#define ll long long
#define pii pair<int, int>
#define pli pair<ll, int>
#define pil pair<int, ll>
#define pll pair<ll, ll>
#define vi vector<int>
#define vll vector<ll>
#define vb vector<bool>
#define vd vector<double>
#define vs vector<string>
#define ff first
#define ss second
#define pb push_back
#define eb emplace_back
#define ppb pop_back
#define pf push_front
#define ppf pop_front
#define vpii vector<pii>
#define umap unordered_map
#define all(x) x.begin(), x.end()
#define clr(a, b) memset(a, b, sizeof a)
#define fr(i, n) for (int i = 0; i < n; ++i)
#define fr1(i, n) for (int i = 1; i <= n; ++i)
#define rfr(i, n) for (int i = n - 1; i >= 0; --i)
#define precise(x) cout << fixed << setprecision(x)
typedef double f80;

const int N = 5e5 + 1, M = 1 << 20, B = 20, D = B;

vi adj[N];
int arr[N], st[N], en[N];
vi path;
int n;

struct vectorSpace
{
  typedef int base;
  int sz = 0;
  array<base, D> basis;
  vectorSpace(int _D)
  {
  }
  void insert(base mask)
  {
    if (sz == D)
      return;
    for (int i = D - 1; i >= 0; --i)
    {
      if (!((mask >> i) & 1))
        continue;
      if (!basis[i])
      {
        basis[i] = mask;
        ++sz;
        return;
      }
      mask ^= basis[i];
    }
  }
  bool represent(base mask)
  {
    if (sz == D)
      return 1;
    for (int i = D - 1; i >= 0; --i)
    {
      if (!((mask >> i) & 1))
        continue;
      if (!basis[i])
        return 0;
      mask ^= basis[i];
    }
    return 1;
  }
};

struct Segtree
{
  typedef vectorSpace base;
  typedef vectorSpace qbase;
  int L, R;
  vector<base> tree;

  inline base unite(base n1, base n2)
  {
    for (auto j : n2.basis)
    {
      n1.insert(j);
    }
    return n1;
  }

  inline void build(int st, int en, int node)
  {
    if (st == en)
    {
      tree[node] = vectorSpace(B);
      tree[node].insert(arr[path[st]]);
      return;
    }

    int mid = (st + en) >> 1, cl = (node << 1), cr = (cl | 1);

    build(st, mid, cl);
    build(mid + 1, en, cr);

    tree[node] = unite(tree[cl], tree[cr]);
  }

  Segtree(int l, int r) : L(l), R(r)
  {
    if (l > r)
      return;
    tree.resize((R - L + 1) << 2, 0);
    build(L, R, 1);
  }

  inline void update(int st, int en, int node, int idx)
  {
    if (st > idx || en < idx)
      return;

    if (st == en)
    {
      tree[node] = vectorSpace(B);
      tree[node].insert(arr[path[st]]);
      return;
    }

    int mid = (st + en) >> 1, cl = (node << 1), cr = (cl | 1);

    update(st, mid, cl, idx);
    update(mid + 1, en, cr, idx);

    tree[node] = unite(tree[cl], tree[cr]);
  }

  inline qbase query(int st, int en, int node, int l, int r)
  {
    if (st >= l && en <= r)
      return tree[node];

    int mid = (st + en) >> 1, cl = (node << 1), cr = (cl | 1);

    if (r <= mid)
      return query(st, mid, cl, l, r);
    if (l > mid)
      return query(mid + 1, en, cr, l, r);
    return unite(query(st, mid, cl, l, r), query(mid + 1, en, cr, l, r));
  }

  qbase query(int l, int r)
  {
    return query(L, R, 1, l, r);
  }

  void update(int idx)
  {
    update(L, R, 1, idx);
  }
};

inline void solve();

signed main()
{
#ifdef LOCAL
  freopen("in.txt", "r", stdin);

#else
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);
#endif

  int t = 1;

  fr1(tc, t)
  {

    solve();
  }
  return 0;
}

void dfs(int idx, int par = 0)
{
  st[idx] = path.size();
  path.pb(idx);

  for (auto i : adj[idx])
  {
    if (i == par)
      continue;
    dfs(i, idx);
  }
  en[idx] = path.size() - 1;
}

Segtree tree(0, -1);

const int mod = 1e9 + 7;

ll power(ll x, ll y, ll m)
{
  if (!y)
    return 1;
  ll p = power(x, y >> 1, m) % m;
  p = p * p % m;
  return (y & 1) ? (x * p) % m : p;
}
ll modInverse(ll a, ll m)
{
  return power(a, m - 2, m);
}

inline void solve()
{
  read(n);

  fr1(i, n)
  {
    read(arr[i]);
  }

  fr(i, n - 1)
  {
    int a, b;
    read(a, b);
    adj[a].pb(b);
    adj[b].pb(a);
  }

  dfs(1);

  tree = Segtree(0, n - 1);

  int q;
  read(q);

  while (q--)
  {
    int typ;
    read(typ);
    if (typ == 1)
    {
      int v, x;
      read(v, x);
      arr[v] = x;
      tree.update(st[v]);
      continue;
    }
    else
    {
      int v;
      read(v);
      auto res = tree.query(st[v], en[v]);
      if (!res.represent(0))
      {
        prn(0);
        continue;
      }

      ll ans = power(2, en[v] - st[v] + 1 - res.sz, mod);
      ans = (ans - 1 + mod) % mod;
      prn(ans);
    }
  }
}