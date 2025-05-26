#include "bits/stdc++.h"
using namespace std;

struct Node
{
  long long size = 0;
  long long cumsize = 0;
  long long cumcumsize = 0;
  long long sum_path = 0;
  long long sum_path_from_top = 0;
  int depth = 0;
  int prof = 0;
  int parent = 0;
  int num_1 = 0;
  int jump = 0;
  int path = 0;
  int pos = 0;
  std::vector<int> children;
};

struct Path
{
  int parent;
  int prof;
  std::vector<int> nodes;
};

int N, M;

Node nodes[300000];
int numPaths = 0;
Path paths[300000];

void extractPath(int n, int path)
{
  auto &node = nodes[n];
  node.pos = paths[path].nodes.size();
  paths[path].nodes.push_back(n);
  node.path = path;
  std::sort(node.children.begin(), node.children.end(), [&](int a, int b)
            { return nodes[a].size > nodes[b].size; });
  node.cumsize = node.size + nodes[node.parent].cumsize;
  node.cumcumsize = node.cumsize + nodes[node.parent].cumcumsize;
  if (node.children.size() > 0)
    extractPath(node.children.front(), path);
  for (int i = 1; i < node.children.size(); i++)
  {
    paths[numPaths].parent = n;
    paths[numPaths].prof = paths[path].prof + 1;
    extractPath(node.children[i], numPaths++);
  }
}

int getDepth(int n, int p = 0, int prof = 1)
{
  auto &node = nodes[n];
  node.parent = p;
  int depth = 0;
  for (int &i : node.children)
  {
    if (i == p)
    {
      i = node.children.back();
      break;
    }
  }
  if (p > 0)
  {
    node.children.pop_back();
    node.jump = node.children.size() <= 1 ? nodes[p].jump : n;
    node.num_1 = node.children.size() <= 1 ? 1 + nodes[p].num_1 : 0;
  }
  for (int i : node.children)
    depth = std::max(depth, getDepth(i, n, prof + 1));
  node.depth = depth + 1;
  node.prof = prof;
  return depth + 1;
}

long long getSize(int n)
{
  long long size = 1;
  for (int i : nodes[n].children)
    size += getSize(i);
  nodes[n].size = size;
  return size;
}

long long getSumPath(int n)
{
  long long sum = 0;
  for (int i : nodes[n].children)
    sum += getSumPath(i);
  nodes[n].sum_path = sum;
  return sum + nodes[n].size;
}

void getSumPathFromTop(int n, long long acc = 0)
{
  nodes[n].sum_path_from_top = acc;
  for (int i : nodes[n].children)
    getSumPathFromTop(i, acc + N - 2 * nodes[i].size + nodes[n].sum_path - nodes[i].sum_path);
}

std::vector<int> lb, la;

int fast_lca(int a, int b)
{
  while (nodes[a].path != nodes[b].path)
  {
    if (paths[nodes[a].path].prof > paths[nodes[b].path].prof)
      a = paths[nodes[a].path].parent;
    else
      b = paths[nodes[b].path].parent;
  }
  if (nodes[a].prof < nodes[b].prof)
    return a;
  return b;
}

int goUp(int node, int dist)
{
  if (nodes[node].pos >= dist)
    return paths[nodes[node].path].nodes[nodes[node].pos - dist];
  return goUp(paths[nodes[node].path].parent, dist - nodes[node].pos - 1);
}

void extract(int a, int prof, std::vector<std::pair<int, long long>> &v)
{
  v.clear();
  int ps = 0;
  while (nodes[a].prof >= prof)
  {
    int j = std::min(nodes[a].num_1, nodes[a].prof - prof);
    if (j > 0 && v.size() > 0)
      v.push_back({j, nodes[a].size - ps});
    else
      v.push_back({1, nodes[a].size - ps});

    if (nodes[a].prof < prof + v.back().first)
      break;
    a = goUp(a, v.back().first - 1);
    ps = nodes[a].size;
    a = nodes[a].parent;
  }
}

std::vector<long long> A, B;

std::unordered_map<long long, long long> map4;
long long solve(long long a, long long b)
{
  if (nodes[a].prof < nodes[b].prof)
    std::swap(a, b);
  const long long key = (a << 20ll) | b;
  int p = fast_lca(a, b);
  int d = 1 + nodes[a].prof + nodes[b].prof - 2 * nodes[p].prof;
  long long sum = 0;

  long long m = d % 2;
  size_t ll = d / 2;
  long long j = ll - 1;
  long bb = 0;
  bool JJ = false;
  bool canjamup = true;
  std::vector<std::pair<int, long long>> bbb, bbb2;

  extract(b, nodes[p].prof + 1, bbb);
  extract(goUp(a, ll), nodes[p].prof + 1, bbb2);
  int preva = goUp(a, nodes[a].prof - nodes[p].prof - 1);
  bbb.push_back({1, N - nodes[preva].size});
  if (b != p)
  {
    int prevb = goUp(b, nodes[b].prof - nodes[p].prof - 1);
    bbb.back().second -= nodes[prevb].size;
  }
  bbb.insert(bbb.end(), bbb2.rbegin(), bbb2.rend());
  int i = 0;
  for (auto &b : bbb)
  {
    if (i >= ll)
      break;
    long long jump = b.first;
    int a1 = goUp(a, j - i - jump + 1);
    int a2 = goUp(a1, jump);
    long long cur = m * nodes[a1].cumsize - 2 * nodes[a1].cumcumsize -
                    (m * nodes[a2].cumsize - 2 * nodes[a2].cumcumsize);

    sum += cur * b.second;
    bb += b.second * jump;
    i += jump;
  }
  sum += 2 * nodes[goUp(a, 0)].cumsize * bb;

  map4[key] = sum;
  return sum;
}

int main()
{
  scanf("%d %d", &N, &M);
  for (int i = 1; i < N; i++)
  {
    int a, b;
    scanf("%d %d", &a, &b);
    nodes[a].children.push_back(b);
    nodes[b].children.push_back(a);
  }

  getDepth(1, 0, 1);
  getSize(1);
  getSumPath(1);
  getSumPathFromTop(1);
  extractPath(1, numPaths++);

  long long sum = 0;
  for (int i = 1; i <= N; i++)
    sum += nodes[i].sum_path + nodes[i].sum_path_from_top;

  sum /= 2;

  for (int i = 0; i < M; i++)
  {
    int a, b;
    scanf("%d %d", &a, &b);
    printf("%lld\n", sum - solve(a, b));
  }
  return 0;
}