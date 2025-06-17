#include <bits/stdc++.h>

using namespace std;

typedef long double ld;

const ld PI = acos(-1);
const int MAX = 1 << 18;
const int MOD = 1e9 + 7;

int bigMod(int a, int e)
{
  if (e == -1)
    e = MOD - 2;
  int ret = 1;
  while (e)
  {
    if (e & 1)
      ret = ret * 1LL * a % MOD;
    a = a * 1LL * a % MOD, e >>= 1;
  }
  return ret;
}

int fac[MAX], inv[MAX];

namespace FFT
{
  struct cp
  {
    ld x, y;

    cp(ld x = 0, ld y = 0) : x(x), y(y) {}

    cp operator+(const cp &rhs) const { return cp(x + rhs.x, y + rhs.y); }
    cp operator-(const cp &rhs) const { return cp(x - rhs.x, y - rhs.y); }
    cp operator*(const cp &rhs) const { return cp(x * rhs.x - y * rhs.y, x * rhs.y + y * rhs.x); }
    cp operator!() const { return cp(x, -y); }
  };

  cp rts[MAX + 1];
  int bitrev[MAX];
  cp f_a[MAX], f_b[MAX];
  cp f_c[MAX], f_d[MAX];

  void fft_init()
  {
    int k = 0;
    while (1 << k < MAX)
      ++k;
    bitrev[0] = 0;
    for (int i = 1; i < MAX; ++i)
    {
      bitrev[i] = bitrev[i >> 1] >> 1 | ((i & 1) << k - 1);
    }
    rts[0] = rts[MAX] = cp(1, 0);
    for (int i = 1; i + i <= MAX; ++i)
    {
      rts[i] = cp(cos(i * 2 * PI / MAX), sin(i * 2 * PI / MAX));
    }
    for (int i = MAX / 2 + 1; i < MAX; ++i)
    {
      rts[i] = !rts[MAX - i];
    }
  }

  void dft(cp a[], int n, int sign)
  {
    static int is_init;
    if (!is_init)
      is_init = 1, fft_init();
    int d = 0;
    while ((1 << d) * n != MAX)
      ++d;
    for (int i = 0; i < n; ++i)
    {
      if (i < bitrev[i] >> d)
        swap(a[i], a[bitrev[i] >> d]);
    }
    for (int len = 2; len <= n; len <<= 1)
    {
      int delta = MAX / len * sign;
      for (int i = 0; i < n; i += len)
      {
        cp *x = a + i, *y = a + i + (len >> 1), *w = sign > 0 ? rts : rts + MAX;
        for (int k = 0; k + k < len; ++k)
        {
          cp z = *y * *w;
          *y = *x - z, *x = *x + z;
          ++x, ++y, w += delta;
        }
      }
    }
    if (sign < 0)
      for (int i = 0; i < n; ++i)
        a[i].x /= n, a[i].y /= n;
  }

  void multiply(int a[], int b[], int n_a, int n_b, long long c[])
  {
    int n = n_a + n_b - 1;
    while (n != n & -n)
      n += n & -n;
    for (int i = 0; i < n; ++i)
      f_a[i] = f_b[i] = cp();
    for (int i = 0; i < n_a; ++i)
      f_a[i] = cp(a[i]);
    for (int i = 0; i < n_b; ++i)
      f_b[i] = cp(b[i]);
    dft(f_a, n, 1), dft(f_b, n, 1);
    for (int i = 0; i < n; ++i)
      f_a[i] = f_a[i] * f_b[i];
    dft(f_a, n, -1);
    for (int i = 0; i < n; ++i)
      c[i] = (long long)floor(f_a[i].x + 0.5);
  }

  void multiply(int a[], int b[], int n_a, int n_b, int c[])
  {
    int n = n_a + n_b - 1;
    while (n != (n & -n))
      n += n & -n;
    for (int i = 0; i < n; ++i)
      f_a[i] = f_b[i] = cp();
    static const int MAGIC = 15;
    for (int i = 0; i < n_a; ++i)
      f_a[i] = cp(a[i] >> MAGIC, a[i] & (1 << MAGIC) - 1);
    for (int i = 0; i < n_b; ++i)
      f_b[i] = cp(b[i] >> MAGIC, b[i] & (1 << MAGIC) - 1);
    dft(f_a, n, 1), dft(f_b, n, 1);
    for (int i = 0; i < n; ++i)
    {
      int j = (n - i) % n;
      cp x = f_a[i] + !f_a[j];
      cp y = f_b[i] + !f_b[j];
      cp z = !f_a[j] - f_a[i];
      cp t = !f_b[j] - f_b[i];
      f_c[i] = (x * t + y * z) * cp(0, 0.25);
      f_d[i] = x * y * cp(0, 0.25) + z * t * cp(-0.25, 0);
    }
    dft(f_c, n, -1), dft(f_d, n, -1);
    for (int i = 0; i < n; ++i)
    {
      long long u = ((long long)floor(f_c[i].x + 0.5)) % MOD;
      long long v = ((long long)floor(f_d[i].x + 0.5)) % MOD;
      long long w = ((long long)floor(f_d[i].y + 0.5)) % MOD;
      c[i] = ((u << 15) + v + (w << 30)) % MOD;
    }
  }

  vector<int> multiply(vector<int> a, vector<int> b)
  {
    static int f_a[MAX], f_b[MAX], f_c[MAX];
    int n_a = a.size(), n_b = b.size();
    for (int i = 0; i < n_a; ++i)
      f_a[i] = a[i];
    for (int i = 0; i < n_b; ++i)
      f_b[i] = b[i];
    multiply(f_a, f_b, n_a, n_b, f_c);
    int k = n_a + n_b - 1;
    vector<int> res(k);
    for (int i = 0; i < k; ++i)
      res[i] = f_c[i];
    return res;
  }

  vector<int> extend(vector<int> a, int c)
  {
    a.insert(a.begin(), 0);
    for (int i = 0; i < (int)a.size() - 1; ++i)
    {
      int add = c * 1LL * a[i + 1] % MOD;
      a[i] -= add;
      if (a[i] < 0)
        a[i] += MOD;
    }
    return a;
  }

  vector<int> falling_factorial(int n)
  {
    if (!n)
      return {1};
    int m = n >> 1;
    if (n & 1)
      return extend(falling_factorial(n - 1), n - 1);
    vector<int> left = falling_factorial(m);
    vector<int> one(m + 1), two(m + 1), right(m + 1);
    for (int i = 0; i <= m; ++i)
      one[i] = bigMod(MOD - m, i) * 1LL * inv[i] % MOD;
    for (int i = 0; i <= m; ++i)
      two[i] = left[m - i] * 1LL * fac[m - i] % MOD;
    vector<int> three = multiply(one, two);
    for (int i = 0; i <= m; ++i)
      right[i] = three[m - i] * 1LL * inv[i] % MOD;
    return multiply(left, right);
  }

  int dot(vector<int> a, vector<int> b)
  {
    int res = 0;
    for (int i = 0; i < (int)min(a.size(), b.size()); ++i)
    {
      int add = a[i] * 1LL * b[i] % MOD;
      res += add;
      if (res >= MOD)
        res -= MOD;
    }
    return res;
  }
}

int main()
{
  fac[0] = 1;
  for (int i = 1; i < MAX; ++i)
    fac[i] = i * 1LL * fac[i - 1] % MOD;
  inv[MAX - 1] = bigMod(fac[MAX - 1], -1);
  for (int i = MAX - 1; i; --i)
    inv[i - 1] = i * 1LL * inv[i] % MOD;
  int n, l, r;
  scanf("%d %d %d", &n, &l, &r);
  vector<int> a(n + 1);
  for (int i = 1; i <= n; ++i)
    scanf("%d", &a[i]);
  vector<int> poly = FFT::falling_factorial(l - 1);
  int last = FFT::dot(a, poly);
  for (int it = l; it <= r; ++it)
  {
    poly = FFT::extend(poly, it - 1);
    int cur = FFT::dot(a, poly);
    int ans = cur - last;
    if (ans < 0)
      ans += MOD;
    if (it > l)
      printf(" ");
    printf("%d", ans);
    last = cur;
  }
  puts("");
  return 0;
}