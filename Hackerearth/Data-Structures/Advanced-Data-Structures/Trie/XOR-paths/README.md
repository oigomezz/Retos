# [XOR paths][link]

You are given a weighted tree (an acyclic undirected connected graph) with N nodes. The tree nodes are numbered from 1 to N. There are N-1 edges with each having a weight assigned to it.

You have to process Q queries on it. In each query, you are given three integers u,v,x. You are required to determine the maximum XOR that you can obtain when you the bitwise XOR operation on any edge weight in the path from node u to node v with x.

## Input format

- The first line contains two space-separated integers N and Q.
- The next N-1 lines contain three space-separated integers u,v,w denoting node u and v are connected with an edge of weight w.
- The next Q lines contain u,v,x.

## Output format

For each query, print a single integer in a new line.

[link]: https://www.hackerearth.com/practice/data-structures/advanced-data-structures/trie-keyword-tree/practice-problems/algorithm/xor-path-1-f7009db6/
