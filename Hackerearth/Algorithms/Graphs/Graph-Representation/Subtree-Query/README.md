# [Subtree Query][link]

Given a tree with N nodes, rooted at node 1. Every node of tree has a value associated with it denoted by an array A.

We perform Q queries of following 2 types on tree:

1. 1 u : Output the sum of values of all the nodes in subtree of u including u.
2. 2 u p : For all the nodes in subtree of u including u, perform Bitwise XOR operation of their value with p. That mean Ai = Ai ⊕ p where i will be the node in subtree of u including u (where ⊕ denotes the Bitwise XOR operator).

Find the output for all the queries of type 1.

## Input format

- First line contains N denoting the number of nodes in the tree.
- Next N - 1 lines contain two space-separated integers u, v denoting an edge between node u and v.
- Next line has N space separated integers denoting the array A.
- Next line contains Q denoting the number of queries.
- Next Q lines contain description of queries.

## Output format

For each query of type 1 print a single integer denoting the answer to that query in a separate line.

[link]: https://www.hackerearth.com/practice/algorithms/graphs/graph-representation/practice-problems/algorithm/subtree-query-cbd6ea30/
