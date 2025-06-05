#include <bits/stdc++.h>
using namespace std;

#include <ext/pb_ds/assoc_container.hpp>
#include <ext/pb_ds/tree_policy.hpp>

using namespace __gnu_pbds;
template <typename T>
using ordered_set = tree<T, null_type, less<T>, rb_tree_tag, tree_order_statistics_node_update>;

void dfs(int s, vector<vector<int>> &v, vector<int> &vis, vector<int> &curr, vector<int> &res)
{
  vis[s] = 1;
  curr.push_back(s);
  for (auto i : v[s])
  {
    if (!vis[i])
      dfs(i, v, vis, curr, res);
    else if (vis[i] == 1)
    {
      vector<int> temp;
      int ind = 0;
      while (ind < curr.size() && curr[ind] != i)
        ind++;
      while (ind < curr.size())
        temp.push_back(curr[ind++]);
      if (!res.size() || temp.size() < res.size())
        res = temp;
    }
  }
  curr.pop_back();
  vis[s] = 2;
}

int main()
{
  ios_base::sync_with_stdio(0);
  cin.tie(0);
  cout.tie(0);
  int n, m, x, y;
  cin >> n >> m;
  vector<vector<int>> v(n + 1);
  for (int i = 0; i < m; ++i)
  {
    cin >> x >> y;
    v[x].push_back(y);
  }
  vector<int> vis(n + 1, 0), res, curr;
  for (int i = 1; i < n + 1; ++i)
  {
    if (!vis[i])
      dfs(i, v, vis, curr, res);
  }
  if (!res.size())
    cout << -1 << '\n';
  else
  {
    cout << res.size() << '\n';
    for (int i = 1; i < res.size(); ++i)
    {
      cout << res[i - 1] << ' ' << res[i] << '\n';
    }
    cout << res.back() << ' ' << res[0] << '\n';
  }
  return 0;
}