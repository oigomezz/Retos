#include <iostream>
#include <algorithm>

using namespace std;

template <typename T>
inline void inp(T &n)
{
  n = 0;
  int ch = getchar_unlocked(), sign = 1;
  while (ch < '0' || ch > '9')
  {
    if (ch == '-')
      sign = -1;
    ch = getchar_unlocked();
  }
  while (ch >= '0' && ch <= '9')
    n = (n << 3) + (n << 1) + ch - '0', ch = getchar_unlocked();
  n *= sign;
}

template <typename T>
inline void puti(T n, char lc)
{
  if (0 == n)
  {
    putchar_unlocked('0');
    if (lc)
      putchar_unlocked(lc);
    return;
  }
  // bool sign = false;
  // if (n < 0) sign = true, n = -n;
  char s[20];
  int rdi = -1;
  while (n)
  {
    s[++rdi] = '0' + n % 10;
    n /= 10;
  }
  // if (sign) putchar_unlocked ('-');
  while (rdi >= 0)
    putchar_unlocked(s[rdi--]);
  if (lc)
    putchar_unlocked(lc);
}

bool cmp(pair<int, int> a, pair<int, int> b)
{
  if (a.first == b.first)
    return a.second > b.second;
  else
    return a.first < b.first;
}

int main()
{
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);
  cout.tie(NULL);
  int t, n, n2, i, a, b, c, ba, cb, p, q;
  long long count, ans;
  inp(t);
  while (t--)
  {
    inp(n);
    inp(a);
    inp(b);
    inp(c);
    ba = b - a;
    cb = c - b;
    n2 = 2 * n;
    pair<int, int> v[n2];
    for (i = 0; i < n2; i += 2)
      inp(p), inp(q), v[i] = {p, ba}, v[i + 1] = {q, cb};
    ans = 0;
    count = (long long)n * a;
    sort(v, v + n2, cmp);
    for (auto p : v)
    {
      count += p.second;
      if (count > ans)
        ans = count;
    }
    puti(ans, '\n');
  }
  return 0;
}