#include <bits/stdc++.h>
using namespace std;

int main()
{
  ios_base::sync_with_stdio(0);
  cin.tie(0);

  map<pair<int, int>, int> frequencyMap;
  string directions;
  cin >> directions;
  int x = 0, y = 0;

  for (int i = 0; i < directions.size() + 1; i++)
  {
    frequencyMap[{x, y}]++;
    if (directions[i] == 'L')
      y--;
    else if (directions[i] == 'R')
      y++;
    else if (directions[i] == 'U')
      x--;
    else if (directions[i] == 'D')
      x++;
  }

  int duplicates = 0;
  for (auto it : frequencyMap)
    if (it.second > 1)
      duplicates += it.second - 1;

  cout << duplicates << endl;

  return 0;
}