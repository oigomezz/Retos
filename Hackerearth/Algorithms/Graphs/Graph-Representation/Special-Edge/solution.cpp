#include <bits/stdc++.h>
#define int long long
using namespace std;

const int MAX_N = 2e5 + 121;
vector<pair<int, int>> gr[MAX_N];
vector<pair<int, int>> graph[MAX_N];
int n, m;
int a[MAX_N];
int V[MAX_N], U[MAX_N];
bool used[MAX_N];
bool usedEdge[MAX_N];
int color[MAX_N];
int cntColor;
long long sum;
long long sumAColor[MAX_N];
long long dp[MAX_N];
vector<int> vec;
map<pair<int, int>, int> mp;

long long result;
int num;
int A, B;

void dfs(int v, int numEdge = 0)
{
  used[v] = 1;
  vec.push_back(v);
  usedEdge[numEdge] = 1;
  for (int i = 0; i < gr[v].size(); ++i)
  {
    int to = gr[v][i].first;
    int numEdge_ = gr[v][i].second;
    if (!used[to])
      dfs(to, numEdge_);
  }
}

void dfs2(int v)
{
  color[v] = cntColor;
  for (int i = 0; i < gr[v].size(); ++i)
  {
    int to = gr[v][i].first;
    int numEdge = gr[v][i].second;
    if (!usedEdge[numEdge] && color[to] == 0)
      dfs2(to);
  }
}

inline void addEdge(int v, int u, int index)
{
  if (!mp[{v, u}])
  {
    graph[v].push_back({u, index});
    mp[{v, u}] = 1;
  }
}

void dfs3(int v, int father)
{
  used[v] = 1;
  dp[v] = sumAColor[v];
  sum += sumAColor[v];
  for (int i = 0; i < graph[v].size(); ++i)
  {
    int to = graph[v][i].first;
    if (to != father)
    {
      dfs3(to, v);
      dp[v] += dp[to];
    }
  }
}

bool cmp(int a, int b, int c, int d)
{
  return (a < c || (a == c && b < d));
}

void updAnswer(int u, int v, long long res)
{
  if (u > v)
    swap(v, u);
  if (res > result || (res == result && cmp(u, v, A, B)))
  {
    result = res;
    A = u;
    B = v;
  }
}

void dfs4(int vertex, int father, int indexEdge = 0)
{
  if (indexEdge != 0)
    updAnswer(U[indexEdge], V[indexEdge], dp[vertex] * 1ll * (sum - dp[vertex]));

  for (int i = 0; i < graph[vertex].size(); ++i)
  {
    int to = graph[vertex][i].first;
    if (to != father)
      dfs4(to, vertex, graph[vertex][i].second);
  }
}

main()
{
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);
  cout.tie(NULL);
  cin >> n >> m;
  for (int i = 1; i <= n; ++i)
    cin >> a[i];

  A = n + 1;
  B = n + 1;

  for (int i = 1; i <= m; ++i)
  {
    ++num;
    cin >> V[num] >> U[num];
    V[num + 1] = V[num];
    U[num + 1] = U[num];
    ++num;
    gr[V[num]].push_back({U[num], num - 1});
    gr[U[num]].push_back({V[num], num});
  }

  for (int i = 1; i <= n; ++i)
    if (!used[i])
      dfs(i);

  for (int i = 1; i <= n; ++i)
  {
    if (!color[vec[i - 1]])
    {
      ++cntColor;
      dfs2(vec[i - 1]);
    }
  }

  for (int i = 1; i <= n; ++i)
  {
    sumAColor[color[i]] += a[i];
    for (int j = 0; j < gr[i].size(); ++j)
    {
      int v = i;
      int u = gr[i][j].first;
      if (color[v] != color[u])
        addEdge(color[v], color[u], gr[i][j].second);
    }
  }

  for (int i = 1; i <= cntColor; ++i)
    used[i] = 0;

  for (int i = 1; i <= cntColor; ++i)
  {
    if (!used[i])
    {
      sum = 0;
      dfs3(i, 0);
      dfs4(i, 0);
    }
  }

  cout << A << ' ' << B << endl;

  return 0;
}