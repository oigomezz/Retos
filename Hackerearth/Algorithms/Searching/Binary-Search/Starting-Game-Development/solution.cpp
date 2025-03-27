#include <bits/stdc++.h>
using namespace std;
#define MOD 1000000007
#define ll long long int

long long int fast_pow(long long base, long long n, long long M)
{
  if (n == 0)
    return 1;
  if (n == 1)
    return base;
  long long halfn = fast_pow(base, n / 2, M);
  if (n % 2 == 0)
    return (halfn * halfn) % M;
  else
    return (((halfn * halfn) % M) * base) % M;
}

long long int fermat(long long int n, long long int M)
{
  return fast_pow(n, M - 2, M);
}

long long int gcd(long long int a, long long int b)
{
  if (b == 0)
    return a;
  return gcd(b, a % b);
}

void NcR(int n, int r)
{
  long long p = 1, k = 1;
  if (n - r < r)
    r = n - r;
  if (r != 0)
  {
    while (r)
    {
      p *= n;
      k *= r;

      long long m = gcd(p, k);

      p /= m;
      k /= m;

      n--;
      r--;
    }
  }

  else
    p = 1;
}

long long int min(long long int a, long long int b)
{
  if (a < b)
    return a;
  return b;
}

int main()
{
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);
  ll n, m, q, a, x, y;
  vector<ll> v[n + 1];
  cin >> n >> m >> q;
  for (int i = 0; i < n; i++)
  {
    for (int j = 0; j < m; j++)
    {
      cin >> a;
      v[i].push_back(a);
    }
    sort(v[i].begin(), v[i].end());
  }

  while (q--)
  {
    ll lvl = 9999999999;
    for (int i = 0; i < n; i++)
    {
      cin >> x;
      lvl = min(lvl, upper_bound(v[i].begin(), v[i].end(), x) - v[i].begin());
    }
    if (lvl == m + 1)
      lvl--;

    cout << lvl << endl;
  }
}