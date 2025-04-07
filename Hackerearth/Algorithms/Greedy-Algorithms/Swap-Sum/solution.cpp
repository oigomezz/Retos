#include <bits/stdc++.h>

using namespace std;

int swapSum(int n, int k, vector<int> &a, vector<int> &b)
{
  // Initializing array 'v' and integer variable 'ans'.
  vector<pair<int, pair<int, int>>> v;
  int ans = 0;

  // Calculating 'ans'
  for (int i = 0; i < n; i++)
  {
    if (a[i] < b[i])
      v.push_back({b[i] - a[i], {b[i], a[i]}});
    else
      ans += a[i];
  }

  // Sorting 'v' in non-increasing order.
  sort(v.rbegin(), v.rend());

  for (int i = 0; i < min(k, (int)(v.size())); i++)
    ans += v[i].second.first;
  for (int i = k; i < v.size(); i++)
    ans += v[i].second.second;

  // We are returning the answer here.
  return ans;
}

int main()
{
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);
  int t;
  cin >> t;
  while (t--)
  {
    int n, k;
    cin >> n >> k;
    vector<int> a(n), b(n);
    for (auto &ele : a)
      cin >> ele;
    for (auto &ele : b)
      cin >> ele;
    cout << swapSum(n, k, a, b) << "\n";
  }
}