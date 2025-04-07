#include <bits/stdc++.h>
using namespace std;
int main()
{
  int t;
  cin >> t;
  while (t--)
  {
    int n, k;
    cin >> n >> k;

    string s;
    cin >> s;
    map<char, vector<int>> m;

    for (int i = 0; i < n; i++)
      m[s[i]].push_back(i);

    if (m[s[0]].size() >= k)
    {
      if (m.size() >= k)
        cout << "YES\n";
      else
        cout << "NO\n";
    }
    else
      cout << "NO\n";
  }
}