#include <bits/stdc++.h>
using namespace std;

#define ll long long

bool check(ll mid, ll d, ll a, ll m, ll b, ll x)
{
  ll totalCycle = mid / (m + 1);
  ll totalRemainingMonth = mid % (m + 1);
  ll totalAmountInOneCycle = (m * a) + b;
  x = x - d;
  x = x - totalAmountInOneCycle * totalCycle;
  x = x - (totalRemainingMonth * a);
  return x <= 0;
}

int main()
{

  int t;
  cin >> t;
  while (t--)
  {
    ll d, a, m, b, x;
    cin >> d >> a >> m >> b >> x;
    ll low = 0, high = 1e9;
    ll ans = -1;
    while (low <= high)
    {
      ll mid = (low + high) / 2;
      if (check(mid, d, a, m, b, x))
      {
        ans = mid;
        high = mid - 1;
      }
      else
        low = mid + 1;
    }

    cout << ans << endl;
  }

  return 0;
}