#include <bits/stdc++.h>
using namespace std;

string solve(int n, vector<int> arr)
{
  map<int, int, greater<int>> m;

  for (auto it : arr)
    m[it]++;

  int a = 0, b = 0, f = 1;
  for (auto it : m)
  {
    if (it.second == 1)
    {
      if (f)
      {
        a += it.first;
        f = 0;
      }
      else
      {
        f = 1;
        b += it.first;
      }
    }
  }
  for (auto it : m)
  {
    if (it.second == 1)
      continue;
    a += it.first;
    b += it.first;
  }
  return a > b ? "Alex" : "Bob";
}

int main()
{

  ios::sync_with_stdio(0);
  cin.tie(0);
  int T;
  cin >> T;
  for (int t_i = 0; t_i < T; t_i++)
  {
    int n;
    cin >> n;
    vector<int> arr(n);
    for (int i_arr = 0; i_arr < n; i_arr++)
    {
      cin >> arr[i_arr];
    }

    string out_;
    out_ = solve(n, arr);
    cout << out_;
    cout << "\n";
  }
}