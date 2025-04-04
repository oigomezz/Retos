#include <cstdio>
#include <algorithm>
#include <queue>
using namespace std;
#define md ((s + e) >> 1)

typedef long long ll;
const ll MAXR = 1e5 + 3;

struct Node
{
  Node *l, *r;
  ll sum;
} tree[10000007], *root[200005];
int used;

Node *build(int s, int e)
{
  Node *ret = &tree[++used];
  if (s == e)
    return ret;
  ret->l = build(s, md);
  ret->r = build(md + 1, e);
  return ret;
}

Node *update(Node *now, int i, int v, int s = 0, int e = MAXR)
{
  if (e < i || i < s)
    return now;
  Node *ret = &tree[++used];
  if (s == e)
  {
    ret->sum = now->sum + v;
    return ret;
  }
  ret->l = update(now->l, i, v, s, md);
  ret->r = update(now->r, i, v, md + 1, e);
  ret->sum = ret->l->sum + ret->r->sum;
  return ret;
}

ll find(Node *now, int l, int r, int s = 0, int e = MAXR)
{
  if (r < s || e < l)
    return 0;
  if (l <= s && e <= r)
    return now->sum;
  return find(now->l, l, r, s, md) + find(now->r, l, r, md + 1, e);
}

struct Edge
{
  int a, b, c;
  bool operator<(const Edge &o) const
  {
    return c < o.c;
  }
} edge[200005];

int p[200005];
int val[200005];

int find(int a)
{
  if (a == p[a])
    return a;
  return p[a] = find(p[a]);
}

bool merge(Edge e)
{
  int a = e.a, b = e.b, c = e.c;
  a = find(a), b = find(b);
  if (a == b)
    return 0;
  if (val[a] > val[b])
    swap(a, b);
  root[c] = update(root[c], val[b], val[b]);
  p[b] = a;
  return 1;
}

vector<int> compress;
ll psum[200005];
int main()
{
  int N, Q;
  scanf("%d %d", &N, &Q);

  for (int i = 0; i < N - 1; i++)
  {
    int a, b, c;
    scanf("%d %d %d", &a, &b, &c);
    edge[i] = {a, b, c};
    compress.push_back(c);
  }
  compress.push_back(-1);
  sort(compress.begin(), compress.end());
  compress.erase(unique(compress.begin(), compress.end()), compress.end());
  for (int i = 0; i < N - 1; i++)
  {
    edge[i].c = lower_bound(compress.begin(), compress.end(), edge[i].c) - compress.begin();
  }
  sort(edge, edge + N - 1);

  ll tot = 0;
  for (int i = 1; i <= N; i++)
  {
    p[i] = i;
    scanf("%d", val + i);
    tot += val[i];
    psum[val[i]] += val[i];
  }
  for (int i = 1; i <= MAXR; i++)
    psum[i] += psum[i - 1];

  root[0] = build(0, MAXR);
  for (int i = 0; i < N - 1;)
  {
    int c = edge[i].c;
    root[c] = root[c - 1];
    while (i < N - 1 && edge[i].c == c)
    {
      merge(edge[i++]);
    }
  }

  ll ans = 0;
  while (Q--)
  {
    ll D, T, X;
    scanf("%lld %lld %lld", &D, &T, &X);
    D ^= ans;
    T ^= ans;
    X ^= ans;
    D = upper_bound(compress.begin(), compress.end(), D) - compress.begin() - 1;
    if (T == 0)
      ans = 0;
    else
      ans = (tot - psum[min((X - 1) / T, MAXR)] - find(root[D], min((X + T - 1) / T, MAXR), MAXR)) * T;
    printf("%lld\n", ans);
  }
}