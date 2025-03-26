#include <bits/stdc++.h>
using namespace std;

#define ll long long

const int mod = 1e9 + 7;
ll arr[500001];
ll power(ll x, ll p)
{
  ll ans = 1;
  while (p)
  {
    if (p & 1)
      ans = (ans * x) % mod;
    x = (x * x) % mod;
    p >>= 1;
  }
  return ans;
}

int main(int argc, char const *argv[])
{
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);
  ll n, q, d;
  cin >> n >> q;
  for (int i = 0; i < n; ++i)
  {
    cin >> arr[i];
  }
  sort(arr, arr + n);
  while (q--)
  {
    char id;
    cin >> id >> d;
    if (id == '=')
    {
      int idx1 = upper_bound(arr, arr + n, d) - arr;
      int idx2 = upper_bound(arr, arr + n, d - 1) - arr;
      if (idx2 == n || arr[idx2] != d)
        cout << 0 << endl;
      else
        cout << (power(2, idx1) - power(2, idx2) + mod) % mod << endl;
    }
    else if (id == '>')
    {
      int idx1 = upper_bound(arr, arr + n, d) - arr;
      cout << (power(2, n) - power(2, idx1) + mod) % mod << endl;
    }
    else
    {
      int idx1 = upper_bound(arr, arr + n, d - 1) - arr;
      cout << (power(2, idx1) + mod) % mod << endl;
    }
  }
  return 0;
}