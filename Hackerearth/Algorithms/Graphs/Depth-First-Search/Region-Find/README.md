# [Region Find][link]

You are given a tree with N nodes and N-1 edges. We define a region as a set of nodes, such that if we remove all other nodes from the tree, these nodes still remain connected i.e. there exists a path between any two remaining nodes.

All the nodes have a weight associated to them. You are given Q queries. Each query has a number k. You have to find number of regions, such that the minimum weight among all the nodes of that region is exactly k. Output your answer modulo 10⁹ + 7.

## Input format

- The first line will contain N, the number of nodes.
- Next line will contain N integers. The ith integer will indicate weight, the weight of ith node.
- Next N-1 lines will contain 2 integers "x y" (quotes for clarity) denoting an edge between node x and node y.
- Next line will contain a number Q , the number of queries.
- Next Q lines will contain an integer k , which is as described in problem statement.

**NOTE:** nodes are numbered 1 indexed.

## Output format

You have to output Q lines, each containing a single integer, the answer to the corresponding query.

[link]: https://www.hackerearth.com/practice/algorithms/graphs/depth-first-search/practice-problems/algorithm/region-find-december-easy-medium-hard/
