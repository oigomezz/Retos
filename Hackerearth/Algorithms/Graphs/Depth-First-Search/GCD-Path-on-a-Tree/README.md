# [GCD Path on a Tree][link]

Given an Integer K and a tree of N vertices where each vertex consists of a value Vi associated to it. Find the longest path in the tree which satisfies the following conditions

1. The number of vertices in the path should be a multiple of K.
2. Let's say there are L x K vertices in the path and Xi be the value associated with i-th vertex in that path, then GCD(X(ixK+1),X(ixK+2), ..., X(ixK+k)) > 1 for all i ∈ [0, L-1]. where GCD(x1,x2,...,xn) is the Greatest Common Divisor of the numbers x1,x2,...,xn.

## Input format

- First line consists of two integers N and K.
- Next N-1 lines consists of two integers ui and vi representing an edge between ui and vi.
- Next line consists of N space separated integers where i-th of them is the value Vi associated to i-th vertex.

## Output format

Print an Integer representing the longest path as described in the problem statement.

[link]: https://www.hackerearth.com/practice/algorithms/graphs/depth-first-search/practice-problems/algorithm/gcd-path-on-a-tree-1-1589989c/
