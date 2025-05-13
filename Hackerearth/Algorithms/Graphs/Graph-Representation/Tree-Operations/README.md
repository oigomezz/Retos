# [Tree operations][link]

Given an undirected tree with N nodes rooted at 1. Every node is assigned a weight which is given by an array A. Weight of an edge W(u, v) is defined as (A[u] XOR A[v]) \* (A[u] | A[v]), where | represents Bitwise OR operator.

You are allowed to perform at most K operations on the tree and in each operation:

- Choose u v, and shift the weights of the nodes present on the simple path from node u to v cyclically by one step.
- Suppose, the simple path between node u v is u - u[1] - u[2] - u[3] - ... - u[n] - v, then do the following simultaneously :
  - A[u] = A[v]
  - A[u[1]] = A[u]
  - A[u[2]] = A[u[1]]
  - ...
  - ...
  - A[v] = A[u[n]]

Suppose, X such operations are performed, maximize the value of Z = (Sum of weight of all the edges of the tree) \* (K - X + 1)

## Input format

- First line contains two space separated integers N K.
- Second line contains N space separated integers denoting the weight of the nodes.
- Next N - 1 lines contains two space separated integers u v, denoting an edge between node u and v.

## Output format

- Print X, denoting the number of operations performed in a new line.
- In next X lines, print the pair of nodes u v choosen in given operation.

[link]: https://www.hackerearth.com/practice/algorithms/graphs/graph-representation/practice-problems/approximate/tree-operations-711e2aca/
