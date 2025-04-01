#include <bits/stdc++.h>
using namespace std;
using ll = long long;
const double sqrt2 = sqrt(2.0);

inline int read_int()
{
  int x = 0, c = getchar_unlocked();
  while (isspace(c))
    c = getchar_unlocked();
  while (isdigit(c))
    x *= 10, x += c - '0', c = getchar_unlocked();
  return x;
}

inline void write_ll(ll x)
{
  char digit[20];
  int n = 0;
  while (x > 0)
    digit[n++] = '0' + x % 10, x /= 10;
  while (n > 0)
    putchar_unlocked(digit[--n]);
}

int main()
{
  ios_base::sync_with_stdio(0), cin.tie(0);
  for (int t = read_int(); t--;)
  {
    const int n = read_int(), m = read_int();
    int a1 = INT_MAX, a2 = INT_MAX, a3 = INT_MIN, a4 = INT_MIN;
    for (int a, i = 0; i < n; ++i)
    {
      if (a = read_int(), a < a1)
        a2 = a1, a1 = a;
      if (a < a2 and a > a1)
        a2 = a;
      if (a > a4)
        a3 = a4, a4 = a;
      if (a > a3 and a < a4)
        a3 = a;
    }
    const int u = a4 - a1, v = a3 - a2, s = 1 + 2 * (u + v), d = u - v;
    write_ll(ll(s + sqrt2 * d) * m), putchar_unlocked('\n');
  }
}