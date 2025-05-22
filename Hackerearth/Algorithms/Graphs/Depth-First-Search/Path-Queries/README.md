# [Path Queries][link]

You are given an undirected tree with N nodes and the tree is rooted at node 1. Each node has an integer value Ai associated with it represented by an array A of size N.

Also, you are given Q queries of the following type:

- u v: Find the value of Minimum + Maximum + Median of all the values present on the simple path between node u and node v.
- Suppose, K nodes are present on the simple path, then Median is defined as ((K+1)/2)th smallest element present on the simple path.

## Input format

- The first line contains two space-separated integers N, Q denoting the number of nodes and queries respectively.
- The second line contains N space-separated integers denoting array A.
- Next N-1 lines contain two space-separated integers denoting the edges of the tree.
- Next Q lines contain two space-separated integers denoting the queries.

## Output format

Print Q space-separated integers denoting the answer of queries.

[link]: https://www.hackerearth.com/practice/algorithms/graphs/depth-first-search/practice-problems/algorithm/count-triplets-5-bc28d9ca/
