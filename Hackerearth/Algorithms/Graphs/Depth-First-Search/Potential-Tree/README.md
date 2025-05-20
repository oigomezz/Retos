# [Potential Tree][link]

You are given a tree consisting of N vertices. Its root is not fixed yet. The potential of a non-leaf vertex is the count of its children (distance of from the vertex) with a non-zero potential. The potential of a leaf vertex i is i % 2.

Your task is to calculate the potential of every possible root. Find an array A such that Ai represents the potential of vertex i if the tree was rooted at i.

## Input format

- The first line of input contains a single integer T, denoting the number of test cases.
- The first line of each test case contains a single integer,N , denoting the number of vertices.
- The following N-1 lines contain two integers u,v denoting an edge between vertex u and vertex v.

## Output format

For each test case, print an array A such that Ai represents the potential of vertex i if the tree was rooted at i.

[link]: https://www.hackerearth.com/practice/algorithms/graphs/depth-first-search/practice-problems/algorithm/potential-tree-26d889a0/
