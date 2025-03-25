#include <bits/stdc++.h>
#include <iostream>
#define pb push_back
#define ll long long
#define mod 1000000007
using namespace std;
vector<ll int> arr(500000, 0);

int main()
{
  string ss;
  cin >> ss;
  ll int qq;
  cin >> qq;
  vector<ll int> pre(ss.size() + 1, 0);
  for (int i = 1; i <= ss.size(); i++)
  {
    pre[i] = ss.size() - i + 1;
  }
  for (int i = 1; i <= ss.size(); i++)
    pre[i] = pre[i] + pre[i - 1];
  cout << endl;
  while (qq--)
  {
    ll int num;
    cin >> num;
    ll int index = lower_bound(pre.begin(), pre.end(), num) - pre.begin();
    if (index == ss.size() + 1)
      cout << "-1" << endl;
    else
    {
      num = num - pre[index - 1];
      string ans = ss.substr(index - 1, num);
      cout << ans << endl;
    }
  }
  return 0;
}