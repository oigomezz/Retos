#include <bits/stdc++.h>
using namespace std;
int solution(int N, string S)
{
  int ans, ct;
  ans = 0;
  ct = 0;
  for (auto ch : S)
  {
    if (ch == '0')
      ct = 0;
    else
    {
      ct++;
      ans = max(ans, ct);
    }
  }
  return ans;
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
    string S;
    cin >> S;

    int out_;
    out_ = solution(N, S);
    cout << out_;
    cout << "\n";
  }
}