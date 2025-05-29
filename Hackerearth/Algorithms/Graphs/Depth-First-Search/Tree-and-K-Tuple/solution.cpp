#include <bits/stdc++.h>
using namespace std;

const int maxn = 100009;
const int mod = 1000000007;
vector<pair<int, int>> arr;

int add(int a, int b)
{
  a += b;
  if (a >= mod)
    a -= mod;
  return a;
}

struct bit
{
  int tree[maxn];

  bit()
  {
    memset(tree, 0, sizeof(tree));
  }

  void update(int idx, int val)
  {
    for (int x = idx; x < maxn; x += (x & -x))
      tree[x] = add(tree[x], val);
  }

  int sum(int idx)
  {
    int ret = 0;
    for (int x = idx; x > 0; x -= (x & -x))
      ret = add(ret, tree[x]);
    return ret;
  }
};

bit B[22];

vector<int> edges[maxn];
int in[maxn], out[maxn];
int timer = 1;

void dfs(int u, int p)
{
  in[u] = timer;
  for (auto v : edges[u])
  {
    if (v == p)
      continue;
    timer++;
    dfs(v, u);
  }
  out[u] = timer;
}

int main()
{
  int n, k;
  scanf("%d %d", &n, &k);
  for (int i = 1; i <= n; i++)
  {
    int x;
    scanf("%d", &x);
    arr.push_back(make_pair(x, i));
  }
  sort(arr.begin(), arr.end());
  for (int i = 1; i < n; i++)
  {
    int u, v;
    scanf("%d %d", &u, &v);
    edges[u].push_back(v);
    edges[v].push_back(u);
  }
  dfs(1, 0);
  for (auto i : arr)
  {
    int u = i.second;
    int l = in[u], r = out[u];
    for (int i = k; i >= 1; i--)
    {
      int S = B[i].sum(r) - B[i].sum(l - 1);
      if (S < 0)
        S += mod;
      B[i + 1].update(l, S);
    }
    B[1].update(l, 1);
  }
  int ans = B[k + 1].sum(timer);
  cout << ans << "\n";
  return 0;
}