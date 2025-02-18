#include <bits/stdc++.h>
#define lli long long int
#define llu unsigned long long int
#define ld long double
#define all(v) v.begin(), v.end()
#define pb push_back
#define mp make_pair
#define F first
#define S second
#define si(n) scanf("%d", &n)
#define slli(n) scanf("%lld", &n);
#define ss(n) scanf("%s", n);

const lli MOD = 1000000007ll;
int INF = (int)1e9;

using namespace std;

lli bit_count(lli _x)
{
  lli _ret = 0;
  while (_x)
  {
    if (_x % 2 == 1)
      _ret++;
    _x /= 2;
  }
  return _ret;
}
lli bit(lli _mask, lli _i) { return (_mask & (1ll << _i)) == 0 ? 0 : 1; }
lli powermod(lli _a, lli _b, lli _m = MOD)
{
  lli _r = 1;
  while (_b)
  {
    if (_b % 2 == 1)
      _r = (_r * _a) % _m;
    _b /= 2;
    _a = (_a * _a) % _m;
  }
  return _r;
}
lli add(lli a, lli b, lli m = MOD)
{
  lli x = a + b;
  while (x >= m)
    x -= m;
  while (x < 0)
    x += m;
  return x;
}
lli sub(lli a, lli b, lli m = MOD)
{
  lli x = a - b;
  while (x < 0)
    x += m;
  while (x >= m)
    x -= m;
  return x;
}
lli mul(lli a, lli b, lli m = MOD)
{
  lli x = a * 1ll * b;
  x %= m;
  while (x < 0)
    x += m;
  return x;
}

struct SegtreeNode
{
  int l, r, best, sz;
};

struct Segtree
{
  typedef SegtreeNode stt;
  static const int MAXN = 4000010;
  stt Segtree[4 * MAXN];

  stt MergeSegTree(stt a, stt b)
  {
    stt temp;

    temp.sz = a.sz + b.sz;
    if (a.l == a.sz)
      temp.l = a.sz + b.l;
    else
      temp.l = a.l;
    if (b.r == b.sz)
      temp.r = b.sz + a.r;
    else
      temp.r = b.r;
    temp.best = max(a.best, b.best);
    temp.best = max(temp.best, a.r + b.l);

    return temp;
  }

  void BuildSegTree(int s, int e, int idx)
  {
    if (s == e)
    {
      Segtree[idx].l = Segtree[idx].r = 0;
      Segtree[idx].best = 0;
      Segtree[idx].sz = 1;
    }
    else
    {
      int mid = (s + e) >> 1;
      BuildSegTree(s, mid, 2 * idx + 1);
      BuildSegTree(mid + 1, e, 2 * idx + 2);
      Segtree[idx] = MergeSegTree(Segtree[2 * idx + 1], Segtree[2 * idx + 2]);
    }
  }

  void UpdateSegTree(int s, int e, int x, int idx)
  {
    if (s == e)
    {
      Segtree[idx].l = Segtree[idx].r = 1;
      Segtree[idx].best = 1;
      Segtree[idx].sz = 1;
      return;
    }
    int mid = (s + e) >> 1;
    if (x <= mid)
      UpdateSegTree(s, mid, x, 2 * idx + 1);
    else
      UpdateSegTree(mid + 1, e, x, 2 * idx + 2);
    Segtree[idx] = MergeSegTree(Segtree[2 * idx + 1], Segtree[2 * idx + 2]);
  }

  stt QuerySegTree(int s, int e, int x, int y, int idx)
  {
    if (s == x && e == y)
      return Segtree[idx];
    int mid = (s + e) >> 1;
    if (y <= mid)
      return QuerySegTree(s, mid, x, y, 2 * idx + 1);
    if (x > mid)
      return QuerySegTree(mid + 1, e, x, y, 2 * idx + 2);
    return MergeSegTree(QuerySegTree(s, mid, x, mid, 2 * idx + 1), QuerySegTree(mid + 1, e, mid + 1, y, 2 * idx + 2));
  }
};

int N, M, Q;
string S[2010];
vector<int> next1[2010];
int x1[1000010], yy1[1000010], x2[1000010], y2[1000010];
vector<int> queries[2010][2010];
vector<int> dothis[2010];
int ans[1000010];
Segtree stt;

int main()
{
  cin >> N >> M;
  for (int i = 1; i <= N; i++)
  {
    cin >> S[i];
    S[i] = ' ' + S[i];
    next1[i].resize(M + 1);
  }
  cin >> Q;
  for (int i = 1; i <= Q; i++)
  {
    cin >> x1[i] >> yy1[i] >> x2[i] >> y2[i];
    queries[x1[i]][x2[i]].pb(i);
  }

  for (int j = 1; j <= M; j++)
  {
    int prev = INF;
    for (int i = N; i >= 1; i--)
    {
      if (S[i][j] == '1')
        prev = i;
      next1[i][j] = prev;
    }
  }

  for (int i1 = 1; i1 <= N; i1++)
  {
    for (int i = i1; i <= N; i++)
      dothis[i].clear();
    for (int j = 1; j <= M; j++)
      if (next1[i1][j] <= N)
        dothis[next1[i1][j]].pb(j);
    stt.BuildSegTree(1, M, 0);
    for (int i2 = i1; i2 <= N; i2++)
    {
      for (int idx : dothis[i2])
        stt.UpdateSegTree(1, M, idx, 0);
      for (int q : queries[i1][i2])
        ans[q] = stt.QuerySegTree(1, M, yy1[q], y2[q], 0).best * (x2[q] - x1[q] + 1);
    }
  }

  for (int i = 1; i <= Q; i++)
    cout << ans[i] << "\n";

  return 0;
}