#include <bits/stdc++.h>
#define mod 10001
using namespace std;
typedef long long LL;
int main()
{
  int n, a[10000], avg;
  LL b[mod], val = 0, s = 0, m;
  cin >> n;
  for (int i = 0; i < n; i++)
  {
    cin >> a[i];
    s += a[i];
  }
  avg = s / n;
  b[0] = 0;
  for (int i = 0; i < n - 1; i++)
    b[i + 1] = b[i] + a[i] - avg;

  sort(b, b + n);
  m = -b[n / 2];
  for (int i = 0; i < n; i++)
    val += abs(b[i] + m);

  cout << val;
  return 0;
}