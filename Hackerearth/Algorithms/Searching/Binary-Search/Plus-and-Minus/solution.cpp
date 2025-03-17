#include <bits/stdc++.h>
using namespace std;
#define ll long long
#define pb push_back
ll a[100001];
ll pre[100001];
int main()
{
  vector<int> v;
  int n;
  cin >> n;
  cin >> a[0];
  ll sum = a[0];
  string s;
  ll cnt = 0;
  pre[0] = a[0];
  for (int i = 1; i < n; i++)
  {
    cin >> s >> a[i];
    sum += a[i];
    pre[i] = pre[i - 1] + a[i];
    if (s[0] == '-')
    {
      v.pb(i);
      cnt += a[i];
    }
  }
  ll mx = -1e18;
  if (v.size() < 2)
  {
    cout << sum - 2 * cnt;
    return 0;
  }
  for (int i = 0; i < v.size() - 1; i++)
  {
    mx = max(sum - 2 * (pre[v[i + 1] - 1] - pre[v[i] - 1]), mx);
    sum -= 2 * a[v[i]];
  }
  sum -= 2 * a[v[v.size() - 1]];
  cout << max(mx, sum);
  return 0;
}