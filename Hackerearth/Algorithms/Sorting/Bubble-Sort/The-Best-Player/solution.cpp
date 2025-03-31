#include <bits/stdc++.h>
using namespace std;

typedef long long LL;

#define PII pair<int, int>
#define all(c) c.begin(), c.end()
#define sz(c) (int)c.size()
#define clr(c) c.clear()
#define pb push_back
#define mp make_pair
#define cin(x) scanf("%d", &x)
#define MOD 1000000007
#define EPS 1E-10

vector<pair<string, int>> arr;

bool cmp(const pair<string, int> &A, const pair<string, int> &B)
{
  return ((A.second > B.second) or (A.second == B.second && A.first < B.first));
}

bool ok(string &a)
{
  for (auto i : a)
    if (i >= 'a' && i <= 'z')
      continue;
    else
      return false;
  return true;
}

int main()
{
  int n, t;
  cin(n);
  cin(t);
  assert(1 <= t && t <= n && n <= 1000);
  arr.resize(n);
  for (auto &i : arr)
  {
    cin >> i.first >> i.second;
    assert(ok(i.first) && 1 <= i.second && i.second <= 1000000000);
  }
  sort(all(arr), cmp);
  for (int i = 0; i < t; i++)
    cout << arr[i].first << "\n";
  return 0;
}