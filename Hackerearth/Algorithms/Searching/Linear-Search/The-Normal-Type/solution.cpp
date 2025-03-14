#include <bits/stdc++.h>
#include <unordered_map>
using namespace std;

#define ll long long

int main()
{
  unordered_map<ll, ll> mp;
  ll n;
  cin >> n;
  ll a[n];
  for (ll i = 0; i < n; i++)
  {
    cin >> a[i];
    mp[a[i]]++;
  }

  ll dis = mp.size();
  mp.clear();
  ll low = 0, high = 0, count = 0;
  mp[a[high]]++;

  while (high < n)
  {
    if (mp.size() == dis)
    {
      count += n - high;
      if (mp[a[low]] > 1)
      {
        mp[a[low]]--;
        low++;
      }
      else
      {
        mp.erase(a[low]);
        low++;
      }
      if (low > high)
      {
        high = low;
        mp[a[high]]++;
      }
    }
    else
    {
      high++;
      mp[a[high]]++;
    }
  }

  cout << count;

  return 0;
}