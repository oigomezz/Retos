#include <bits/stdc++.h>
using namespace std;

#define int long long
#define inf 1e18

int f(int a, int b, int n)
{
  int op1 = n / a;
  int op2 = n / b;
  int lcm = (a * b) / __gcd(a, b);
  int op3 = n / lcm;
  return op1 + op2 - op3;
}

int32_t main()
{
  int t;
  cin >> t;
  while (t--)
  {
    int a, b, n;
    cin >> a >> b >> n;

    int i = 1;
    int j = inf;
    int ans = j;
    while (i <= j)
    {
      int mid = (i + j) / 2;
      int cnt = f(a, b, mid);
      if (cnt >= n)
      {
        j = mid - 1;
        ans = mid;
      }
      else
        i = mid + 1;
    }
    cout << ans << endl;
  }
  return 0;
}