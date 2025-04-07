#include <bits/stdc++.h>

using namespace std;

int emptyGame(int n, vector<int> &a)
{
  // Intializing the variable 'count'
  int count = 0;

  // Sort the array 'A'.
  sort(a.begin(), a.end());

  while (!a.empty())
  {
    if (a.size() >= 2 && a[a.size() - 1] - a[a.size() - 2] <= 2)
    {
      a.pop_back();
      a.pop_back();
    }
    else
      a.pop_back();
    count++;
  }

  return count;
}

int main()
{
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);
  int t;
  cin >> t;
  while (t--)
  {
    int n;
    cin >> n;
    vector<int> a(n);
    for (auto &ele : a)
      cin >> ele;
    cout << emptyGame(n, a) << "\n";
  }
}