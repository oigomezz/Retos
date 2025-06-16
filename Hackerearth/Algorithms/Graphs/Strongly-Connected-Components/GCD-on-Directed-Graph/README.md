# [GCD on directed graph][link]

You are given a directed graph with n nodes and m edges. The nodes are numbered from 1 to n, and node i is assigned a cost ci. The cost of a walk on the graph is defined as the greatest common divisor of the costs of the vertices used in the walk. Formally, the cost of a walk v1,v2,...,vk is given by GCD(cv1, cv2, ..., cvk). Note that vi's need not be distinct. Find the cost of the walk with minimum cost.

The walk might consist of single vertex.

## Input format

- The first line contains two integers, n, and m.
- The next line contains n space separated integers, i-th of which is equal to ci.
- Each of the next m lines contain two integers, u, and v, denoting a directed edge from u to v.

## Output format

Print one integer containing the cost of the walk with minimum cost.

[link]: https://www.hackerearth.com/practice/algorithms/graphs/strongly-connected-components/practice-problems/algorithm/gcd-on-directed-graph-1122228a/
