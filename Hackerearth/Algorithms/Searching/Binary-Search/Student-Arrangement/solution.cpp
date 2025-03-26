#include <bits/stdc++.h>
using namespace std;

int main()
{
  int n, m, k;
  cin >> n >> m >> k;
  vector<int> prefer(n);
  vector<int> cap(m + 1, k);
  set<int> s;
  for (int i = 1; i <= m; i++)
    s.insert(i);
  int ans = 0;
  for (int i = 0; i < n; i++)
    cin >> prefer[i];
  for (int i = 0; i < n; i++)
  {
    if (cap[prefer[i]] != 0)
    {
      cap[prefer[i]]--;
      if (cap[prefer[i]] == 0)
        s.erase(prefer[i]);
    }
    else
    {
      if (s.empty())
      {
        ans += n - i;
        break;
      }
      ans++;
      auto it = s.upper_bound(prefer[i]);
      if (it == s.end())
        it = s.begin();
      cap[*it]--;
      if (cap[*it] == 0)
        s.erase(it);
    }
  }
  cout << ans;
}