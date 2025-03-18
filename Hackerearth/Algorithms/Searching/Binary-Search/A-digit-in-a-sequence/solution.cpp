#include <bits/stdc++.h>
#define int long long
using namespace std;

int a, b, k;
int n;
int x, y;
int h;
int L, R;
int m;
int len;
int i;
int l, r, c[100], LL[100];
int ans, pos, ANSWER;
int st[100], val, kol;

int f(int x)
{
  int len = 0;
  while (x > 0)
  {
    x /= 10;
    ++len;
  }
  return len;
}

void solve()
{
  memset(c, 0, sizeof c);
  cin >> a >> b >> k;
  n = 1e9;
  x = y = 0;
  h = a;
  while (h > 0)
  {
    ++x;
    h /= 10;
  }

  h = a + b * n;
  while (h > 0)
  {
    ++y;
    h /= 10;
  }

  L = 0;
  R = n;

  for (i = x; i <= y; ++i)
  {
    l = L;
    r = R;
    while (l + 1 < r)
    {
      m = (l + r) >> 1;
      if (f(a + m * b) > i)
        r = m;
      else
        l = m;
    }
    for (m = min(r + 10, R); m >= max(L, r - 10); --m)
      if (f(a + m * b) == i)
      {
        c[i] = (m - L + 1);
        LL[i] = L;
        L = m + 1;
        break;
      }
    if (L > R)
      break;
  }

  ans = 0;

  for (i = x; i <= y; ++i)
  {
    ans += c[i] * i;
    if (ans >= k)
    {
      ans -= c[i] * i;
      k -= ans;
      pos = k / i;
      if (k % i == 0)
      {
        val = a + b * (LL[i] + pos - 1);
        ANSWER = val % 10;
      }
      else
      {
        val = a + b * (LL[i] + pos);
        k %= i;
        kol = 0;
        while (val > 0)
        {
          st[++kol] = val % 10;
          val /= 10;
        }
        reverse(st + 1, st + kol + 1);
        ANSWER = st[k];
      }
      cout << ANSWER << '\n';
      return;
    }
  }

  cout << -1 << '\n';
}

main()
{
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);
  cout.tie(NULL);

  int t;
  cin >> t;
  while (t-- > 0)
    solve();

  return 0;
}