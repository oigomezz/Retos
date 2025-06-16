# [Maximum size of a set][link]

You are given a DAG N with N nodes and M edges. You are building a graph G^. G^ contains the same vertex set as G and all edges are available in G. Moreover,

1. If there exists an edge between vertex u and v in G, then there does not exist an edge between vertex v and u in G^.
2. If there exists an edge between vertex u and v in G and also between v and w in G, then there exists an edge between vertex u and w in G^.

For G^, find the maximum possible size of S where S is a set of vertices in G^ such that there exists an edge between every unordered pair of vertex present in S.

The meaning of unordered is that there must exist an edge between every pair of vertex (u,v), that is, either u - > v or v - > u must be in an edge set.

## Input format

- The first line contain two integer N and M describing nodes and edges in graph G.
- Next M lines contain two integers u and v representing an edge from u to v.

## Output format

Print the maximum possible size of set S.

[link]: https://www.hackerearth.com/practice/algorithms/graphs/topological-sort/practice-problems/algorithm/social-graph-1-ac58bbdf/
