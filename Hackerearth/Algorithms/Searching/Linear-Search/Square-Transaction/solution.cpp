#include <bits/stdc++.h>
using namespace std;

int binary_search(int a[], int x, int lo, int hi)
{
  if (x > a[hi])
    return -1;
  int trans_no = 0;
  while (hi >= lo)
  {
    int mid = lo + (hi - lo) / 2;
    if (a[mid] >= x)
    {
      trans_no = mid;
      hi = mid - 1;
    }
    else
      lo = mid + 1;
  }
  return trans_no;
}

int main()
{
  int n;
  cin >> n;
  int a[n + 11];
  a[0] = 0;
  for (int i = 1; i <= n; i++)
  {
    cin >> a[i];
    a[i] += a[i - 1];
  }
  int q;
  cin >> q;
  while (q--)
  {
    int x;
    cin >> x;
    cout << binary_search(a, x, 1, n) << "\n";
  }

  return 0;
}