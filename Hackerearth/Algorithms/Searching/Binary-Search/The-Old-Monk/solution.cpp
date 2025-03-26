#include <bits/stdc++.h>
using namespace std;
int main()
{
  int t;
  cin >> t;
  while (t--)
  {
    long long a;
    cin >> a;
    long long a1[a], b1[a];
    for (int i = 0; i < a; i++)
      cin >> a1[i];

    for (int i = 0; i < a; i++)
      cin >> b1[i];

    int ans = 0;
    int i = 0;
    int j = 0;
    while (j < a && i < a)
    {
      if (b1[j] >= a1[i])
      {
        ans = max(ans, j - i);
        j++;
      }
      else
        i++;
    }
    cout << ans << endl;
  }
  return 0;
}