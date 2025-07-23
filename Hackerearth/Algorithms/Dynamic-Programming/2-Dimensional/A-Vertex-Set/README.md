# [A vertex set][link]

You are given a tree T with N nodes and the tree is rooted at node 1. Each node has a value A[i] associated with it. Let us define a set X as follows:

X = {v1,v2,...,vk} , set X has nodes v1,v2,...,vk such that there does not exist an edge between any two vertices in X.

Also, F(v) is the maximum value node present in the subtree of node v (including itself).

V(X) = Σ F(vi) where {v1,v2,...,vk} belong to X.

Find the maximum value of V(X).

## Input format

- The first line contains an integer T denoting the number of test cases.
- The first line of each test case contains an integer N denoting the number of nodes in the tree.
- Next N-1 lines contain two space-separated integers denoting the edges.
- The last line contains N space-separated integers denoting the value of nodes.

## Output format

For each test case, print the maximum value of F(X) in a new line.

[link]: https://www.hackerearth.com/practice/algorithms/dynamic-programming/2-dimensional/practice-problems/algorithm/vertex-set-90a5e5a1/
