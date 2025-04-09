#include <bits/stdc++.h>
using namespace std;

int main()
{
  ios::sync_with_stdio(false);
  cin.tie(0);
  cout.tie(0);
  int t;
  cin >> t;
  while (t--)
  {
    int number;
    cin >> number;
    if (number >= 28 && 2 <= number % 14 && number % 14 <= 12)
      cout << number / 14 << "\n";
    else if (number == 21)
      cout << 1 << "\n";
    else
      cout << "-1" << "\n";
  }
  return 0;
}