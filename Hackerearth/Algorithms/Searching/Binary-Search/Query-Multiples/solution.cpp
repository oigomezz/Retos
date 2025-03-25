#include <bits/stdc++.h>
using namespace std;

#define pb push_back
typedef array<int, 2> aii;

int main()
{
  cin.tie(0), cout.tie(0);
  ios_base::sync_with_stdio(0);
  cout.setf(ios::fixed);
  cout.precision(10);
  int n, m, k, q;

  cin >> n >> q;
  int arr[n + 1];
  for (int i = 1; i <= n; i++)
    cin >> arr[i];

  int fcnt[20001] = {};
  vector<aii> vec[n + 1];
  for (int l = 0; l < q; l++)
  {
    int x, y;
    cin >> x >> y;
    vec[x].pb({l, y});
  }

  int ans[q];
  for (int i = n; i >= 1; i--)
  {
    int cur = arr[i];
    for (int j = 1; j * j <= arr[i]; j++)
    {
      if (arr[i] % j == 0)
      {
        fcnt[j]++;
        if (arr[i] / j != j)
          fcnt[arr[i] / j]++;
      }
    }

    for (auto [idx, x] : vec[i])
      ans[idx] = fcnt[x];
  }

  for (int i = 0; i < q; i++)
    cout << ans[i] << "\n";

  return 0;
}