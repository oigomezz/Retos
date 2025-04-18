#include <bits/stdc++.h>
using namespace std;

int solve(int N, vector<int> A)
{
  unordered_set<int> s;
  for (int i = 0; i < N; i++)
    s.insert(A[i]);
  return s.size();
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
    vector<int> A(N);
    for (int i_A = 0; i_A < N; i_A++)
      cin >> A[i_A];

    int out_;
    out_ = solve(N, A);
    cout << out_;
    cout << "\n";
  }
}