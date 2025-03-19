#include <bits/stdc++.h>
using namespace std;

typedef long long ll;

bool check(int a[], int b[], int mid, int i, int j)
{
  while (i >= 0 and j >= 0)
  {
    if (a[i] > b[j])
      return 0;
    i -= mid;
    j -= 1;
  }
  if (j < 0 and i >= 0)
    return 0;
  return 1;
}

int main()
{
  ios::sync_with_stdio(0), cin.tie(0);
  int n, m;
  cin >> n >> m;
  int m1 = m - 1, n1 = n - 1;
  int a[n], b[m];
  for (int i = 0; i < n; i++)
    cin >> a[i];
  for (int i = 0; i < m; i++)
    cin >> b[i];
  sort(a, a + n);
  sort(b, b + m);
  if (b[m1] < a[n1])
    return cout << "-1\n", 0;
  int lo = 0, hi = n;
  while (lo < hi)
  {
    int mid = (lo + hi) / 2;
    if (check(a, b, mid, n1, m1))
      hi = mid;
    else
      lo = mid + 1;
  }
  cout << hi * 2 - 1 << '\n';
}