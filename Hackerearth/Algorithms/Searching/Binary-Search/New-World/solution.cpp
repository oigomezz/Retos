#include <bits/stdc++.h>
using namespace std;
int main()
{
  int t;
  cin >> t;
  while (t--)
  {
    int n, k;
    cin >> n >> k;
    int a[n];
    for (int i = 0; i < n; i++)
      cin >> a[i];
    int ans = -1;
    int l = 0;
    int r = INT_MAX;
    while (l <= r)
    {
      int mid = l + (r - l) / 2;
      int c = 1;
      int s = 0;
      for (int i = 1; i < n; i++)
      {
        s += a[i] - a[i - 1];
        if (s > mid)
        {
          s = a[i] - a[i - 1];
          if (s > mid)
          {
            c = INT_MAX;
            break;
          }
          c++;
        }
      }
      if (c <= k)
      {
        ans = mid;
        r = mid - 1;
      }
      else
        l = mid + 1;
    }
    cout << ans << endl;
  }
}