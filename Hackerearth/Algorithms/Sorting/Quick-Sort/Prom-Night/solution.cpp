#include <bits/stdc++.h>

using namespace std;

#define ll long long int

int main()
{
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);
  int test;
  cin >> test;
  while (test--)
  {
    int m, n;
    cin >> n >> m;
    int arr1[n], arr2[m];
    for (int i = 0; i < n; i++)
      cin >> arr1[i];

    for (int i = 0; i < m; i++)
      cin >> arr2[i];

    sort(arr1, arr1 + n);
    sort(arr2, arr2 + m);

    int i = 0, j = 0;
    while (i < n && j < m)
    {
      if (arr2[j] < arr1[i])
      {
        i++;
        j++;
      }
      else
        j++;
    }

    if (i == n)
      cout << "YES" << "\n";
    else
      cout << "NO" << "\n";
  }

  return 0;
}
