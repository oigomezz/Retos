#include <bits/stdc++.h>
#include <iostream>

using namespace std;

int main()
{
  int t;
  cin >> t;
  while (t--)
  {
    int n;
    cin >> n;
    int m;
    cin >> m;
    int arr[n];
    for (int i = 0; i < n; i++)
      cin >> arr[i];

    int diff = n - m;
    for (int i = 0; i < n - 1; i++)
    {
      bool swapped = false;
      for (int j = 0; j < n - 1; j++)
      {
        if (arr[j] > arr[j + 1])
        {
          swap(arr[j], arr[j + 1]);
          swapped = true;
        }
      }
      if (swapped == false)
        break;
    }

    int maxsum = 0;
    int minsum = 0;
    for (int i = 0; i < diff; i++)
      minsum = minsum + arr[i];

    for (int i = n - 1; i >= n - diff; i--)
      maxsum = maxsum + arr[i];

    int d = (maxsum - minsum);
    cout << d << endl;
  }
}