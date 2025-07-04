#include <bits/stdc++.h>
#define endl '\n'
#define vi vector<int>
#define vll vector<long long>
#define ll long long
#define int long long
#define ii pair<int, int>
#define vii vector<ii>
#define MAX 1e18
#define MIN -1e18
#define LSOne(S) ((S) & -(S))
#define digitCount(a) (int)floor(1 + log10((double)a))
#define iii tuple<int, int, int> // get<0> get<1> tie(par1, par2, par3)
using namespace std;

const double EPS = 1e-9;
const int mod = 1e9 + 7;

bool cmp(const int &a, const int &b)
{
  return a > b;
}

int input(int a[], int n)
{
  for (int i = 0; i < n; i++)
  {
    cin >> a[i];
  }
  return n;
}

int input(vi &a)
{
  int n;
  cin >> n;
  for (int i = 0; i < n; i++)
  {
    int temp;
    cin >> temp;
    a.push_back(temp);
  }
  return n;
}

int setMask(int mask, int i, int j)
{
  mask |= (1 << i);
  mask |= (1 << j);
  return mask;
}

int f(int round, int n, int a[], int k, int mask, vector<vector<int>> &dp)
{
  if (round > k)
    return 0;
  if (dp[round][mask] != -1)
    return dp[round][mask];
  int ans = 0;
  for (int i = 0; i < n; i++)
  {
    if ((mask >> i) & 1)
      continue;
    for (int j = i + 1; j < n; j++)
    {
      if ((mask >> j) & 1)
        continue;
      ans = max(ans, round * (a[i] & a[j]) + f(round + 1, n, a, k, setMask(mask, i, j), dp));
    }
  }
  return dp[round][mask] = ans;
}

void solve()
{
  int n;
  cin >> n;
  int a[n];
  input(a, n);
  int k;
  cin >> k;
  vector<vector<int>> dp(k + 1, vector<int>((1 << n) + 1, -1));
  cout << f(1, n, a, k, 0, dp) << endl;
}

int32_t main(void)
{
  ios::sync_with_stdio(false);
  cin.tie(NULL);
  cout.tie(NULL);
  int t = 1;
  // cin >> t;
  while (t--)
  {
    solve();
  }
  return 0;
}