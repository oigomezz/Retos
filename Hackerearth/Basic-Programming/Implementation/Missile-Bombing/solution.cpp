#include <bits/stdc++.h>
using namespace std;

int main()
{

  long long n;
  long long m;
  cin >> n >> m;
  long long arr[n + 1][n + 1] = {0};

  while (m--)
  {
    long long p, a, b, c, d;
    cin >> p >> a >> b >> c >> d;
    long long range1 = 0, range2 = 0;
    range1 = (c - a);
    range2 = (d - b);
    for (long i = a; i <= (a + range1); i++)
    {
      for (long j = b; j <= (b + range2); j++)
      {
        arr[i][j] = (arr[i][j] ^ p);
      }
    }
  }

  for (long i = 1; i <= n; i++)
  {
    for (long j = 1; j <= n; j++)
    {
      cout << arr[i][j] << " ";
    }
    cout << endl;
  }

  return 0;
}