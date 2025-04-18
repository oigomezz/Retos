#include <bits/stdc++.h>
using namespace std;
#define LL long long int

int N;
vector<int> A;

int main()
{
  cin >> N;
  assert(N <= 1000000 && N >= 1);
  A.resize(N);
  for (int i = 0; i < N; i++)
  {
    cin >> A[i];
    assert(A[i] <= 1000000 && A[i] >= 1);
  }
  sort(A.begin(), A.end());
  int i = 0, distinct = 0;
  LL ans;
  while (i < N)
  {
    distinct++;
    int x = A[i];
    while (i < N && x == A[i])
      i++;
  }
  ans = (1LL * distinct * (distinct - 1) / 2);
  cout << ans << endl;
  return 0;
}