# [Minimum Valid Path][link]

You are given a weighted directed graph some of whose vertices are marked as special vertices. A valid path in it is a path which satisfies the following conditions:

1. For any two adjacent edges x and y on the path, 0.5 \* weight(x) <= weight(y) <= 2 \* weight(x)

2. The path contains exactly one special vertex.

Given two vertices x and y, your task is to calculate the minimum cost of a valid path between them.

## Input format

- First line: n and m, the number of vertices and the number of edges in the graph.
- Next m lines contain three integers u, v, and w representing an edge from vertex u to vertex v, with a weight of w.
- Next line contains an integer k - the number of special vertices.
- Next line contains k distinct integers, the indices of the special vertices.
- The last line contains the integers x and y, the source and destination vertices.

**Note:** Graph can have multiple edges between two vertices.

## Output format

If there is no valid path from x to y output -1, else output the minimum cost of a valid path from x to y.

[link]: https://www.hackerearth.com/practice/algorithms/graphs/graph-representation/practice-problems/algorithm/minimum-valid-path-3dc5bd03/
