# [Xor tree][link]

You are given an undirected tree with N nodes. Every node is initially assigned a value equal to 0.

Perform Q queries that are given on the tree as follows:

- u v w: For all the nodes present on a simple path between nodes u and v take the xor of node value with w.

**Task** Find the sum of values assigned to all the nodes after performing Q queries.

## Input format

- First line contains an integer T, denoting the number of test cases.
- For each test case:
  - The first line contains two space separated integer N, Q.
  - The next N - 1 lines contain two space-separated integers u, v denoting an edge between node u and node v.
  - The next Q lines contains three space-separated integers denoting the query.

## Output format

For each test case in a new line, print the sum of values assigned to each node after performing Q queries.

[link]: https://www.hackerearth.com/practice/algorithms/graphs/depth-first-search/practice-problems/algorithm/xor-tree-4-c6f207f4/
