#include <iostream>
#include <map>
#include <set>
#include <algorithm>
#include <numeric>
#include <vector>
#include <cmath>
#include <cstring>
#include <queue>
#include <stack>
#include <climits>
#include <iomanip>
#define endl "\n"
using namespace std;
typedef long long int ll;
typedef pair<ll, ll> pi;
typedef vector<ll> vec;
typedef vector<vector<ll>> matrix;
ll const mod = 1000000007;
ll const N = 100100;
bool vis[N];
vec adj[N];
vec lazy(4 * N + 10, 1);
ll tr[4 * N + 10], ar[N], br[N], n, val[N], beg[N], en[N], ttm, par[N];
ll power(ll x, ll y)
{
  ll res = 1;
  while (y > 0)
  {
    if (y & 1)
      res = (res * x) % mod;
    if (res < 0)
      res += mod;
    y = y >> 1;
    x = (x * x) % mod;
    if (x < 0)
      x += mod;
  }
  res %= mod;
  if (res < 0)
    res += mod;
  return res;
}
void dfs(ll s, ll p)
{
  ttm += 1;
  val[ttm] = s;
  vis[s] = true;
  beg[s] = ttm;
  for (auto it = adj[s].begin(); it != adj[s].end(); it++)
  {
    if (*it == p)
      continue;
    if (!vis[*it])
    {
      dfs(*it, s);
    }
  }
  en[s] = ttm;
}
void build(ll node, ll low, ll high)
{
  if (low == high)
  {
    tr[node] = 1;
    return;
  }
  ll mid = (low + high) / 2;
  build(2 * node, low, mid);
  build(2 * node + 1, mid + 1, high);
  tr[node] = (tr[2 * node] + tr[2 * node + 1]) % mod;
  if (tr[node] < 0)
    tr[node] += mod;
}
void update(ll node, ll l, ll r, ll ql, ll qr, ll val)
{
  if (lazy[node] != 1)
  {
    tr[node] = (tr[node] * lazy[node]) % mod;
    if (tr[node] < 0)
      tr[node] += mod;
    if (l != r)
    {
      lazy[2 * node] = (lazy[2 * node] * lazy[node]) % mod;
      if (lazy[2 * node] < 0)
        lazy[2 * node] += mod;
      lazy[2 * node + 1] = (lazy[2 * node + 1] * lazy[node]) % mod;
      if (lazy[2 * node + 1] < 0)
        lazy[2 * node + 1] += mod;
    }
    lazy[node] = 1;
  }
  if (ql > r || qr < l)
    return;
  if (l >= ql && r <= qr)
  {
    tr[node] = (tr[node] * val) % mod;
    if (tr[node] < 0)
      tr[node] += mod;
    if (l != r)
    {
      lazy[2 * node] = (lazy[2 * node] * val) % mod;
      if (lazy[2 * node] < 0)
        lazy[2 * node] += mod;
      lazy[2 * node + 1] = (lazy[2 * node + 1] * val) % mod;
      if (lazy[2 * node + 1] < 0)
        lazy[2 * node + 1] += mod;
    }
    return;
  }
  ll mid = (l + r) / 2;
  update(2 * node, l, mid, ql, qr, val);
  update(2 * node + 1, mid + 1, r, ql, qr, val);
  tr[node] = (tr[2 * node] + tr[2 * node + 1]) % mod;
  if (tr[node] < 0)
    tr[node] += mod;
}
ll query(ll node, ll l, ll r, ll ql, ll qr)
{
  if (lazy[node] != 1)
  {
    tr[node] = (tr[node] * lazy[node]) % mod;
    if (tr[node] < 0)
      tr[node] += mod;
    if (l != r)
    {
      lazy[2 * node] = (lazy[2 * node] * lazy[node]) % mod;
      if (lazy[2 * node] < 0)
        lazy[2 * node] += mod;
      lazy[2 * node + 1] = (lazy[2 * node + 1] * lazy[node]) % mod;
      if (lazy[2 * node + 1] < 0)
        lazy[2 * node + 1] += mod;
    }
    lazy[node] = 1;
  }
  if (ql > r || qr < l)
    return 0;
  if (l >= ql && r <= qr)
    return tr[node];
  ll mid = (l + r) / 2;
  ll p1, p2;
  p1 = query(2 * node, l, mid, ql, qr);
  p2 = query(2 * node + 1, mid + 1, r, ql, qr);
  return (p1 + p2) % mod;
}
int main()
{
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);
  ll q, u, v, t, x, d;
  cin >> n >> q;
  for (ll i = 1; i < n; i++)
  {
    cin >> u >> v;
    adj[u].push_back(v);
    adj[v].push_back(u);
  }
  build(1, 1, n);
  for (ll i = 1; i <= n; i++)
  {
    cin >> ar[i];
  }
  ttm = 0;
  dfs(1, -1);
  for (ll i = 1; i <= n; i++)
    update(1, 1, n, beg[i] + 1, en[i], ar[i]);
  while (q--)
  {
    cin >> t;
    if (t == 1)
    {
      cin >> v >> x;
      d = (x * power(ar[v], mod - 2)) % mod;
      update(1, 1, n, beg[v] + 1, en[v], d);
      ar[v] = x;
    }
    else
    {
      cin >> v;
      d = query(1, 1, n, beg[v], en[v]);
      cout << d << endl;
    }
  }

  return 0;
}