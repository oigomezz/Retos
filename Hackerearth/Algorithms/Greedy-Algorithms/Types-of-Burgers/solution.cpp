#include <bits/stdc++.h>
using namespace std;
int main()
{
  int t;
  cin >> t;
  while (t--)
  {
    int x, y, z;
    cin >> x >> y >> z;
    int k;
    cin >> k;
    long long int b1[x], b2[y], b3[z];
    for (int i = 0; i < x; i++)
      cin >> b1[i];

    for (int j = 0; j < y; j++)
      cin >> b2[j];

    for (int u = 0; u < z; u++)
      cin >> b3[u];

    sort(b1, b1 + x);
    sort(b2, b2 + y);
    sort(b3, b3 + z);
    reverse(b1, b1 + x);
    reverse(b2, b2 + y);
    reverse(b3, b3 + z);
    priority_queue<vector<long long int>> pq;
    long long int ans = 0;
    set<vector<int>> st;
    st.insert({0, 0, 0});
    pq.push({b1[0] + b2[0] + b3[0], 0, 0, 0});
    while (k != 0)
    {
      ans += pq.top()[0];
      int i1 = pq.top()[1];
      int i2 = pq.top()[2];
      int i3 = pq.top()[3];
      pq.pop();
      if (i1 + 1 < x && st.find({i1 + 1, i2, i3}) == st.end())
      {
        st.insert({i1 + 1, i2, i3});
        pq.push({b1[i1 + 1] + b2[i2] + b3[i3], i1 + 1, i2, i3});
      }
      if (i2 + 1 < y && st.find({i1, i2 + 1, i3}) == st.end())
      {
        st.insert({i1, i2 + 1, i3});
        pq.push({b1[i1] + b2[i2 + 1] + b3[i3], i1, i2 + 1, i3});
      }
      if (i3 + 1 < z && st.find({i1, i2, i3 + 1}) == st.end())
      {
        st.insert({i1, i2, i3 + 1});
        pq.push({b1[i1] + b2[i2] + b3[i3 + 1], i1, i2, i3 + 1});
      }
      k--;
    }
    cout << ans << "\n";
  }
}