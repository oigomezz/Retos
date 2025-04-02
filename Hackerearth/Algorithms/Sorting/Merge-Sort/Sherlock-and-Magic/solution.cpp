#include <bits/stdc++.h>
using namespace std;
#define ll long long int;
const int N = 51;
int t, n;
vector<int> x(N), y(N);
vector<char> dir(N);
vector<pair<double, pair<int, int>>> arr;

void check(int i, int j)
{
  if (dir[i] == dir[j])
    return;
  if (dir[i] > dir[j])
    swap(i, j);
  if (dir[i] == 'E')
  {
    int d = x[j] - x[i];
    if (d < 0)
      return;
    if (dir[j] == 'W' && y[i] == y[j])
      arr.push_back(make_pair(1.0 * d / 2, make_pair(i, j)));
    else if ((dir[j] == 'N' && y[i] - y[j] == d) || (dir[j] == 'S' && y[j] - y[i] == d))
      arr.push_back(make_pair(d, make_pair(i, j)));
  }
  else if (dir[i] == 'N')
  {
    int d = y[j] - y[i];
    if (d < 0)
      return;
    if (dir[j] == 'S' && x[i] == x[j])
      arr.push_back(make_pair(1.0 * d / 2, make_pair(i, j)));
    else if (dir[j] == 'W' && x[j] - x[i] == d)
      arr.push_back(make_pair(d, make_pair(i, j)));
  }
  else if (dir[i] == 'S')
  {
    int d = x[j] - x[i];
    if (dir[j] == 'W' && d > 0 && d == y[i] - y[j])
      arr.push_back(make_pair(d, make_pair(i, j)));
  }
}

int main()
{
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);
  cout.tie(NULL);
  int t;
  cin >> t;
  while (t--)
  {
    arr.clear();
    cin >> n;
    for (int i = 0; i < n; i++)
      cin >> x[i] >> y[i] >> dir[i];

    for (int i = 0; i < n; i++)
      for (int j = i + 1; j < n; j++)
        check(i, j);

    vector<double> mn(n, 10000000.0);
    sort(arr.begin(), arr.end());
    int avail = n;
    for (int i = 0; i < arr.size(); i++)
    {
      int a = arr[i].second.first;
      int b = arr[i].second.second;
      if (mn[a] < arr[i].first || mn[b] < arr[i].first)
        continue;
      if (mn[a] > arr[i].first)
        avail--;
      if (mn[b] > arr[i].first)
        avail--;
      mn[a] = mn[b] = arr[i].first;
    }
    cout << avail << endl;
  }
  return 0;
}