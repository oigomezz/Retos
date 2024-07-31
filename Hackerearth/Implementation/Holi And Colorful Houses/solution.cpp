#include <bits/stdc++.h>

using namespace std;

int main()
{
  int t;
  cin >> t;
  while (t--)
  {
    int n, q;
    int x1, y1;
    cin >> n >> q;
    string s;
    cin >> s;
    int count, ans;
    while (q--)
    {
      count = 0, ans = 0;
      int x, y;
      cin >> x >> y;
      x--;
      y--;
      x1 = x;
      y1 = y;
      while (x != y)
      {
        x++;
        if (x != n && s[x] != s[x - 1])
          count++;
        else if (x == n)
        {
          if (s[0] != s[n - 1])
            count++;

          if (x == y)
            break;

          x = 0;
        }
      }
      while (x1 != y1)
      {
        x1--;
        if (x1 != -1 && s[x1] != s[x1 + 1])
          ans++;
        else if (x1 == -1)
        {
          if (s[0] != s[n - 1])
            ans++;

          if (x1 == y1)
            break;

          else
            x1 = n - 1;
        }
      }

      if (count > ans)
        cout << ans << endl;

      else
        cout << count << endl;
    }
  }
}