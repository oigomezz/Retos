#include <bits/stdc++.h>

#define ll long long
#define uint unsigned

#define debug(...) fprintf(stderr, __VA_ARGS__)

#define SZ(x) ((int)(x).size())
#define pb push_back

#define pii std::pair<int, int>
#define mp std::make_pair
#define fi first
#define se second

template <class T>
inline void chkmax(T &x, const T &y)
{
  if (x < y)
    x = y;
}
template <class T>
inline void chkmin(T &x, const T &y)
{
  if (y < x)
    x = y;
}

template <class T>
inline void read(T &x)
{
  char c;
  int f = 1;
  x = 0;
  while (((c = getchar()) < '0' || c > '9') && c != '-')
    ;
  if (c == '-')
    f = -1;
  else
    x = c - '0';
  while ((c = getchar()) >= '0' && c <= '9')
    x = x * 10 + c - '0';
  x *= f;
}

const int N = 1e5;
const int MOD = 1e9 + 7;

int n;
char s[N + 9];

int sa[N + 9], rk[N + 9], h[N + 9], t1[N + 9], t2[N + 9], c[N + 9];

void array()
{
  int m = 0, *x = t1, *y = t2;
  for (int i = 1; i <= n; ++i)
    chkmax(m, x[i] = s[i] - 'a' + 1);

  std::fill(c + 1, c + m + 1, 0);
  for (int i = 1; i <= n; ++i)
    c[x[i]]++;
  for (int i = 1; i <= m; ++i)
    c[i] += c[i - 1];
  for (int i = n; i >= 1; --i)
    sa[c[x[i]]--] = i;
  for (int k = 1; k <= n; k <<= 1)
  {
    int p = 0;
    for (int i = n - k + 1; i <= n; ++i)
      y[++p] = i;
    for (int i = 1; i <= n; ++i)
      if (sa[i] > k)
        y[++p] = sa[i] - k;

    std::fill(c + 1, c + m + 1, 0);
    for (int i = 1; i <= n; ++i)
      c[x[y[i]]]++;
    for (int i = 1; i <= m; ++i)
      c[i] += c[i - 1];
    for (int i = n; i >= 1; --i)
      sa[c[x[y[i]]]--] = y[i];

    std::swap(x, y), x[sa[1]] = p = 1;
    for (int i = 2; i <= n; ++i)
    {
      if (!(sa[i] + k <= n && sa[i - 1] + k <= n && y[sa[i]] == y[sa[i - 1]] && y[sa[i] + k] == y[sa[i - 1] + k]))
        ++p;
      x[sa[i]] = p;
    }
    if (p >= n)
      break;
    m = p;
  }
}

void height()
{
  for (int i = 1; i <= n; ++i)
    rk[sa[i]] = i;
  for (int i = 1, k = 0; i <= n; ++i)
  {
    if (k)
      k--;
    if (rk[i] == 1)
    {
      h[1] = 0;
      continue;
    }
    int j = sa[rk[i] - 1];
    while (s[i + k] == s[j + k])
      ++k;
    h[rk[i]] = k;
  }
}

void suffix()
{
  array(), height();
}

void solve()
{
  static int st[N + 9], stn, l[N + 9], r[N + 9], pre[N + 9];
  st[stn = 1] = 1, h[1] = -1;
  for (int i = 2; i <= n; ++i)
  {
    while (stn && h[st[stn]] >= h[i])
      r[st[stn--]] = i - 1;
    l[i] = st[stn], st[++stn] = i;
  }
  while (stn)
    r[st[stn--]] = n;
  for (int i = 1; i <= n; ++i)
    pre[i] = (pre[i - 1] + sa[i]) % MOD;
  int ans = 0;
  for (int i = 2; i <= n; ++i)
  {
    int pn = (ll)(i - l[i]) * (r[i] - i + 1) % MOD, x = h[i], x2 = (ll)x * (x + 1) / 2 % MOD, x3 = (ll)x * (x + 1) * (2 * x + 1) / 3 % MOD;
    (ans += ((2ll * n + 3) * x2 % MOD * pn % MOD - (ll)x3 * pn % MOD - (ll)x2 * ((ll)(r[i] - i + 1) * (pre[i - 1] - pre[l[i] - 1]) % MOD + (ll)(i - l[i]) * (pre[r[i]] - pre[i - 1]) % MOD) % MOD) % MOD) %= MOD;
    (ans += (ll)x * ((ll)(i - l[i]) * (n - x + 1) % MOD - (pre[i - 1] - pre[l[i] - 1])) % MOD * ((ll)(r[i] - i + 1) * (n - x + 1) % MOD - (pre[r[i]] - pre[i - 1])) % MOD) %= MOD;
  }
  (ans <<= 1) %= MOD;
  for (int i = 1; i <= n; ++i)
    (ans += ((ll)-i * (i + 1) * (2 * i + 1) / 6 + (ll)i * (i + 1) / 2 * (2 * i + 1)) / 2 % MOD) %= MOD;
  ans = (ans + MOD) % MOD;
  printf("%d\n", ans);
}

int main()
{
  int T;
  read(T);
  while (T--)
  {
    read(n);
    scanf("%s", s + 1);
    suffix(), solve();
  }
  return 0;
}