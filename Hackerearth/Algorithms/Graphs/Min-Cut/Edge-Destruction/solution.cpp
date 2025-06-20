#include <bits/stdc++.h>
using namespace std;
const int maxN = 1007;
const int maxM = 8e5 + 7;
const int VCL = 1e9 + 7;

vector<int> Adj[maxN], Nadj[maxN];
struct Canh
{
  int to, dis, cost;
} E[maxM];
int n, m;
int D[maxN], Last[maxN];
vector<int> F[2];

int Capp[maxN][maxN], Flow[maxN][maxN];

inline void Dijkstra(int s, vector<int> &D)
{
  D.resize(n + 1, VCL);
  D[s] = 0;
  set<pair<int, int>> S;
  S.insert({0, s});
  while (S.size())
  {
    int w = S.begin()->first;
    int u = S.begin()->second;
    S.erase(S.begin());
    if (w > D[u])
      continue;
    for (auto i : Adj[u])
    {
      int v = E[i].to;
      int w = D[u] + E[i].dis;
      if (w < D[v])
      {
        D[v] = w;
        S.insert({D[v], v});
      }
    }
  }
}

inline bool BFS()
{
  for (int i = 1; i <= n; ++i)
    D[i] = VCL;
  D[1] = 0;
  queue<int> Q;
  Q.push(1);
  while (Q.size())
  {
    int u = Q.front();
    Q.pop();
    if (u == n)
      return true;
    for (auto i : Nadj[u])
    {
      int v = E[i].to;
      if (Capp[u][v] > Flow[u][v] && D[v] > D[u] + 1)
      {
        D[v] = D[u] + 1;
        Q.push(v);
      }
    }
  }
  return false;
}

inline int DFS(int u, int f)
{
  if (u == n)
    return f;
  for (int &i = Last[u]; i < (int)Nadj[u].size(); ++i)
  {
    int v = E[Nadj[u][i]].to;
    if (D[v] == D[u] + 1 && Capp[u][v] > Flow[u][v])
    {
      int df = DFS(v, min(f, Capp[u][v] - Flow[u][v]));
      if (df > 0)
      {
        Flow[u][v] += df;
        Flow[v][u] -= df;
        return df;
      }
    }
  }
  return 0;
}

inline int Dicnic()
{
  int ans = 0;
  while (BFS())
  {
    for (int i = 1; i <= n; ++i)
      Last[i] = 0;
    do
    {
      int df = DFS(1, VCL);
      if (df > 0)
        ans += df;
      else
        break;
    } while (true);
  }
  return ans;
}

int main()
{
  ios_base::sync_with_stdio(false);
  cin >> n >> m;
  for (int i = 0; i < m; ++i)
  {
    int u, v, d, c;
    cin >> u >> v >> d >> c;
    int j = i << 1;
    E[j] = {v, d, c};
    Adj[u].push_back(j);
    j |= 1;
    E[j] = {u, d, c};
    Adj[v].push_back(j);
  }

  Dijkstra(1, F[0]);
  Dijkstra(n, F[1]);

  for (int u = 1; u <= n; ++u)
  {
    Nadj[u].clear();
    for (auto i : Adj[u])
    {
      int v = E[i].to;
      if (F[0][u] + E[i].dis + F[1][v] == F[0][n])
      {
        Nadj[u].push_back(i);
        Capp[u][v] = E[i].cost;
        Flow[u][v] = 0;
        Capp[v][u] = 0;
        Flow[v][u] = 0;
      }
    }
  }

  cout << Dicnic() << endl;
  return 0;
}