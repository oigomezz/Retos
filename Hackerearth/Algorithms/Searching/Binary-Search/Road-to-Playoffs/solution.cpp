#include <bits/stdc++.h>
using namespace std;
#define FIO                         \
  ios_base::sync_with_stdio(false); \
  cin.tie(0);                       \
  cout.tie(0)
#define mod 1000000007
#define endl "\n"
#define test \
  ll t;      \
  cin >> t;  \
  while (t--)
typedef long long int ll;
bool check(vector<ll> &a, ll mid, ll n, ll m, ll k, ll p)
{
  ll total = 0;
  for (ll i = 0; i < n; i++)
  {
    if (i + 1 < p || i >= mid)
    {
      total += m;
    }
    else
    {
      if (a[i] > a[mid] + m)
      {
        return false;
      }
      total += (a[mid] + m - a[i]);
    }
  }
  return (total >= m * k);
}
int main()
{
  FIO;
  test
  {
    ll n, m, k, b;
    cin >> n >> m >> k >> b;
    vector<ll> a(n);
    for (auto &it : a)
      cin >> it;
    sort(a.begin(), a.end(), greater<ll>());
    ll ans = b, st = b, dr = n - 1;
    while (st <= dr)
    {
      ll mid = (st + dr) / 2;
      if (check(a, mid, n, m, k, b))
      {
        ans = mid + 1;
        st = mid + 1;
      }
      else
      {
        dr = mid - 1;
      }
    }
    cout << ans << endl;
  }
  return 0;
}