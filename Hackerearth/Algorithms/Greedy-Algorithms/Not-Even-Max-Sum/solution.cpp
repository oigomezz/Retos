#include <bits/stdc++.h>
using namespace std;

long long solve(int n, int arr[])
{
  int odd = 0;
  long long sum = 0;
  int minodd = INT_MAX;
  for (int i = 0; i < n; i++)
  {
    sum += arr[i];
    if (arr[i] % 2 == 1)
    {
      odd++;
      if (minodd > arr[i])
        minodd = arr[i];
    }
  }

  if (sum % 2 == 1)
    return sum;
  else if (odd == 0)
    return 0;
  else
    return sum - minodd;
}

int main()
{

  ios::sync_with_stdio(0);
  cin.tie(0);
  int T;
  cin >> T;
  for (int t_i = 0; t_i < T; t_i++)
  {
    int N;
    cin >> N;
    int arr[N];
    for (int i = 0; i < N; i++)
      cin >> arr[i];
    long long out_;
    out_ = solve(N, arr);
    cout << out_;
    cout << endl;
  }
}