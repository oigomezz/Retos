# [Tree and XOR][link]

For a tree X, rooted at node 1, having values at nodes, and a node i, lets define S(X,i) as the bitwise xor (⊕) of all values in the subtree of node i.

You are given a tree T. Let Ti be the tree remaining after removing all nodes in subtree of i. Define P(i) = max(S(T,i) ⊕ S(Ti,j)). You have to find sum of P(i) over all nodes i != 1.

## Input format

- First line contains a single integer N, denoting the number of nodes in the tree T.
- Next line contains N space separated integers denoting the values of nodes in the tree G.
- Each of the next N-1 lines contain 2 space separated integers A and B, meaning that there is an edge from node A to node B.

## Output format

Print a single integer, the sum of P(x) for all nodes x (except 1) of the tree G.

[link]: https://www.hackerearth.com/practice/algorithms/graphs/depth-first-search/practice-problems/algorithm/tree-and-xor-1-aaedc91e/
