#include <iostream>
#include <vector>
using namespace std;

int main()
{
  int n, m, b;
  cin >> n >> m;
  cin >> b;

  vector<vector<int>> garden(n, vector<int>(m, 1));

  for (int i = 0; i < b; ++i)
  {
    int x, y;
    cin >> x >> y;
    garden[x][y] = -1;
  }

  int mn = 0, mx = 0;
  for (int i = 0; i < n; ++i)
  {
    int cnt = 0;
    for (int j = 0; j < m; ++j)
    {
      if (garden[i][j] == 1)
      {
        cnt += 1;
      }
      else
      {
        mn += (cnt + 2) / 3;
        mx += (cnt + 1) / 2;
        cnt = 0;
      }
    }
    mn += (cnt + 2) / 3;
    mx += (cnt + 1) / 2;
  }

  cout << mx << " " << mn << endl;

  return 0;
}