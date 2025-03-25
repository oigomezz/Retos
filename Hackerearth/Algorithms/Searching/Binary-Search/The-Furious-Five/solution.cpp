#include <bits/stdc++.h>
using namespace std;

long long int fun(vector<long long int> &five, long long int n)
{
  long long int sum = 0;
  for (int i = 0; i <= 20; i++)
    sum += n / five[i];
  return sum;
}

int main()
{
  int t;
  cin >> t;
  vector<long long int> five;
  long int p;
  p = 5;
  for (int i = 0; i <= 20; i++)
  {
    five.push_back(p);
    p *= 5;
  }
  while (t--)
  {
    long long int n;
    cin >> n;
    long long int ans;
    long long int l = 0;
    long long int r = 1e18;
    long long int mid;
    ans = LONG_MAX;
    while (l <= r)
    {
      mid = l + (r - l) / 2;
      if (fun(five, mid) < n)
        l = mid + 1;
      else
      {
        if (ans > mid)
          ans = mid;
        r = mid - 1;
      }
    }
    cout << ans << endl;
  }
}