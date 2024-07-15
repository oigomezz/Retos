#include <bits/stdc++.h>

using namespace std;
const int N = 300005;
int n, k, id = N, A[N], P[N];
long long tot, Mn = LLONG_MAX;
bool CMP(int i, int j)
{
  return (A[i] < A[j]);
}
int main()
{
  scanf("%d%d", &n, &k);
  for (int i = 1; i <= n; i++)
    scanf("%d", &A[i]), P[i] = i;
  sort(P + 1, P + n + 1, CMP);
  for (int i = 1; i <= n; i++)
    tot += A[P[i]] - A[P[1]];
  for (int i = 1; i <= n; i++)
  {
    if (tot >= k && Mn > tot - k)
      Mn = tot - k, id = P[i];
    if (tot >= k && Mn >= tot - k)
      Mn = tot - k, id = min(id, P[i]);
    if (tot < k && Mn > ((k - tot) & 1))
      Mn = (k - tot) & 1, id = P[i];
    if (tot < k && Mn >= ((k - tot) & 1))
      Mn = (k - tot) & 1, id = min(id, P[i]);
    tot += (A[P[i + 1]] - A[P[i]]) * 1LL * (i + i - n);
  }
  return !printf("%d %lld\n", id, Mn);
}