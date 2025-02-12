#include <bits/stdc++.h>
#define INF 1000000007
using namespace std;
vector<vector<int>> bit;
int get(int index, int k)
{
  int ans = bit[k][index];
  while (index > 0)
  {
    ans = min(ans, bit[k][index]);
    index -= index & (-index);
  }
  return ans;
}
void update(int index, int k, int val, int n)
{
  while (index <= n)
  {
    bit[k][index] = min(bit[k][index], val);
    index += index & (-index);
  }
}
int main()
{
  int n, k;
  cin >> n >> k;
  for (int i = 0; i <= k; i++)
  {
    vector<int> temp;
    for (int j = 0; j <= n; j++)
      temp.push_back(j);
    bit.push_back(temp);
  }
  for (int i = 0; i <= k; i++)
    for (int j = 0; j <= n; j++)
      bit[i][j] = INF;
  map<int, int> mp;
  int a[n + 5], ans = -1;
  for (int i = 1; i <= n; i++)
  {
    cin >> a[i];
    ans = max(ans, a[i]);
    mp[a[i]] = 1;
  }
  if (k == 1)
  {
    cout << ans << "\n";
    return 0;
  }

  ans = -1;
  int l = 1;
  map<int, int>::iterator it;
  for (it = mp.begin(); it != mp.end(); it++)
    it->second = l++;

  for (int i = 1; i <= n; i++)
  {
    int ind = mp[a[i]], val;
    update(ind, 1, a[i], l);
    for (int j = 2; j <= k; j++)
    {
      val = get(ind - 1, j - 1);
      update(ind, j, val, l);
    }

    ans = max(ans, a[i] - bit[k][ind]);
  }
  cout << ans << "\n";
  return 0;
}