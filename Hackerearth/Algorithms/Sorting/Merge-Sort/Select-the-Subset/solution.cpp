#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

template <typename T>
inline void inp(T &n)
{
  n = 0;
  int ch = getchar_unlocked(), sign = 1;
  while (ch < '0' || ch > '9')
  {
    if (ch == '-')
      sign = -1;
    ch = getchar_unlocked();
  }
  while (ch >= '0' && ch <= '9')
    n = (n << 3) + (n << 1) + ch - '0', ch = getchar_unlocked();
  n *= sign;
}

int LongestSubsequenceLength(vector<int> &v, int n)
{
  if (n == 0)
    return 0;
  vector<int> tail(n, 0);
  int length = 1; // always points empty slot in tail
  tail[0] = v[0];
  for (int i = 1; i < n; i++)
  {
    if (v[i] > tail[length - 1])
      tail[length++] = v[i];
    else
      tail[lower_bound(tail.begin(), tail.begin() + length, v[i]) - tail.begin()] = v[i];
  }
  return length;
}

int main()
{
  ios::sync_with_stdio(0), cin.tie(0), cout.tie(0);
  int t;
  inp(t); // cin >> t;
  while (t--)
  {
    int n;
    inp(n); // cin >> n;
    pair<int, int> a[n];
    for (int i = 0; i < n; ++i)
      inp(a[i].first); // cin >> a [i].first;
    for (int i = 0; i < n; ++i)
      inp(a[i].second); // cin >> a [i].second;
    sort(a, a + n);
    vector<int> sb(n);
    for (int i = 0; i < n; ++i)
      sb[i] = a[i].second;
    cout << LongestSubsequenceLength(sb, n) << '\n';
  }
}