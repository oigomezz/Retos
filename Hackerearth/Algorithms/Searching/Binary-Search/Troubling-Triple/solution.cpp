#include <cstdio>
#include <algorithm>
#include <cassert>
#include <vector>
using namespace std;

#define MAXN 2000
#define MAXK 1000001
vector<long long> ar;
vector<long long>::iterator up;

int main()
{
  int N, K;
  long long t;
  scanf("%d %d", &N, &K);
  assert(N > 0 and N <= MAXN);
  assert(K > 0 and K <= MAXK);
  for (int i = 0; i < N; i++)
  {
    scanf("%lld", &t);
    ar.push_back(t);
    assert(ar[i] > 0 and ar[i] <= 1000000);
  }
  sort(ar.begin(), ar.begin() + N);
  long long ans = 0;
  for (int i = 0; i < N; i++)
    for (int j = i + 1; j < N; j++)
    {
      long long f = (long long)K / ar[i];
      f = f / ar[j];
      up = upper_bound(ar.begin(), ar.end(), f);
      if (up - ar.begin() > j)
        ans = ans + (up - (ar.begin() + j) - 1);
    }
  printf("%lld\n", ans);
}