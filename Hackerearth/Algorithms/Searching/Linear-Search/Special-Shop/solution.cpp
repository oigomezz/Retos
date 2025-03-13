#include <bits/stdc++.h>
using namespace std;

typedef long long ll;

int main()
{

  ll t, n, a, b;
  cin >> t;
  while (t--)
  {
    cin >> n >> a >> b;
    ll X, Y, res1, res2, res3, result;
    X = (b * n) / (a + b);
    Y = n - X;
    res1 = X * X * a + (n - X) * (n - X) * b;
    X++;

    res2 = X * X * a + (n - X) * (n - X) * b;
    X -= 2;

    res3 = X * X * a + (n - X) * (n - X) * b;
    result = min(res1, res2);
    result = min(result, res3);
    cout << result << endl;
  }
}