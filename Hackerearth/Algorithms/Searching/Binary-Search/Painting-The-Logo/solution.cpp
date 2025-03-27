#include <bits/stdc++.h>
#define ll long long

using namespace std;

int main()
{
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);
  ll t;
  cin >> t;
  while (t--)
  {
    ll n;
    cin >> n;
    ll l = 2;
    ll h = 1e9 + 1;
    ll ans = 0;
    while (l <= h)
    {
      ll mid = (l + h) / 2;
      if (2 * mid * (mid + 1) <= n)
      {
        ans = mid;
        l = mid + 1;
      }
      else
        h = mid - 1;
    }
    if (ans == 0)
      cout << "0 0" << endl;
    else if (ans % 2)
      cout << ans << " " << ans - 1 << endl;
    else
      cout << ans - 1 << " " << ans << endl;
  }
}