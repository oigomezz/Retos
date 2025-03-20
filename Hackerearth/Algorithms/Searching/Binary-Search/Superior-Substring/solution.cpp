#include <bits/stdc++.h>
using namespace std;

const int N = 1E5 + 5;
int f[N];
vector<int> A, L, R;

int main()
{
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);
  int t;
  cin >> t;
  while (t--)
  {
    int n;
    string s;
    cin >> n >> s;
    int ans = 1;
    for (int i = 0; i < 26; i++)
    {
      int cnt = 0;
      memset(f, 0, sizeof f);
      for (int j = 0; j < n; j++)
      {
        if (s[j] - 'a' == i)
          cnt++;
        f[j] = cnt;
      }
      for (int j = 0; j < n; j++)
      {
        L.push_back((2 * f[j - 1]) - j);
        R.push_back((2 * f[j]) - j);
      }
      int max_len = INT_MIN;
      int min_val = INT_MAX;
      for (int j = 0; j < n; j++)
      {
        min_val = min(min_val, L[j]);
        A.push_back(min_val);
        int l = 0, r = j;
        while (l <= r)
        {
          int mid = (l + r) >> 1;
          if (A[mid] <= R[j])
          {
            max_len = max(max_len, j - mid + 1);
            r = mid - 1;
          }
          else
          {
            l = mid + 1;
          }
        }
      }
      ans = max(ans, max_len);
      A.clear();
      R.clear();
      L.clear();
    }
    cout << ans << '\n';
  }
  return 0;
}