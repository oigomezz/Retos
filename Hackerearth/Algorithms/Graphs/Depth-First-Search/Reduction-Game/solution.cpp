#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
const int M = 1e4 + 239;
const int B = 30;
int n, a[M];
ll c1, c2;
bool used[M];
map<int, int> id;
void dfs(int p)
{
  used[p] = true;
  for (int i = 0; i < B; i++)
  {
    int r = (1 << i) ^ a[p];
    if (id.find(r) == id.end())
      continue;
    r = id[r];
    if (!used[r])
      dfs(r);
  }
}
void dfs2(int p)
{
  used[p] = true;
  for (int i = 0; i < n; i++)
    if (!used[i] && __builtin_popcount(a[i] ^ a[p]) > 1)
      dfs2(i);
}
void solve()
{
  cin >> n >> c1 >> c2;
  for (int i = 0; i < n; i++)
    cin >> a[i];
  sort(a, a + n);
  if (c2 <= c1)
  {
    if (n > 60)
    {
      cout << (ll)c2 * (ll)(n - 1) << "\n";
      return;
    }
    for (int i = 0; i < n; i++)
      used[i] = false;
    ll w = -1;
    for (int i = 0; i < n; i++)
      if (!used[i])
      {
        w++;
        dfs2(i);
      }
    cout << w * (ll)c1 + (ll)(n - 1 - w) * (ll)c2 << "\n";
    return;
  }
  id.clear();
  for (int i = 0; i < n; i++)
    id[a[i]] = i;
  for (int i = 0; i < n; i++)
    used[i] = false;
  ll w = -1;
  for (int i = 0; i < n; i++)
    if (!used[i])
    {
      w++;
      dfs(i);
    }
  cout << w * (ll)c2 + (ll)(n - 1 - w) * (ll)c1 << "\n";
}
int main()
{
  ios::sync_with_stdio(0);
  cin.tie(0);
  cout.tie(0);
  int T;
  cin >> T;
  while (T--)
    solve();
  return 0;
}