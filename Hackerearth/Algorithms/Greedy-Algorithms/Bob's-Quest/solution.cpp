#include <bits/stdc++.h>
using namespace std;

typedef long long ll;

int main()
{
  ll t;
  cin >> t;
  while (t--)
  {
    ll n, x, y;
    cin >> n >> x >> y;
    vector<ll> a(n);
    for (ll i = 0; i < n; i++)
      cin >> a[i];
    ll l = 0, r = 0;
    unordered_map<ll, ll> mp;
    ll cnt = 0, maxi = 0;
    bool flag = false;
    while (r < n)
    {
      if (mp[a[r]] == 0)
        cnt++;
      while (cnt > x)
      {
        mp[a[l]]--;
        if (mp[a[l]] == 0)
          cnt--;
        if (a[l] == y && mp[a[l]] == 0)
          flag = false;
        l++;
      }
      if (a[r] == y)
        flag = true;
      if (cnt == x && flag == true)
        maxi = max(maxi, r - l + 1);
      mp[a[r]]++;
      r++;
    }
    cout << maxi << endl;
  }
  return 0;
}