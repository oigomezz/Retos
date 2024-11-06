#include <bits/stdc++.h>
using namespace std;
int lft[2250150], rgt[2250150], cnt = 0;
vector<pair<int, int>> queriesY[20005];
vector<int> pointsY[20005];
vector<pair<pair<int, int>, pair<int, int>>> queries;

struct datos
{
  int n;
  unsigned long long sumx2, sumy2, sumx, sumy;
  datos()
  {
    n = sumx = sumy = sumx2 = sumy2 = 0;
  }
  datos(int x, int y)
  {
    n = 1, sumx = x, sumx2 = x * x, sumy = y, sumy2 = y * y;
  }
  datos operator+(const datos &D) const
  {
    datos ret;
    ret.n = n + D.n;
    ret.sumx = sumx + D.sumx;
    ret.sumx2 = sumx2 + D.sumx2;
    ret.sumy = sumy + D.sumy;
    ret.sumy2 = sumy2 + D.sumy2;
    return ret;
  }
  datos operator-(const datos &D) const
  {
    datos ret;
    ret.n = n - D.n;
    ret.sumx = sumx - D.sumx;
    ret.sumx2 = sumx2 - D.sumx2;
    ret.sumy = sumy - D.sumy;
    ret.sumy2 = sumy2 - D.sumy2;
    return ret;
  }
} tree[2250150];

datos bit[20005];
map<pair<int, int>, datos> store[20005];
void update(int pos, const datos &D)
{
  for (; pos < 20005; pos += (pos & (-pos)))
    bit[pos] = bit[pos] + D;
}

datos get(int i)
{
  datos ret;
  for (; i; i -= (i & -i))
    ret = ret + bit[i];
  return ret;
}

datos get(int l, int r)
{
  return get(r) - get(l - 1);
}

void insert(int x, int y)
{
  datos D = datos(x, y);
  update(y, D);
}

unsigned long long get_ans(datos D)
{
  return D.sumx + D.sumy + 3 * (D.n * (D.sumx2 + D.sumy2) - D.sumx * D.sumx - D.sumy * D.sumy);
}

datos query(int x1, int y1, int x2, int y2)
{
  return store[x2][{y1, y2}] - store[x1 - 1][{y1, y2}];
}

void yes(int x, int y)
{
  assert(x >= 1 && x <= 20000 && y >= 1 && y <= 20000);
}

int main()
{
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);
  cout.tie(NULL);
  int p, q;
  cin >> p >> q;
  for (int i = 1; i <= p; i++)
  {
    int x, y;
    cin >> x >> y;
    yes(x, y);
    pointsY[x].push_back(y);
  }
  for (int i = 1; i <= q; i++)
  {
    int a, b, c, d;
    cin >> a >> c >> b >> d;
    yes(a, b);
    yes(c, d);
    queries.push_back({{a, b}, {c, d}});
    queriesY[a - 1].push_back({b, d});
    queriesY[c].push_back({b, d});
  }
  for (int x = 0; x < 20005; x++)
  {
    for (int y : pointsY[x])
      insert(x, y);
    for (auto y : queriesY[x])
      store[x][y] = get(y.first, y.second);
  }
  for (auto it : queries)
    cout << get_ans(query(it.first.first, it.first.second, it.second.first, it.second.second)) << endl;
}