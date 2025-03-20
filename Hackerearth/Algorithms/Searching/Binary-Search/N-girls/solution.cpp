#include <iostream>
#include <bits/stdc++.h>
#define ll long long
#define pb push_back
#define mp make_pair
#define ipair pair<ll int, ll int>
using namespace std;
ll int M = 1000000000000000;
ll int M1 = 1000000007;
ll int binsearch(ll int l, ll int r, ll int x, vector<ll int> &v, ll int n);

int main()
{
  ll int n, k, ans, x1, x2, i, x3, p1, q1;
  float f, f1, q, p;
  cin >> n >> k >> p1 >> q1;
  vector<ll int> v(n);
  p = min(p1, q1);
  q = max(p1, q1);
  for (i = 0; i < n; i++)
    cin >> v[i];
  ans = 1;
  sort(v.begin(), v.end());
  f = q / p;
  for (i = 0; i < n - 1; i++)
  {
    x1 = v[i];
    f1 = f * x1;
    x2 = floor(f1);
    x3 = binsearch(i + 1, n - 1, x2, v, n);
    ans = max(ans, x3 - i + 1);
  }
  if (ans + k > n)
    ans = n;
  else
    ans = ans + k;
  cout << ans << endl;
}

ll int binsearch(ll int l, ll int r, ll int x, vector<ll int> &v, ll int n)
{
  ll int m;
  while (l <= r)
  {
    m = l + (r - l) / 2;
    if (v[m] == x)
      return m;
    else if (m == n - 1 && v[m] <= x)
      return m;
    else if (v[m] > x && v[m - 1] <= x)
      return m - 1;
    else if (v[m] < x)
      l = m + 1;
    else if (v[m] > x)
      r = m - 1;
  }
}
