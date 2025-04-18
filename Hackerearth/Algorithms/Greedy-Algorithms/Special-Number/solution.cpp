#include <bits/stdc++.h>
using namespace std;
vector<long long> freq, possible;
#define MOD 1000000007

long long solve(int ind, long long prev)
{
  for (int i = 2; i <= 5; i++)
  {
    if (prev % (i * i) == 0)
      return 0;
  }
  long long req = 0;
  if (ind == possible.size())
    return 1;
  if (freq[possible[ind]] > 0)
  {
    long long cur = 0;
    if (__gcd(prev, possible[ind]) == 1)
      cur += solve(ind + 1, prev * possible[ind]) * freq[possible[ind]];
    cur %= MOD;
    req = (req % MOD + cur % MOD) % MOD;
  }
  long long temp = solve(ind + 1, prev);
  req = (req % MOD + temp % MOD) % MOD;
  return req;
}

long long int pow1(long long int n, long long int k)
{
  if (k == 0)
    return 1;
  if (k == 1)
    return n;
  long long int X = 1;
  if (k % 2 == 1)
    X = n % MOD;
  long long int Y = pow1(n, k / 2) % MOD;
  return (((Y * Y) % MOD) * X) % MOD;
}

int main()
{
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);
  cout.tie(NULL);
  int n;
  cin >> n;
  possible = vector<long long>({2, 3, 5, 6, 7, 10, 11, 13, 14, 15, 17, 19, 21, 22, 23, 26, 29, 30});
  freq = vector<long long>(31);
  vector<int> arr(n);
  for (int i = 0; i < n; i++)
  {
    int val;
    cin >> val;
    arr[i] = val;
    freq[val]++;
  }
  long long ans = solve(0, 1);
  ans = (((long long)pow1(2, freq[1]) % MOD) * (ans % MOD)) % MOD;
  ans %= MOD;
  ans = (ans + MOD - 1) % MOD;
  cout << ans << '\n';
}