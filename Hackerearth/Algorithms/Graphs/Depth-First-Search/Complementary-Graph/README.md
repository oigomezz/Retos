# [Complementary Graph][link]

You are given an undirected graph A, which has n vertices and m edges. There is another undirected graph B, which has n vertices and n \* (n - 1) / 2 - m edges. For each pair of vertices u, v there is an edge between them if and only if they are not connected by an edge in graph A.

Find the number of connected components in graph B and the size of each component.

## Input format

- The first line contains T, the number of test cases. The following lines contain the descriptions of the test cases.
- The first line of each test case contains two integers, n and m.
- Then m lines follow, each line containing two integers u and v (1 <= u, v <= n) denoting the edges present in graph A.

## Output format

- On the first line print an integer K - denoting the count of connected components in the graph.
- In the next line, print K integers denoting the size of K connected components in the graph. The size of components should be printed in increasing order.

[link]: https://www.hackerearth.com/practice/algorithms/graphs/depth-first-search/practice-problems/algorithm/complementary-graph-d7df491b/
