#include <iostream>
#include <bits/stdc++.h>
using namespace std;
int main()
{
  int n, k;
  cin >> n;
  vector<int> freq(n);
  for (int i = 0; i < n; i++)
    cin >> freq[i];
  cin >> k;
  int keysize[k];
  int temp = 0;
  for (int i = 0; i < k; i++)
  {
    cin >> keysize[i];
    temp += keysize[i];
  }
  if (temp < n)
  {
    cout << -1;
    return 0;
  }

  sort(freq.begin(), freq.end(), greater<int>());
  vector<vector<int>> arr(k);
  int i = 0;
  for (int j = 0; j < n; j++)
  {
    if (arr[i].size() < keysize[i])
      arr[i].push_back(freq[j]);
    else
      j--;

    if (++i == k)
      i = 0;
  }

  int ans = 0;
  for (int i = 0; i < k; i++)
  {
    int lvl = 1;
    for (auto it : arr[i])
    {
      ans += (it * lvl);
      lvl++;
    }
  }
  cout << ans;
}