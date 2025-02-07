#include <bits/stdc++.h>
using namespace std;

#define ll long long
#define sp ios_base::sync_with_stdio(false), cin.tie(NULL), cout.tie(NULL)
#define cps CLOCKS_PER_SEC
#define mod (ll)1000000007
#define f first
#define s second
#define debug1(x) cerr << x << "\n"
#define debug2(x, y) cerr << x << " " << y << "\n"
#define debug3(x, y, z) cerr << x << " " << y << " " << z << "\n"
#define nl cerr << "\n";
#define pq priority_queue

#define test cerr << "abcd\n";
#define pi pair<ll, int>
#define pii pair<int, pi>
#define pb push_back
#define mxn 500005

ll inf = -10000000000000000LL;

struct node
{
  ll sum, pref, suff, ans;
  node()
  {
    sum = inf;
    pref = inf;
    suff = inf;
    ans = inf;
  }
};
node tree[4 * mxn];

node combine(node a, node b)
{
  node x;
  x.sum = max(inf, a.sum + b.sum);
  x.pref = max(inf, max(a.pref, a.sum + b.pref));
  x.suff = max(inf, max(b.suff, b.sum + a.suff));
  x.ans = max(inf, max(max(a.ans, b.ans), a.suff + b.pref));
  return x;
}

void update(int i, int l, int r, int pos, ll val)
{
  if (l == r)
  {
    tree[i].sum = val;
    tree[i].ans = val;
    tree[i].pref = val;
    tree[i].suff = val;
    return;
  }
  int m = (l + r) / 2;
  if (pos >= l && pos <= m)
    update(i + i, l, m, pos, val);
  else
    update(i + i + 1, m + 1, r, pos, val);
  tree[i] = combine(tree[i + i], tree[i + i + 1]);
}

int main()
{
  sp;
  int n, q;
  cin >> n >> q;
  ll k, mn = inf, ans[q];
  pi a[n], qq[q];
  for (int i = 0; i < n; ++i)
  {
    cin >> a[i].f;
    a[i].s = i;
    mn = min(mn, a[i].f);
  }

  for (int i = 0; i < q; ++i)
  {
    cin >> qq[i].f;
    qq[i].s = i;
  }
  sort(a, a + n);
  sort(qq, qq + q);

  int id, y = 0;
  for (int i = 0; i < 4 * mxn; ++i)
    tree[i] = node();
  for (int i = 0; i < q; ++i)
  {
    k = qq[i].f;
    id = qq[i].s;
    if (k < mn)
    {
      ans[id] = inf;
      continue;
    }
    while (y < n && a[y].f <= k)
    {
      update(1, 1, n, a[y].s + 1, a[y].f);
      ++y;
    }
    ans[id] = tree[1].ans;
  }
  for (int i = 0; i < q; ++i)
  {
    if (ans[i] == inf)
      cout << "No Solution\n";
    else
      cout << ans[i] << "\n";
  }
  return 0;
}