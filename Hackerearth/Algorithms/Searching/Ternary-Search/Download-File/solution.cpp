#include <bits/stdc++.h>
using namespace std;

#define int long long int

int h[4000005];
int num, den, s, n;
long double ans = 1e18;
int lower_bound(int x)
{
  int lo = 0, hi = 4000004;
  while (lo <= hi)
  {
    int mid = (lo + hi) / 2;
    if (h[mid] <= x)
      lo = mid + 1;
    else
      hi = mid - 1;
  }
  return lo;
}
void calc(int i)
{
  int x;
  int cnt;
  if (i)
    cnt = s + h[i - 1];
  else
    cnt = s;
  x = lower_bound(cnt);
  double curr;
  if (h[x] != cnt)
  {
    curr = x - i;
    double val = (cnt - h[x - 1]);
    double y = h[x] - h[x - 1];
    if (curr + (val / y) <= ans)
    {
      ans = curr + val / y;
      int t1 = val;
      int t2 = y;
      int ans1 = curr;
      ans1 = curr * y + val;
      int g = __gcd(ans1, t2);
      ans1 /= g;
      t2 /= g;
      num = ans1, den = t2;
    }
  }
  else if (x - i + 1 < ans)
  {
    ans = x - i + 1;
    num = ans;
    den = 1;
  }
}
void calc2(int i)
{
  if (h[i] - s < 0)
    return;
  int x = lower_bound(h[i] - s);
  double curr;
  if (h[x] != h[i] - s)
  {
    curr = i - x;
    double val = h[x] - h[i] + s;
    double y;
    if (x)
      y = h[x] - h[x - 1];
    else
      y = h[x];
    if (val > y)
      cout << "wrong " << val << ' ' << y << ' ' << i << endl;
    if (curr + (val / y) < ans)
    {
      ans = curr + val / y;
      int t1 = val, t2 = y;
      int ans1 = curr * t2 + t1;
      int g = __gcd(ans1, t2);
      ans1 /= g;
      t2 /= g;
      num = ans1;
      den = t2;
    }
  }
  else if (i - x < ans)
  {
    ans = i - x;
    num = i - x;
    den = 1;
  }
}
signed main()
{
  ios_base::sync_with_stdio(false);
  cin.tie(0);
  cout.tie(0);
  cin >> n >> s;
  int a[n], b[n];
  int f = 0, sum = 0;
  for (int i = 0; i < n; i++)
  {
    cin >> a[i] >> b[i];
    sum += a[i];
    if (b[i] >= s)
    {
      f = 1;
      double val = (double)s / b[i];
      if (ans > val)
      {
        ans = val;
        int g = __gcd(s, b[i]);
        num = s / g;
        den = b[i] / g;
      }
    }
  }
  if (f)
    return cout << num << "/" << den, 0;
  for (int i = 0; i < n; i++)
    h[a[i]] = b[i];
  for (int i = 0; i < 4000005; i++)
  {
    if (h[i] == 0)
      h[i] = h[i - 1];
  }
  for (int i = 1; i < 4000005; i++)
    h[i] += h[i - 1];
  for (int i = 0; i < 2000005; i++)
  {
    calc(i);
    calc2(i);
  }
  cout << num << "/" << den;
}