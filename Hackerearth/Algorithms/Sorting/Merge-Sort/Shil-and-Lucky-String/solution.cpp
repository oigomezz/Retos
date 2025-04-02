#include <iostream>
#include <vector>
#include <string>

using namespace std;

template <typename T>
inline void inp(T &n)
{
  n = 0;
  int ch = getchar_unlocked(), sign = 1;
  while (ch < '0' || ch > '9')
  {
    if (ch == '-')
      sign = -1; // only if also negative integer
    ch = getchar_unlocked();
  }
  while (ch >= '0' && ch <= '9')
    n = (n << 3) + (n << 1) + ch - '0', ch = getchar_unlocked();
  n *= sign; // only if also negative integer
}

inline int inp()
{
  int n = 0;
  int ch = getchar_unlocked(), sign = 1;
  while (ch < '0' || ch > '9')
  {
    if (ch == '-')
      sign = -1; // only if also negative integer
    ch = getchar_unlocked();
  }
  while (ch >= '0' && ch <= '9')
    n = (n << 3) + (n << 1) + ch - '0', ch = getchar_unlocked();
  n *= sign; // only if also negative integer
  return n;
}

inline void inps(string &i)
{
  i = "";
  char temp = getchar_unlocked();
  while (temp == '\n' or temp == ' ')
    temp = getchar_unlocked();
  while (temp != '\n' and temp != ' ' and temp != EOF)
    i += temp, temp = getchar_unlocked();
}

int grt(vector<int> a, vector<int> b)
{
  int ans = a[0], req;
  a[25] += ans;
  a[0] = 0;
  for (int i = 1; i < 26; i++)
  {
    req = a[i];
    for (int j = 0; j < i; j++)
    {
      if (b[j] >= req)
        b[j] -= req, req = 0;
      else
        req -= b[j], b[j] = 0;
      if (not req)
        break;
    }
    ans += req;
  }
  return ans;
}

int equ(vector<int> &a, vector<int> &b)
{
  int ans = 0;
  for (int i = 0; i < 26; i++)
    ans += abs(b[i] - a[i]);
  return ans / 2;
}

int main()
{
  ios::sync_with_stdio(0);
  cin.tie(0);
  cout.tie(0);
  int i, n, nh, gt, sm, eq, mn;
  inp(n);
  nh = n / 2;
  string s;
  inps(s);
  vector<int> a(26, 0);
  vector<int> b(26, 0);
  for (i = 0; i < nh; i++)
    a[s[i] - 'a']++, b[s[i + nh] - 'a']++;
  gt = grt(a, b);
  sm = grt(b, a);
  eq = equ(a, b);
  if (gt < sm)
  {
    if (gt < eq)
      mn = gt;
    else
      mn = eq;
  }
  else
  {
    if (sm < eq)
      mn = sm;
    else
      mn = eq;
  }
  cout << mn << '\n';
  return 0;
}