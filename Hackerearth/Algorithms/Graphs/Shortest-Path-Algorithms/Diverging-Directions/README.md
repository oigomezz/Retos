# [Diverging Directions][link]

You are given a directed weighted graph with n nodes and 2n - 2 edges. The nodes are labeled from 1 to n, while the edges are labeled from 1 to 2n - 2 . The graph's edges can be split into two parts.

- The first n - 1 edges will form a rooted spanning tree, with node 1 as the root. All these edges will point away from the root.
- The last n - 1 edges will be from node i to node 1, for all 2 <= i <= n.

You are given q queries. There are two types of queries

- 1iw: Change the weight of the i-th edge to w.
- 2uv: Print the length of the shortest path from node u to v

Given these queries, print the shortest path lengths.

## Input format

- The first line of input will contain two integers n,q, the number of nodes, and the number of queries, respectively.
- The next 2n - 2 integers will contain 3 integers ai,bi,ci, denoting a directed edge from node ai to node bi with weight ci.
- The first n - 1 of these lines will describe a rooted spanning tree pointing away from node 1, while the last n - 1 of these lines will have bi = 1.
- The next q lines will contain 3 integers, describing a query in the format described in the statement.

## Output format

For each type 2 query, print the length of the shortest path in its own line.

[link]: https://www.hackerearth.com/practice/algorithms/graphs/shortest-path-algorithms/practice-problems/algorithm/diverging-directions-c3a64882/
