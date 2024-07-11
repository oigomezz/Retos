#include <bits/stdc++.h>

#include <math.h>

using namespace std;

#define ll long long int

int main()
{

  ll n;

  cin >> n;

  set<ll> v;

  while (n--)
  {

    ll x;

    cin >> x;

    v.insert(x);

    auto it = v.lower_bound(x);

    if (it != v.begin())
    {

      cout << *(--it) << " ";
    }
    else
    {

      cout << -1 << " ";
    }

    auto it2 = v.upper_bound(x);

    if (it2 == v.end())
    {

      cout << -1 << endl;
    }
    else
    {

      cout << *it2 << endl;
    }
  }

  return 0;
}