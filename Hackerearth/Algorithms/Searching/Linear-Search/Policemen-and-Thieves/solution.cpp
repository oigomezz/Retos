#include <bits/stdc++.h>
using namespace std;

signed main()
{
  int t;
  cin >> t;
  while (t--)
  {
    int n, k;
    cin >> n;
    cin >> k;
    int res = 0;
    vector<int> thi;
    vector<int> pol;
    char arr[n][n];
    for (int i = 0; i < n; i++)
      for (int j = 0; j < n; j++)
        cin >> arr[i][j];

    int j = 0;
    while (j < n)
    {
      int cur_res = 0;
      for (int i = 0; i < n; i++)
      {
        if (arr[j][i] == 'P')
          pol.push_back(i);
        else if (arr[j][i] == 'T')
          thi.push_back(i);
      }

      int l = 0, r = 0;
      while (l < thi.size() && r < pol.size())
      {
        if (abs(thi[l] - pol[r]) <= k)
        {
          cur_res++;
          l++;
          r++;
        }
        else if (thi[l] < pol[r])
          l++;
        else
          r++;
      }

      res += cur_res;
      j++;
      pol.clear();
      thi.clear();
    }

    cout << res << endl;
  }
}