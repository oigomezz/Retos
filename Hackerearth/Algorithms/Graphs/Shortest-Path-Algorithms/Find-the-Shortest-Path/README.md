# [Find the shortest path][link]

Given a weighted tree with N vertices and N-1 edges. Let D(i,j) be the distance of the unique simple path from i to j in this tree (i.e., the path from i to j that will not visit any node more than once).

We construct a new directed graph with N vertices, for each pair of vertices (i,j) if i < j we add an edge from i to j with weight D(i,j).

Find the shortest path from 1 to all other vertices in the newly constructed graph.

## Input format

- The first line contains one integer N.
- The (i+1)th line contains three integers ui,vi,wi, meaning there is an edge with cost wi between vertices ui and vi. These edges describe the original tree.

## Output format

Output N integers, the i-th integer represents the shortest path from 1 to i.

[link]: https://www.hackerearth.com/practice/algorithms/graphs/shortest-path-algorithms/practice-problems/algorithm/find-the-shortest-path-71e2e3d7/
