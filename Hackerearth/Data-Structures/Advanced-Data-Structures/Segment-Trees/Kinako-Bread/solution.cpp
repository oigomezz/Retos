#include <iostream>
using namespace std;
int main()
{
  int n, m;
  cin >> n >> m;
  vi arr(n);
  for (auto &it : arr)
    cin >> it;
  int res = 0, cnt = 0;
  int mp[m + 1];
  mset(mp, 0);
  int c[m + 1];
  mset(c, 0);
  vpii list(m + 1);
  for (int i = 1; i <= m; i++)
    cin >> list[i].ff >> list[i].ss;
  for (int left = 0, middle = 0, right = 0; right < n; right++)
  {
    cnt += ++mp[arr[right]] == list[arr[right]].ff;
    c[arr[right]]++;
    bool found = false;
    while (mp[arr[right]] > list[arr[right]].ss)
    {
      found = true;
      cnt -= --mp[arr[left]] == (list[arr[left]].ff - 1);
      if (++left > middle)
        c[arr[middle++]]--;
    }
    if (cnt == m)
    {
      while (c[arr[middle]] > list[arr[middle]].ff)
        c[arr[middle++]]--;
      res += middle - left + 1;
    }
  }
  cout << res << endl;
}
