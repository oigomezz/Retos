#include <bits/stdc++.h>
#define ll int64_t
#define pii pair<int, int>
#define pb push_back
#define vi vector<int>

using namespace std;
const ll mod = 1e9 + 7;
const int N = 2e5 + 5;

string ss;
int n, m, p[N];
struct Q
{
  int qi, id;
};
vector<Q> q[N];
ll ans[N];

struct bit
{
  ll ar[N];
  bit() { fill(ar, ar + N, 0); }
  ll query(ll x)
  {
    ll res = 0;
    while (x)
      res += ar[x], x -= (x & -x);
    return res;
  }
  void update(ll x, ll by)
  {
    while (x <= n + 1)
      ar[x] += by, x += (x & -x);
  }
} bb;

void manacher()
{
  string s = "|";
  for (auto x : ss)
    s.pb(x), s.pb('|');
  n = s.size();
  int m = 0, r = 0;
  for (int i = 1; i < n; i++)
  {
    p[i] = (r > i) ? min(p[m - (i - m)], r - i) : 0;
    while (i - p[i] >= 1 && s[i + 1 + p[i]] == s[i - 1 - p[i]])
      p[i]++;
    if (i + p[i] > r)
      r = i + p[i], m = i;
  }
}

void offline()
{
  for (int i = n - 2; i; i--)
  {
    bb.update(i - p[i] + 1, 1);
    for (auto &qq : q[i])
      ans[qq.id] = bb.query(qq.qi + 1);
  }
}

int main()
{
  cin.tie(NULL);
  cout.tie(NULL);
  ios_base::sync_with_stdio(false);
  int ii, len;
  cin >> ss;
  manacher();
  cin >> m;
  for (int i = 0; i < m; i++)
  {
    cin >> ii >> len;
    ii = ii * 2 + 1;
    if (ii + len - 1 < n)
      q[ii + len - 1].pb({ii, i});
    ans[i] = 0;
  }
  offline();
  for (int i = 0; i < m; i++)
    cout << ans[i] << "\n";
  return 0;
}