#include <bits/stdc++.h>

using namespace std;

const int INF = 1e9;
const int N = 4031;

int d[N];
int ptr[N];

struct edge
{
  int a, b, cap, flow;
};

vector<edge> e;
vector<int> g[N];
int s, t;
int n, m;
int c[50][50], v[50][50], b[50][50];

void add_edge(int a, int b, int cap)
{
  edge e1 = {a, b, cap, 0};
  g[a].push_back(e.size());
  e.push_back(e1);
  edge e2 = {b, a, 0, 0};
  g[b].push_back(e.size());
  e.push_back(e2);
}

int bfs()
{
  for (int i = 0; i < N; i++)
  {
    d[i] = -1;
  }
  queue<int> qu;
  qu.push(s);
  d[s] = 0;
  while (qu.size())
  {
    int v = qu.front();
    qu.pop();
    for (int i = 0; i < g[v].size(); i++)
    {
      int id = g[v][i];
      int to = e[id].b;
      if (e[id].flow == e[id].cap)
        continue;
      if (d[to] != -1)
        continue;
      d[to] = d[v] + 1;
      qu.push(to);
    }
  }
  return (d[t] != -1);
}

int dfs(int v, int flow)
{
  if (v == t || flow == 0)
    return flow;
  for (; ptr[v] < g[v].size(); ptr[v]++)
  {
    int id = g[v][ptr[v]];
    int to = e[id].b;
    if (d[to] != d[v] + 1)
      continue;
    int pushed = dfs(to, min(flow, e[id].cap - e[id].flow));
    if (pushed)
    {
      e[id].flow += pushed;
      e[id ^ 1].flow -= pushed;
      return pushed;
    }
  }
  return 0;
}

int dinic()
{
  int flow = 0;
  while (true)
  {
    if (!bfs())
      break;
    for (int i = 0; i < N; i++)
      ptr[i] = 0;
    while (true)
    {
      int pushed = dfs(s, 100000000);
      if (pushed == 0)
        break;
      flow += pushed;
    }
  }
  return flow;
}

int get_ps(int a, int b)
{
  return a * m + b;
}

int paired(int x)
{
  if (x >= 1000)
    return x - 1000;
  return x + 1000;
}

bool outside(int a, int b)
{
  return (a < 0 || a >= n || b < 0 || b >= m);
}

int main()
{
  ios_base::sync_with_stdio(0);

  cin >> n >> m;

  for (int i = 0; i < n; i++)
  {
    for (int j = 0; j < m; j++)
    {
      cin >> v[i][j];
    }
  }
  for (int i = 0; i < n; i++)
  {
    for (int j = 0; j < m; j++)
    {
      cin >> b[i][j];
    }
  }
  for (int i = 0; i < n; i++)
  {
    for (int j = 0; j < m; j++)
    {
      cin >> c[i][j];
    }
  }

  int can_get = 0;

  s = N - 2;
  t = N - 1;

  for (int i = 0; i < n; i++)
  {
    for (int j = 0; j < m; j++)
    {
      can_get += v[i][j];

      int ps = get_ps(i, j);

      add_edge(ps, paired(ps), v[i][j]);

      if (i % 2 != j % 2)
      {
        add_edge(s, ps, c[i][j]);
        add_edge(paired(ps), t, min(b[i][j], v[i][j]));
        for (int di = -1; di <= 1; di++)
        {
          for (int dj = -1; dj <= 1; dj++)
          {
            if (abs(di) + abs(dj) != 1)
              continue;
            if (outside(i + di, j + dj))
              continue;
            int V = get_ps(i + di, j + dj);
            add_edge(ps, V, INF);
            add_edge(paired(ps), paired(V), INF);
          }
        }
      }
      else
      {
        add_edge(s, ps, min(b[i][j], v[i][j]));
        add_edge(paired(ps), t, c[i][j]);
      }
    }
  }

  cout << can_get - dinic() << endl;

  return 0;
}