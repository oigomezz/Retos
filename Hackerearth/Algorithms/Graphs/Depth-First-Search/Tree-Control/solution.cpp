#include <bits/stdc++.h>
using namespace std;

#define boost ios_base::sync_with_stdio(0), cin.tie(0), cout.tie(0)
#define li long long int
#define mod 1000000007

li D = 20;
li n, a[200005];
vector<li> g[200005];
li par[200005][22];
li w[200005];
li dep[200005];
li sum[200005];
void dfs(li s, li pr, li d)
{
  par[s][0] = pr;
  dep[s] = d;
  sum[s] = 1;
  for (auto i : g[s])
  {
    dfs(i, s, d + w[i]);
  }
}
void SetTable()
{
  for (li i = 1; i <= 20; i++)
  {
    for (li j = 1; j <= n; j++)
    {
      par[j][i] = par[par[j][i - 1]][i - 1];
    }
  }
}
void upd(li s, li val)
{
  for (li d = D; d >= 0; d--)
  {
    if (dep[par[s][d]] >= val)
    {
      s = par[s][d];
    }
  }
  if (s == 1)
    return;
  s = par[s][0];
  sum[s]--;
}
void go(li s)
{
  if (s != 1)
  {
    upd(s, dep[s] - a[s]);
  }
  for (auto i : g[s])
  {
    go(i);
    sum[s] += sum[i];
  }
}
int main()
{

  boost;
  cin >> n;
  for (li i = 1; i <= n; i++)
    cin >> a[i];

  for (li i = 2; i <= n; i++)
  {
    li x, y;
    cin >> x;
    g[x].push_back(i);
  }

  for (li i = 2; i <= n; i++)
  {
    li x, y;
    cin >> y;
    w[i] = y;
  }

  dfs(1, 1, 0);
  SetTable();
  go(1);
  for (li i = 1; i <= n; i++)
    cout << sum[i] - 1 << " ";
  return 0;
}