# [Path Value][link]

Given a connected graph G with N nodes and M edges (edges are bi-directional). Every node is assigned a value Ai. We define a value of a simple path as:

- Value of path = Maximum of (absolute difference between values of adjacent nodes in a path).

A path consists of a sequence of nodes starting with start node S and end node E.

- S - u1 - u2 -...- E is a simple path if all nodes on the path are distinct and S, u1, u2, ..., E are nodes in G.

Given a start node S and end node E, find the minimum possible "value of path" which starts with node S and ends with node E.

## Input format

- First line contains two space-separated integers N M.
- Second line contains two space-separated integers S E.
- Next M lines contain two space-separated integers u v, denoting an edge between node u and v.
- Next line contains N space-separated integers denoting values of nodes.

## Output format

Print a single integer — minimum possible "value of path" between node S and E.

[link]: https://www.hackerearth.com/practice/algorithms/graphs/graph-representation/practice-problems/algorithm/path-value-2-54ac4ca3/
