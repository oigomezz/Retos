#include <bits/stdc++.h>
using namespace std;
#define ios                     \
  ios_base::sync_with_stdio(0); \
  cin.tie(0);                   \
  cout.tie(0)
#define scn(n) scanf("%d", &n)
#define lscn(n) scanf("%lld", &n)
#define rep(i, st, n) for (int i = st; i < n; i++)
typedef long long ll;
#define pri(n) printf("%d\n", n)
#define lpri(n) printf("%lld\n", n)
#define var(n) \
  int n;       \
  scn(n)
#define all(x) (x).begin(), (x).end()
#define pb(n) push_back(n)
#define pii pair<int, int>
#define F first
#define S second
const int N = 3e5 + 5;
const ll M = 1e9 + 7;

vector<int> g[N];
vector<pair<ll, ll>> vp(N);

void dfs(int node, int par)
{
  int child = 0;
  int mx = 0, nmx = 0;
  for (int it : g[node])
  {
    if (it != par)
    {
      child++;
      dfs(it, node);
      if (vp[it].F > mx)
      {
        mx = vp[it].F;
        nmx = vp[it].S;
      }
      else if (vp[it].F == mx)
        nmx += vp[it].S;
    }
  }
  if (child == 0)
  {
    vp[node] = {1, 1};
  }
  else
  {
    vp[node] = {mx + 1, nmx};
  }
}

void dfs_ans(int node, int par, int up, ll cnt)
{
  vector<pair<ll, ll>> vpr;
  for (int it : g[node])
  {
    if (it != par)
    {
      vpr.push_back(vp[it]);
    }
  }

  vpr.push_back({up, cnt});
  sort(vpr.rbegin(), vpr.rend());

  pair<ll, ll> cur = {0, 0};
  int Case = 0;
  ll sum = 0, prod = 0;
  int sz = vpr.size();
  if (sz == 0)
  {
    cur = {1, 1};
  }
  else if (sz == 1)
  {
    cur = vpr[0];
    cur.F++;
    Case = 4;
  }
  else
  {
    if (vpr[0].F == vpr[1].F)
    {
      Case = 1;
      int pos = 1;
      while (pos + 1 < sz and vpr[pos + 1].F == vpr[pos].F)
        pos++;

      sum = 0, prod = 0;
      for (int i = 0; i <= pos; i++)
      {
        prod += sum * vpr[i].S;
        sum += vpr[i].S;
      }
      cur = {vpr[0].F * 2 + 1, prod};
    }
    else if (sz > 2 and vpr[1].F == vpr[2].F)
    {
      Case = 2;
      int pos = 2;
      while (pos + 1 < sz and vpr[pos + 1].F == vpr[pos].F)
        pos++;
      sum = 0;
      for (int i = 1; i <= pos; i++)
        sum += vpr[i].S;
      cur = {vpr[0].F + vpr[1].F + 1, sum * vpr[0].S};
    }
    else
    {
      Case = 3;
      cur = {vpr[0].F + vpr[1].F + 1, vpr[0].S * vpr[1].S};
    }
  }

  vp[node] = cur;

  for (int it : g[node])
  {
    if (it != par)
    {
      if (Case == 4)
      {
        dfs_ans(it, node, 1, 1);
      }
      else if (Case == 3)
      {
        if (vp[it] == vpr[0])
          dfs_ans(it, node, vpr[1].F + 1, vpr[1].S);
        else
          dfs_ans(it, node, vpr[0].F + 1, vpr[0].S);
      }
      else if (Case == 2)
      {
        if (vp[it] == vpr[0])
        {
          dfs_ans(it, node, vpr[1].F + 1, sum);
        }
        else
        {
          dfs_ans(it, node, vpr[0].F + 1, vpr[0].S);
        }
      }
      else if (Case == 1)
      {
        if (vp[it].F == vpr[0].F)
          dfs_ans(it, node, vpr[0].F + 1, sum - vp[it].S);
        else
          dfs_ans(it, node, vpr[0].F + 1, sum);
      }
    }
  }
}

int main()
{
  ios;
  int n, x, y;
  cin >> n;
  for (int i = 0; i < n - 1; i++)
  {
    cin >> x >> y;
    g[x].push_back(y);
    g[y].push_back(x);
  }
  dfs(1, -1);

  dfs_ans(1, -1, 0, 1);

  for (int i = 1; i <= n; i++)
    cout << vp[i].F << ' ' << vp[i].S << "\n";
}