# [Separate paths][link]

You are given a directed graph that contains N nodes (numbered from 1 to N) and M edges.

A valid path is a path that starts from a node that does not contain any edges that are directed towards it. That is, the value of Indegree of node is 0. This path can also contain only one node in it. That is, the paths of length 0 are also valid paths but they must still follow the main condition that the starting node (in this case the only node) should not contain any edges that are directed towards it.

You are required to calculate the number of unordered pair of nodes such that there exist two valid paths that end at these nodes. These two paths should not contain any node in common.

**Note:** The graph can be cyclic as well as disconnected, but there are no self-loops or multiple edges.

## Input format

- First line: A single integer T denoting the number of test cases.
- For each test case:
  - First line: Two integers, N and M denoting the number of nodes and number of edges that are available in the graph respectively
  - Each of the next M lines: Two integers u and v denoting an edge from vertex u to vertex v.

## Output format

For each test case, print a single integer denoting the number of unordered pair of nodes that are satisfying the mentioned condition.

[link]: https://www.hackerearth.com/practice/algorithms/graphs/graph-representation/practice-problems/algorithm/separate-paths-2638c0fa/
