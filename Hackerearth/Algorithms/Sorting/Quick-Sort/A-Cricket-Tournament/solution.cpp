#include <bits/stdc++.h>
using namespace std;
#define int long long int

int32_t main()
{
  ios::sync_with_stdio(false);
  cin.tie(0);
  cout.tie(0);
  int n = 0;
  cin >> n;
  vector<int> a(n), b(n);
  for (int i = 0; i < n; i++)
  {
    cin >> a[i];
  }
  for (int i = 0; i < n; i++)
  {
    cin >> b[i];
  }
  sort(a.begin(), a.end());
  sort(b.begin(), b.end());
  reverse(b.begin(), b.end());
  int ans = 0;
  for (int i = 0; i < n; i++)
  {
    if (a[i] > b[i])
    {
      ans += (a[i] - b[i]);
    }
  }
  cout << ans;
  return 0;
}