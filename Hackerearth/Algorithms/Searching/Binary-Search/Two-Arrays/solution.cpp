#include <bits/stdc++.h>
using namespace std;

typedef long long int ll;
#define MAX 100005
vector<int> adj[MAX];
int xMove[] = {0, 1, 0, -1, 1, 1, -1, -1, 2, 2, -2, -2, 1, 1, -1, -1};
int yMove[] = {1, 0, -1, 0, 1, -1, 1, -1, 1, -1, 1, -1, 2, -2, 2, -2};

int csum[2000 + 1][2000 + 1];
int main()
{
  cin.tie(0), cout.tie(0);
  ios_base::sync_with_stdio(0);
  cout.setf(ios::fixed);
  cout.precision(10);
  int TC = 1;
  int n, m, k, q;

  cin >> n >> m >> k;
  int a[n + 1], b[m + 1];
  for (int i = 1; i <= n; i++)
    cin >> a[i];
  for (int i = 1; i <= m; i++)
    cin >> b[i];

  for (int i = 1; i <= n; i++)
    for (int j = 1; j <= m; j++)
      csum[i][j] = a[i] == b[j];
  for (int i = 1; i <= n; i++)
    for (int j = 1; j <= m; j++)
      csum[i][j] += csum[i][j - 1];
  for (int i = 1; i <= n; i++)
    for (int j = 1; j <= m; j++)
      csum[i][j] += csum[i - 1][j];

  ll ans = 0;
  for (int i = 1; i <= n; i++)
  {
    for (int j = 1; j <= m; j++)
    {
      int lo = 0, hi = min(n, m), ans1 = -1, ans2 = -1;
      while (lo <= hi)
      {
        int mid = (lo + hi) >> 1;

        if (i + mid <= n and j + mid <= m)
        {
          int s = csum[i + mid][j + mid] - csum[i - 1][j + mid] - csum[i + mid][j - 1] + csum[i - 1][j - 1];
          if (s >= k)
          {
            ans1 = mid;
            hi = mid - 1;
          }
          else
            lo = mid + 1;
        }
        else
          hi = mid - 1;
      }

      if (ans1 != -1)
        ans += min(n - i - ans1 + 1, m - j - ans1 + 1);
    }
  }

  cout << ans << "\n";
  return 0;
}