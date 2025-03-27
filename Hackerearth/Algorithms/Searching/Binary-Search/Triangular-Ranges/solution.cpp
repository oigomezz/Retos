#include <bits/stdc++.h>
#define ll long long

using namespace std;

int main()
{
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);
  vector<ll> a(2e6 + 1, 0);
  for (ll i = 0; i < 2e6 + 1; i++)
    a[i] = (i * (i + 1)) / 2;

  ll q;
  cin >> q;
  while (q--)
  {
    ll l, r;
    cin >> l >> r;
    ll cnt = 0;
    ll rep = 0;
    for (int i = 1; i < a.size() && a[i] < r; i++)
    {
      ll x = a[i];
      ll pos = upper_bound(a.begin(), a.end(), r - x) - lower_bound(a.begin() + 1, a.end(), l - x);
      if (2 * a[i] >= l && 2 * a[i] <= r)
      {
        rep++;
        pos--;
      }
      cnt += pos;
    }
    cout << cnt / 2 + rep << endl;
  }
}