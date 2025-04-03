#include <bits/stdc++.h>
using namespace std;

int main()
{
  int t;
  cin >> t;
  for (int i = 0; i < t; i++)
  {
    int n, x, y;
    cin >> n;
    vector<pair<int, int>> v;
    for (int i = 0; i < n; i++)
    {
      cin >> x >> y;
      v.push_back({y, x});
    }
    sort(v.begin(), v.end());

    int ans = 1;
    int p = 0;
    priority_queue<int, vector<int>, greater<int>> pq;
    pq.push(v[0].second);
    for (int i = 1; i < n; i++)
    {
      if (v[i].first >= pq.top())
      {
        while (pq.size() > 0)
        {
          if (v[i].first < pq.top())
            break;
          pq.pop();
        }
      }
      pq.push(v[i].second);
      int z = pq.size();
      ans = max(ans, z);
    }
    cout << ans << endl;
  }
}