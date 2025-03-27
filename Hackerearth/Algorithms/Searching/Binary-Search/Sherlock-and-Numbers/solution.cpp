#include <bits/stdc++.h>
using namespace std;

long fun()
{
  long n, k, p;
  cin >> n >> k >> p;
  long min = p;
  unordered_set<long> mp;
  vector<long> v(k);
  for (int i = 0; i < k; i++)
    cin >> v[i];
  for (auto x : v)
  {
    if (x <= min)
    {
      min++;
    }
    else
    {
      mp.insert(x);
    }
    while (mp.find(min) != mp.end())
    {
      min++;
    }
    if (min > n)
    {
      min = -1;
      break;
    }
  }
  return min;
}

int main()
{
  int t;
  cin >> t;
  while (t--)
  {
    cout << fun() << endl;
  }
}