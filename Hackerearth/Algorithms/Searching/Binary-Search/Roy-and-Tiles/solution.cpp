#include <bits/stdc++.h>
using namespace std;

void get(vector<int> &v, int &sidx, int &lidx, int target)
{
  int st = 0;
  int end = v.size() - 1;
  while (st <= end)
  {
    int mid = st + (end - st) / 2;
    if (v[mid] == target)
    {
      sidx = mid;
      end = mid - 1;
    }
    else if (v[mid] > target)
      end = mid - 1;
    else
      st = mid + 1;
  }
  st = 0;
  end = v.size() - 1;
  while (st <= end)
  {
    int mid = st + (end - st) / 2;
    if (v[mid] == target)
    {
      lidx = mid;
      st = mid + 1;
    }
    else if (v[mid] > target)
      end = mid - 1;

    else
      st = mid + 1;
  }
}

int main()
{
  int t;
  cin >> t;

  while (t--)
  {
    int n;
    cin >> n;
    vector<vector<int>> v(n, vector<int>(n));
    for (int i = 0; i < n; i++)
    {
      for (int j = 0; j < n; j++)
        cin >> v[i][j];

      sort(begin(v[i]), end(v[i]));
    }

    int MOD = 1000000007;

    vector<long long> dp(n, 0);
    dp[0] = 1;
    for (int i = 1; i < n; i++)
    {
      dp[i] = 1 + dp[i - 1];
      dp[i] %= MOD;
    }

    for (int i = n - 2; i >= 0; i--)
    {
      vector<int> temp(n, 0);
      for (int j = 0; j < n; j++)
      {
        int elem = v[i][j] + 1;
        int sidx = -1, lidx = -1;
        get(v[i + 1], sidx, lidx, elem);

        if (sidx != -1)
        {
          int total = (dp[lidx] - (sidx > 0 ? dp[sidx - 1] : 0) + MOD) % MOD;
          temp[j] = total;
        }
      }
      vector<long long> p(n, 0);
      p[0] = temp[0];
      for (int j = 1; j < n; j++)
      {
        p[j] = (p[j - 1] % MOD + temp[j] % MOD) % MOD;
      }
      dp = p;
    }

    int q;
    cin >> q;

    while (q--)
    {
      int s, d;
      cin >> s >> d;
      if (s + n + 1 != d)
      {
        cout << 0 << "\n";
        continue;
      }
      bool f1 = false, f2 = false;
      for (int i = 0; i < n; i++)
      {
        if (v[0][i] == s + 1)
          f1 = true;

        if (v[n - 1][i] == d - 1)
          f2 = true;
      }
      if (f1 and f2)
      {
        long long total = 0;
        int sidx = -1, lidx = -1;
        get(v[0], sidx, lidx, s + 1);
        total = (dp[lidx] - (sidx > 0 ? dp[sidx - 1] : 0) + MOD) % MOD;
        cout << total << "\n";
      }
      else
        cout << 0 << "\n";
    }
  }
}