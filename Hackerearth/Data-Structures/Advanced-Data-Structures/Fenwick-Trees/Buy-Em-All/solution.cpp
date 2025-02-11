#include <bits/stdc++.h>

using namespace std;

typedef complex<double> base;
typedef long double ld;
typedef long long ll;

#define pb push_back

const int LN = 18, maxn = (1 << LN);
ll a[maxn], pre[maxn];
const ll mod = (ll)(1e9 + 7);

int main()
{
  ios_base::sync_with_stdio(0);

  int n;
  ll k;
  cin >> n >> k;
  assert(n >= 1 && n <= (int)(2e5));
  assert(k >= 0 && k <= (ll)(1e18));

  for (int i = 1; i <= n; i++)
  {
    cin >> a[i];
    assert(a[i] >= 0 && a[i] <= (ll)(1e6));
  }

  for (int i = n - 1; i >= 1; i--)
  {
    pre[i] = pre[i + 2] + (a[i] * a[i + 1]);
  }

  ll res = 0;
  for (int i = n - 1; i >= 1; i--)
  {
    int low = 1, high = (n - i + 1) / 2;
    while (low < high)
    {
      int mid = (low + high + 1) >> 1;
      ll now = pre[i] - pre[i + (mid * 2)];
      if (now <= k)
      {
        low = mid;
      }
      else
      {
        high = mid - 1;
      }
    }

    if (pre[i] - pre[i + (low * 2)] <= k)
    {
      res += low;
    }
  }

  for (int i = n; i >= 1; i--)
  {
    ll now = k - a[i];
    if (now >= 0)
    {
      int low = 0, high = (i - 1) / 2;
      while (low < high)
      {
        int mid = (low + high + 1) >> 1;
        ll zz = pre[i - (mid * 2)] - pre[i];
        if (zz <= now)
        {
          low = mid;
        }
        else
        {
          high = mid - 1;
        }
      }

      if (pre[i - (low * 2)] - pre[i] <= now)
      {
        res += (low + 1);
      }
    }
  }

  cout << res << endl;
  return 0;
}