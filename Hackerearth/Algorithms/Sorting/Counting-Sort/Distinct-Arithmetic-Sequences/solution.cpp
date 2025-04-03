#include <bits/stdc++.h>
using namespace std;
using ll = long long;

ll ans = 0;

void solve(vector<int> &x, int d, int n)
{
  int cnt = 1;
  for (int i = 1; i < x.size(); i++)
  {
    if (x[i] - x[i - 1] == d)
      ++cnt;
    else
    {
      ans += max(cnt - n + 1, 0) * 2;
      cnt = 1;
    }
  }
  ans += max(cnt - n + 1, 0) * 2;
}

int main()
{
  ios::sync_with_stdio(false);
  cin.tie(0);
  cout.tie(0);
  int t;
  cin >> t;
  while (t--)
  {
    ans = 0;
    int n, m;
    cin >> n >> m;
    int a[n];
    for (int i = 0; i < n; i++)
      cin >> a[i];
    int b[m];
    for (int i = 0; i < m; i++)
      cin >> b[i];
    int c[n + m];
    int i = 0, j = 0, k = 0;
    while (i < n && j < m)
    {
      if (a[i] <= b[j])
        c[k++] = a[i++];
      else
        c[k++] = b[j++];
    }
    while (i < n)
      c[k++] = a[i++];
    while (j < m)
      c[k++] = b[j++];
    int cnt = 1;
    vector<int> x{c[0]};
    for (int i = 1; i < n + m; i++)
    {
      if (c[i] == c[i - 1])
        ++cnt;
      else
      {
        if (cnt >= n)
          ++ans;
        x.push_back(c[i]);
        cnt = 1;
      }
    }
    if (cnt >= n)
      ++ans;
    m = x.size();
    if (m < n)
    {
      cout << ans << endl;
      continue;
    }
    for (int i = m - 1; i >= 0; i--)
      x[i] -= x[0];
    int d = 2 * n / (n - 1);
    if (x[m - 1] - x[0] >= n - 1)
      solve(x, 1, n);
    for (int i = 2; i <= d; i++)
    {
      if (x[m - 1] - x[0] >= 1LL * i * (n - 1))
      {
        vector<vector<int>> p(i, vector<int>());
        for (int j = 0; j < m; j++)
          p[x[j] % i].push_back(x[j]);
        for (int j = 0; j < i; j++)
          if (p[j].size() >= n)
            solve(p[j], i, n);
      }
    }
    cout << ans << endl;
  }
  return 0;
}