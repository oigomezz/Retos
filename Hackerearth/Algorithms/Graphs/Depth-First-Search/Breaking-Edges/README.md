# [Breaking Edges][link]

You are given a tree (undirected connected graph with no cycles) consisting of N nodes and N-1 edges. There is a number associated with each node (vi) of the tree. You can break any edge of the tree you want and this would result in formation of 2 trees which were part of the original tree.

Let us denote by treeOr, the bitwise OR of all the numbers written on each node in a tree.

You need to find how many edges you can choose, such that, if that edge was removed from the tree, the treeOr of the 2 resulting trees is equal.

## Input format

- First line of input contains N, the number of nodes in the tree.
- Next line contains N space separated integers, i-th of which denotes vi.
- Each of the next N-1 lines describe the edges of the tree.
- Each line contains 2 space separated integers A and B, meaning that there is an edge between nodes A and B.

## Output format

Print the number of edges that can be chosen, such that, if that edge was removed from the tree, the treeOr of the 2 resulting trees is equal.

[link]: https://www.hackerearth.com/practice/algorithms/graphs/depth-first-search/practice-problems/algorithm/breaking-edges-march-circuits-ca482e2a/
