#include <bits/stdc++.h>
using namespace std;
string s;

long long value(int b, int c)
{
  long long val = 0, l = 1;
  for (int i = c; i >= b; i--)
  {
    if (s[i] == '1')
      val += l;
    l *= 2;
  }
  return val;
}

int main()
{
  long long int c, p;
  cin >> s >> c >> p;
  int len = s.length();
  long long ans = 0;
  for (int i = 0; i < len - 2; i++)
  {
    int cl = 0, cr = 0;
    for (int j = max(0, i - 25 + 1); j <= i; j++)
    {
      long long a = value(j, i);
      if (a == c)
        cl++;
    }
    for (int j = i + 1; j <= min(len - 1, i + 25); j++)
    {
      long long a = value(i + 1, j);
      if (a == p)
        cr++;
    }
    ans += cr * cl;
  }
  cout << ans << endl;
}