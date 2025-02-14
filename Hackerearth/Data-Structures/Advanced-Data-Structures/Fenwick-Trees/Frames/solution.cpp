#include <bits/stdc++.h>
using namespace std;

const int MAXN = 2e3 + 3;
int BIT[MAXN];
char mat[MAXN][MAXN];
pair<int, int> dp[MAXN][MAXN], rdp[MAXN][MAXN];
vector<pair<int, int>> top;
vector<int> del[MAXN];
int n, m, MAX;

inline int min(pair<int, int> p)
{
  return min(p.first, p.second);
}

void update(int k, int delta)
{
  while (k <= MAX)
  {
    BIT[k] += delta;
    k += k & -k;
  }
}

int getSum(int k)
{
  int ret = 0;
  while (k > 0)
  {
    ret += BIT[k];
    k -= k & -k;
  }
  return ret;
}

int main()
{

  scanf("%d %d\n", &n, &m);
  for (int i = 1; i <= n; ++i)
  {
    scanf("%s\n", mat[i] + 1);
    for (int j = 1; j <= m; ++j)
    {
      if (mat[i][j] == '0')
      {
        dp[i][j].first = dp[i][j - 1].first + 1;
        dp[i][j].second = dp[i - 1][j].second + 1;
      }
    }
  }
  for (int i = n; i > 0; --i)
  {
    for (int j = m; j > 0; --j)
    {
      if (mat[i][j] == '0')
      {
        rdp[i][j].first = rdp[i][j + 1].first + 1;
        rdp[i][j].second = rdp[i + 1][j].second + 1;
      }
    }
  }

  int x, y, pos;
  MAX = min(m, n);
  top.push_back(pair<int, int>(1, 1));
  for (int i = 2; i <= n; ++i)
    top.push_back(pair<int, int>(i, 1));
  for (int i = 2; i <= m; ++i)
    top.push_back(pair<int, int>(1, i));
  long long res = 0;
  for (int i = 0; i < top.size(); ++i)
  {
    x = top[i].first, y = top[i].second;
    pos = 0;
    memset(BIT, 0, sizeof(BIT));
    for (int j = 1; j <= MAX; ++j)
      del[j].clear();
    while (x <= n && y <= m)
    {
      pos++;
      for (int j = 0; j < del[pos].size(); ++j)
      {
        update(del[pos][j], -1);
      }
      if (mat[x][y] == '0')
      {
        del[pos + min(rdp[x][y])].push_back(pos);
        update(pos, 1);
        res += getSum(pos) - getSum(pos - min(dp[x][y]) - 1);
      }
      x++;
      y++;
    }
  }
  cout << res;
}