#include <bits/stdc++.h>
using namespace std;

#define fr(i, a, b) for (int i = (a), _b = (b); i <= _b; i++)
#define frr(i, a, b) for (int i = (a), _b = (b); i >= _b; i--)
#define rep(i, n) for (int i = 0, _n = (n); i < _n; i++)
#define repr(i, n) for (int i = (n) - 1; i >= 0; i--)
#define foreach(it, ar) for (typeof(ar.begin()) it = ar.begin(); it != ar.end(); it++)
#define fill(ar, val) memset(ar, val, sizeof(ar))

#define uint64 unsigned long long
#define int64 long long
#define all(ar) ar.begin(), ar.end()
#define pb push_back
#define mp make_pair
#define ff first
#define ss second

typedef pair<int, int> ii;
typedef pair<int, ii> iii;
typedef vector<ii> vii;
typedef vector<int> vi;

#define PI 3.1415926535897932385
#define EPS 1e-7
#define MOD 1000000007
#define INF 1500111222
#define MAX 400111
#define MAXK 18

struct BITree
{
  int n;
  vi value;

  BITree(int n)
  {
    this->n = n;
    value = vi(n + 1, 0);
  }

  int get(int lo, int hi)
  {
    return get(hi) - get(lo - 1);
  }

  int get(int i)
  {
    int res = 0;
    while (i > 0)
    {
      res += value[i];
      i -= (-i & i);
    }
    return res;
  }

  void update(int i, int val)
  {
    while (i <= n)
    {
      value[i] += val;
      i += (-i & i);
    }
  }
};

int n, m, a[MAX], p[MAX][MAXK];
int64 inver[MAX];

struct Entry
{
  int id;
  ii val;
  bool operator<(const Entry &en) const
  {
    if (val == en.val)
      return id < en.id;
    return val < en.val;
  }
} L[MAX];

void calSuffix()
{
  int k = 16;
  rep(i, n) p[i][0] = a[i];
  fr(j, 1, k)
  {
    int len = 1 << (j - 1);
    rep(i, n)
    {
      L[i].val.ff = p[i][j - 1];
      L[i].val.ss = (len + len <= n) ? p[(i + len) % n][j - 1] : -1;
      L[i].id = i;
    }
    sort(L, L + n);
    p[L[0].id][j] = 0;
    fr(i, 1, n - 1) p[L[i].id][j] = p[L[i - 1].id][j] + (L[i].val != L[i - 1].val);
  }
}

void solve()
{
  BITree tree(n);
  int64 maxRes = 0, curRes = 0;
  rep(i, n)
  {
    curRes += tree.get(a[i] + 1, n);
    tree.update(a[i], 1);
    a[i + n] = a[i];
  }
  inver[0] = maxRes = curRes;
  for (int i = n, j = 0; j < n - 1; i++, j++)
  {
    curRes -= tree.get(0, a[j] - 1);
    curRes += tree.get(a[i] + 1, n);
    inver[j + 1] = curRes;

    maxRes = max(maxRes, curRes);
  }
  calSuffix();
  int maxIndex = 0;
  rep(i, n)
  {
    int id = L[i].id;
    if (inver[id] == maxRes)
    {
      maxIndex = id;
      break;
    }
  }

  printf("%d %lld\n", maxIndex, maxRes);
}

void compress()
{
  map<int, int> idx;
  rep(i, n) idx[a[i]] = 1;
  int m = 0;
  for (map<int, int>::iterator it = idx.begin(); it != idx.end(); it++)
    it->ss = ++m;
  rep(i, n) a[i] = idx[a[i]];
}

bool compare(int x, int y)
{
  rep(i, n)
  {
    if (a[x] != a[y])
      return a[x] < a[y];
    x = (x + 1) % n;
    y = (y + 1) % n;
  }
  return false;
}

void solveBruteForces()
{
  int64 maxRes = -1;
  int maxIndex = -1;
  rep(x, n)
  {
    BITree tree(n);
    int64 res = 0;
    rep(i, n)
    {
      int id = (x + i) % n;
      res += tree.get(a[id] + 1, n);
      tree.update(a[id], 1);
    }
    if (res > maxRes || (res == maxRes && compare(x, maxIndex)))
    {
      maxRes = res;
      maxIndex = x;
    }
  }
  printf("%d %lld\n", maxIndex, maxRes);
}

int main()
{
  int cases;
  scanf("%d", &cases);
  assert(1 <= cases && cases <= 10);
  while (cases--)
  {
    scanf("%d", &n);
    assert(1 <= n && n <= 1e5);
    rep(i, n)
    {
      scanf("%d", &a[i]);
      assert(1 <= a[i] && a[i] <= 1e9);
    }
    compress();
    solve();
  }
  return 0;
}