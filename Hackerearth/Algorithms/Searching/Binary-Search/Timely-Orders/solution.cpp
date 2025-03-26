#include <bits/stdc++.h>
#include <iostream>
#include <map>
using namespace std;
#define mod 1000000007
typedef long long ll;

int main()
{
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);
  int p;
  map<ll, ll> mp;
  unsigned long long sum = 0;
  cin >> p;
  while (p--)
  {
    int q;
    ll t, x;
    cin >> q >> x >> t;
    if (q == 1)
    {
      sum += x;
      mp[t] = sum;
    }
    else
    {
      int v = 1;
      auto it1 = mp.lower_bound(t);
      auto it2 = mp.lower_bound(t - x);
      if (it1 != mp.begin() && it2 != mp.begin())
      {
        if (it1 == mp.end() || (*it1).first != t)
          it1--;
        it2--;
        cout << (*it1).second - (*it2).second << "\n";
      }
      else if (it1 != mp.begin())
      {
        if (it1 == mp.end() || (*it1).first != t)
          it1--;
        cout << (*it1).second - 0 << "\n";
      }
      else
      {
        it2--;
        cout << (*it1).second - (*it2).second << "\n";
      }
    }
  }

  return 0;
}