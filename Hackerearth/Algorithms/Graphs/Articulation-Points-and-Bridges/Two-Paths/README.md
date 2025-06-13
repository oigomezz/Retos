# [Two paths][link]

Given an undirected graph with n vertices and m edges. Each edge is one of the two types: white and black.

There are q queries denoted by four vertices a, b, c and d. Each query asks: can some of the black edges be deleted, so that a is reachable from b, but c is not reachable from d? Note that graph itself doesn't change from query to query.

## Input format

- The first line contains three integers n, m and q, number of vertices, number of edges and number of queries, respectively.
- Then m lines follow.
  - The i-th of them contains three integers ai, bi and ti describing edge connecting ai and bi, ti = 0 for black edge and ti = 1 for white edge.
- Then q lines follow.
  - The i-th of them contains four integers ai, bi, ci and di — vertices in the i-th query.

## Output format

For each query print Yes if it's possible to delete some black edges and satisfy the condition. Print No otherwise.

[link]: https://www.hackerearth.com/practice/algorithms/graphs/articulation-points-and-bridges/practice-problems/algorithm/two-paths/
