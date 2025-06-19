# [Isomorphic Trees][link]

You are given two trees. You are allowed to perform an operation several times: attaching a new vertex connect to an existing vertex of a tree. For each vertex A of the first tree and vertex B of second tree, we root the first tree at A and the second tree at B then your task is to find the minimum number of operations needed to make two trees isomorphic.

(Two rooted trees are isomorphic if they are the same size N, and there is a permutation P of {1,2,...,N} such that P["root of the first tree"] = "root of the second tree" and there is an edge between u,v in the first tree iff there is an edge between P[u],P[v] in the second tree.)

## Input format

- The first line contains two space-separated integers N,M denoting the number of vertices of two trees.
- Each of N-1 next lines contains two space-separated integers u,v denoting an edge (u,v) of the first tree.
- Each of M-1 next lines contains two space-separated integers u,v denoting an edge (u,v) of the second tree.

## Output format

Output N lines, each line contains M space-separated integers. j-th number in the i-th line contains the answer if we root the first tree at vertex i and the second tree at vertex j.

[link]: https://www.hackerearth.com/practice/algorithms/graphs/minimum-cost-maximum-flow/practice-problems/algorithm/isomorphic-tree-70be4549/
