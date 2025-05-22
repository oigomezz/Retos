# [Minimizing graphs' weights][link]

You are given an undirected weighted graph G with N nodes and M edges. Each edge has a weight assigned to it. You are also given an array A of N elements. Graph G does not contain any self-loops and multiple edges.

If a new edge is added between node u and v, then the weight of this edge is max(Au,Av).

Add some edges (possible 0) until there exists a subgraph H such that it satisfies the following conditions:

- H contains all the vertices of G.
- H is connected.
- H is bipartite.
- H does not contain self-loops or multi-edges.
- Number of additional edges should be as minimum as possible.

Find the minimum possible weight of such subgraph H. The weight of a graph is defined as the summation of weights of all the edges present in the graph.

## Input format

- The first line contains a single integer T that denotes the number of test cases.
- For each test case:
  - The first line contains an integer N.
  - The second line contains an integer M.
  - The third line contains N space-separated integers denoting array A.
  - Next M lines contain three space-separated integers u,v,w denoting an edge between nodes u and v with weight w.

## Output format

For each test case, print the minimum possible weight of subgraph H. Print the output for each test case in a new line.

[link]: https://www.hackerearth.com/practice/algorithms/graphs/depth-first-search/practice-problems/algorithm/minimize-graph-weight-2fc2503b/
