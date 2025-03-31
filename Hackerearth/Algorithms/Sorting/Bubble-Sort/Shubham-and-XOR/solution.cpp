#include <bits/stdc++.h>
using namespace std;

int main()
{
  int i, j, n, a;
  long long ans = 0;
  unordered_map<int, int> mp;
  scanf("%d", &n);
  for (i = 0; i < n; i++)
  {
    scanf("%d", &a);
    mp[a]++;
    ans -= (1ll) * (mp[a] - 1) * (mp[a] - 2) / 2;
    ans += (1ll) * (mp[a]) * (mp[a] - 1) / 2;
  }
  printf("%lld\n", ans);
  return 0;
}