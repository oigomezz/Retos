#include <bits/stdc++.h>
using namespace std;

#define int long long
#define pb push_back
#define S second
#define F first
#define f(i, n) for (int i = 0; i < n; i++)
#define fast                    \
  ios_base::sync_with_stdio(0); \
  cin.tie(0);                   \
  cout.tie(0)
#define vi vector<int>
#define pii pair<int, int>
#define all(x) x.begin(), x.end()
#define ordered_set tree<int, null_type, less<int>, rb_tree_tag, tree_order_statistics_node_update>
#define precise(x) fixed << setprecision(x)

const int N = 4e4 + 100;
const int LN = 17;

struct node
{
  int count;
  node *left, *right;

  node(int count, node *left, node *right) : count(count), left(left), right(right) {}
};

node *null = new node(0, NULL, NULL);
node *nodes[N];

node *insert(node *old, int l, int r, int val)
{
  if (l > val || r < val)
    return old;

  if (l == r)
    return new node(1, null, null);

  int mid = (l + r) / 2;

  return new node(old->count + 1, insert(old->left, l, mid, val), insert(old->right, mid + 1, r, val));
}

int query(node *a, node *b, node *c, node *d, int l, int r, int k)
{
  if (l == r)
    return l;

  int mid = (l + r) / 2;
  int cn = a->left->count + b->left->count - c->left->count - d->left->count;

  if (cn < k)
    return query(a->right, b->right, c->right, d->right, mid + 1, r, k - cn);
  else
    return query(a->left, b->left, c->left, d->left, l, mid, k);
}

vector<int> g[N], go;
int a[N];
int n, q;

int depth[N], par[N][LN];

map<int, int> cmp;

void dfs(int v)
{
  if (par[v][0] == -1)
  {
    depth[v] = 0;
    nodes[v] = insert(null, 1, n, a[v]);
  }
  else
  {
    depth[v] = depth[par[v][0]] + 1;
    nodes[v] = insert(nodes[par[v][0]], 1, n, a[v]);
  }

  for (auto x : g[v])
    if (x != par[v][0])
    {
      par[x][0] = v;
      dfs(x);
    }
}

int lca(int u, int v)
{
  if (depth[u] > depth[v])
    swap(u, v);

  int diff = depth[v] - depth[u];

  for (int i = 0; i < LN; i++)
    if (diff & (1LL << i))
      v = par[v][i];

  if (u == v)
    return u;

  for (int i = LN - 1; i >= 0; i--)
    if (par[u][i] != par[v][i])
      u = par[u][i], v = par[v][i];

  u = par[u][0];

  return u;
}

// value of node with rank k in path u to v
int get(int u, int v, int k)
{
  int lc = lca(u, v);
  return go[query(nodes[u], nodes[v], nodes[lc], par[lc][0] == -1 ? null : nodes[par[lc][0]], 1, n, k) - 1];
}

void solve()
{
  null->left = null->right = null;
  memset(par, -1, sizeof(par));

  cin >> n >> q;

  for (int i = 1; i <= n; i++)
  {
    cin >> a[i];
  }

  for (int i = 1; i <= n; i++)
    go.push_back(a[i]);

  sort(all(go));

  for (int i = 1; i <= n; i++)
  {
    a[i] = lower_bound(all(go), a[i]) - go.begin() + 1;
  }

  int u, v;

  f(i, n - 1)
  {
    cin >> u >> v;
    g[u].pb(v);
    g[v].pb(u);
  }

  dfs(1);

  for (int i = 0; i < LN - 1; i++)
    for (int j = 1; j <= n; j++)
      if (par[j][i] != -1)
        par[j][i + 1] = par[par[j][i]][i];

  while (q--)
  {
    cin >> u >> v;

    int lc = lca(u, v);
    int tot = depth[u] + depth[v] - depth[lc] - depth[lc] + 1;

    cout << get(u, v, 1) + get(u, v, tot) + get(u, v, (tot + 1) / 2) << ' ';
  }
}

signed main()
{
  fast;
  solve();
}