#include <bits/stdc++.h>
using namespace std;

typedef long long ll;
typedef long double ld;
const int maxn = 1e5 + 17;
ld fen[maxn], a[maxn];

void upd(int p, ld x)
{
  for (p++; p < maxn; p += p & -p)
    fen[p] += x;
}

ld get(int p)
{
  ld ans = 0;
  for (; p; p ^= p & -p)
    ans += fen[p];
  return ans;
}

int n, m;
int main()
{
  ios::sync_with_stdio(0), cin.tie(0);
  cin >> n >> m;
  ld s = 0;
  for (int i = 0; i < n; i++)
  {
    ll x;
    cin >> x;
    upd(i, log(x));
    s += log(x);
  }
  while (m--)
  {
    int t;
    cin >> t;
    if (t == 1)
    {
      int i;
      ll x;
      cin >> i >> x;
      i--;
      upd(i, log(x));
      s += log(x);
    }
    else
    {
      int lo = -1, hi = n;
      auto f = [&s](int i)
      {
        return abs(get(i + 1) - (s - get(i + 1)));
      };
      while (hi - lo > 2)
      {
        int lh = lo + (hi - lo) / 3, rh = hi - (hi - lo) / 3;
        if (f(rh) >= f(lh))
          hi = rh;
        else
          lo = lh;
      }
      cout << lo + 2 << '\n';
    }
  }
}