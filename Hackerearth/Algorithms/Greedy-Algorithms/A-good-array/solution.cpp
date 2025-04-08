#include <bits/stdc++.h>
using namespace std;

#define pb push_back
#define fast ios_base::sync_with_stdio(false), cin.tie(NULL)

typedef long long int ll;
typedef vector<int> vi;

int main()
{
  fast;
  ll tc, n, i, j, k, a;
  cin >> tc;
  while (tc--)
  {
    ll x, y;
    cin >> n >> x >> y;
    vi v;
    for (i = 0; i < n; i++)
    {
      cin >> a;
      v.pb(a);
    }
    ll cnt0 = 0, cnt1 = 0;
    for (i = 0; i < n; i++)
    {
      if (i % 2 == 0 && v[i] == 0)
        cnt1++;
      else if (i % 2 != 0 && v[i] == 1)
        cnt0++;
    }
    ll ans = cnt1 * x + cnt0 * y;
    cnt0 = 0, cnt1 = 0;
    for (i = 0; i < n; i++)
    {
      if (i % 2 == 0 && v[i] == 1)
        cnt1++;
      else if (i % 2 != 0 && v[i] == 0)
        cnt0++;
    }
    cout << min(ans, cnt1 * y + cnt0 * x) << endl;
  }

  return 0;
}