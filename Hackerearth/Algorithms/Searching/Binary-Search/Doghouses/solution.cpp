#include <bits/stdc++.h>
using namespace std;
int main()
{
  ios_base::sync_with_stdio(0);
  cin.tie(0);
  cout.tie(0);
  int n, amx, i, m1 = 0, m2 = 0, y1 = 0, y2 = 0, y0, yn, ct, y;
  cin >> n;
  int a[n];
  for (int i = 0; i < n; ++i)
    cin >> a[i];
  if (n < 3)
  {
    cout << n << '\n';
    return 0;
  }
  amx = *max_element(a, a + n) + 1;
  int f[amx];
  fill(f, f + amx, 0);
  for (i = 1; i < n - 1; i++)
    f[a[i]] += 1;
  y0 = a[0];
  yn = a[n - 1];
  for (y = 0; y < amx; y++)
  {
    ct = f[y];
    if (ct >= m1)
    {
      if (m2 != m1)
        m2 = m1, y2 = y1;
      m1 = ct;
      y1 = y;
    }
    else if (ct >= m2)
      m2 = ct, y2 = y;
  }
  if (y2 > y1)
    swap(y1, y2);
  if (m2)
  {
    int lft = 0;
    if (a[0] == y1 or a[0] == y2)
      lft = 1;
    else
    {
      for (auto v : a)
      {
        if (v == y1 or v == y2)
          break;
        if (v >= y2 and v <= y1)
        {
          lft = 1;
          break;
        }
      }
    }
    int rght = 0;
    if (a[n - 1] == y1 or a[n - 1] == y2)
      rght = 1;
    else
    {
      for (i = n - 1; i >= 0; i--)
      {
        int v = a[i];
        if (v == y1 or v == y2)
          break;
        if (v >= y2 and v <= y1)
        {
          rght = 1;
          break;
        }
      }
    }
    cout << m1 + m2 + lft + rght << '\n';
  }
  else
  {
    int add = 0;
    if (y0 >= y1 and yn >= y1 or y0 < y1 and yn < y1)
      add = 2;
    else
      add = 1;
    cout << m1 + add << '\n';
  }
  return 0;
}