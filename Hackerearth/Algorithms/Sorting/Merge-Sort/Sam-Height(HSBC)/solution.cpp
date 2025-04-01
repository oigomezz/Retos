#include <bits/stdc++.h>
using namespace std;

#define endl "\n"

int main()
{
  int t;
  cin >> t;
  while (t--)
  {
    int n, s, low = 0, high = 0;
    cin >> n >> s;
    int arr[n];
    for (int i = 0; i < n; i++)
    {
      cin >> arr[i];
      if (arr[i] > s)
        high++;
      else if (arr[i] < s)
        low++;
    }
    cout << (n - (min(high, low) * 2)) << endl;
  }
  return 0;
}