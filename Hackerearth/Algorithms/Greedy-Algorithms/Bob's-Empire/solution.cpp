#include <bits/stdc++.h>
using namespace std;

int main()
{
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);
  cout.tie(NULL);
  int t;
  cin >> t;
  while (t--)
  {
    int n;
    cin >> n;
    vector<int> abcd;
    int value;
    while (cin >> value)
    {
      abcd.push_back(value);
      if (cin.peek() == '\n')
        break; // Stop reading on new line
    }
    int maxValue = 0;
    for (int j : abcd)
    {
      maxValue = max(maxValue, (n + j - 1) / j);
    }
    cout << maxValue + 3 << endl;
  }
  return 0;
}