# [Maximize Tree Value][link]

Given an undirected tree with N nodes rooted at 1. Every node is assigned a weight which is given by an array A. Weight of an edge W(u, v) is defined as (A[u] + A[v]) \* (A[u] | A[v]), where | represents Bitwise OR operator.

You are allowed to perform at most K operations on tree and in each operation:

- Choose u v, and reverse the weights of the nodes present on the simple path between node u and v.

Suppose, X such operations are performed, maximize the value of Z = (Sum of weight of all the edges of the tree) \* (K - X + 1)

## Input format

- First line contains two space separated integers N K.
- Second line contains N space separated integers denoting the weight of the nodes.
- Next N - 1 lines contains two space separated integers u v, denoting an edge between node u and v.

## Output format

- Print X, denoting the number of operations performed.
- In next X lines, print the pair of nodes u v choosen in given operation.

[link]: https://www.hackerearth.com/practice/algorithms/graphs/depth-first-search/practice-problems/approximate/minimize-tree-value-44962c92/
