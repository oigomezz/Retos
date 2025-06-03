#include <bits/stdc++.h>

#define ll long long int
#define vi vector<ll>
#define mod 1000000007
#define vpl vector<pair<ll, ll>>
#define pb push_back

using namespace std;

ll mul(ll a, ll b)
{
  return ((a % mod) * (b % mod)) % mod;
}

vi adj[500005];
vpl v[500005];
vi lvl[500005];
ll n, m;

ll store(ll node, ll par, vi &vis)
{
  ll mx1 = 0, mx2 = 0, ind1 = -1, ind2 = -1;
  ll ht = 0;
  vis[node] = 1;
  for (auto x : adj[node])
  {
    if (x != par)
    {
      ll ret = store(x, node, vis);
      if (ret > mx1)
      {
        mx2 = mx1;
        ind2 = ind1;
        mx1 = ret;
        ind1 = x;
      }
      else if (ret > mx2)
      {
        mx2 = ret;
        ind2 = x;
      }
      ht = max(ht, ret);
    }
  }
  v[node].pb({mx1, ind1}), v[node].pb({mx2, ind2});
  return 1 + ht;
}

void help(ll node, ll par, ll id, vi &vis)
{
  if (par == 0)
  {
    lvl[id].pb(v[node][0].first);
  }
  else
  {
    ll mx = 0;
    for (auto x : v[par])
    {
      if (x.second != node && 1 + x.first > mx)
      {
        mx = 1 + x.first;
      }
    }
    v[node].pb({mx, par});
    sort(v[node].rbegin(), v[node].rend());
    lvl[id].pb(v[node][0].first);
  }
  vis[node] = 1;
  for (auto x : adj[node])
  {
    if (x != par)
    {
      help(x, node, id, vis);
    }
  }
}

int main()
{
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);

#ifndef ONLINE_JUDGE
  freopen("input.txt", "r", stdin);
  freopen("output.txt", "w", stdout);
#endif

  ll t = 1;
  cin >> t;

  while (t--)
  {
    cin >> n >> m;
    for (ll i = 0; i <= n; i++)
    {
      adj[i].clear();
      v[i].clear();
      lvl[i].clear();
    }
    ll u, v;
    for (ll i = 0; i < m; i++)
    {
      cin >> u >> v;
      adj[u].pb(v), adj[v].pb(u);
    }
    vi vis(n + 1, 0);
    for (ll i = 1; i <= n; i++)
    {
      if (vis[i] == 0)
      {
        store(i, 0, vis);
      }
    }
    vi vis1(n + 1, 0);
    ll id = 0;
    for (ll i = 1; i <= n; i++)
    {
      if (vis1[i] == 0)
      {
        help(i, 0, id, vis1);
        id++;
      }
    }
    ll mx = 0;
    for (ll i = 0; i < id; i++)
    {
      sort(lvl[i].begin(), lvl[i].end());
      mx = max(mx, lvl[i][0]);
    }
    ll ans = 1;
    for (ll i = 0; i < id; i++)
    {
      ans = mul(ans, upper_bound(lvl[i].begin(), lvl[i].end(), mx) - lvl[i].begin());
    }
    cout << ans << "\n";
  }
}