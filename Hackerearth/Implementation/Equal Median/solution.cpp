#include <bits/stdc++.h>

using namespace std;

int main()
{
  int test;
  cin >> test;
  while (test--)
  {
    int index;
    int n;
    cin >> n;
    long long arr[n];
    long long arr2[n];
    long long arr12[2 * n];

    for (int i = 0; i < n; i++)
    {
      cin >> arr[i];
      arr12[i] = arr[i];
    }

    for (int i = 0; i < n; i++)
    {
      cin >> arr2[i];
      arr12[i + n] = arr2[i];
    }

    sort(arr12, arr12 + (2 * n));
    sort(arr, arr + n);
    sort(arr2, arr2 + n);

    if (arr12[n - 1] != arr12[n])
    {
      cout << -1 << "\n";
      continue;
    }

    int prev = 0;
    for (int i = n - 1; i >= 1; i--)
    {
      if (arr12[i] == arr12[i - 1])
      {
        prev++;
      }
      else
      {
        break;
      }
    }

    int last = 0;
    for (int i = n; i < 2 * n - 1; i++)
    {
      if (arr12[i] == arr12[i + 1])
      {

        last++;
      }
      else
      {
        break;
      }
    }

    int min = n;
    int k = 0;
    int h = 0;
    int y;

    for (int i = 0; i < n; i++)
    {
      if (arr[i] == arr12[n - 1])
      {
        k++;
        if (k == 1)
        {
          y = i;
        }

        if (arr2[(n - 1 - i)] == arr12[n - 1])
        {
          if (min > abs(n / 2 - i))
          {
            min = abs(n / 2 - i);
            index = i;
          }
        }
      }
    }

    if (k > 1)
    {
      for (int i = y; i < n - 1; i++)
      {
        if (min > abs(n / 2 - i))
        {
          min = abs(n / 2 - i);
          index = i;
        }
        if (arr[i + 1] != arr[i])
        {
          break;
        }
      }

      int y = count(arr, arr + index, arr12[n - 1]);
      int t = 1;
      if (y > prev)
      {
        t = 0;
        min += y - prev;
      }

      if (t)
      {
        y = count(arr + index + 1, arr + n, arr12[n - 1]);
        if (y > last)
        {
          min += y - last;
        }
      }
    }
    else
    {
      for (int i = 0; i < n - 1; i++)
      {
        if (arr2[i] == arr2[i + 1] && arr2[i] == arr12[n - 1])
        {
          if (min >= abs(n / 2 - i))
          {
            h = 1;
            min = abs(n / 2 - i);
            index = i;
            if (i < n / 2)
            {
              min--;
              index++;
            }
          }
        }
      }

      int y = count(arr2, arr2 + index, arr12[n - 1]);
      int t = 1;
      if (h)
      {
        if (y > prev)
        {
          t = 0;
          min += y - prev;
        }

        if (t)
        {
          y = count(arr2 + index + 1, arr2 + n, arr12[n - 1]);
          if (y > last)
          {
            min += y - last;
          }
        }
      }
    }
    cout << min << "\n";
  }
}