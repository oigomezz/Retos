# [Construct Tree][link]

Given a set of N nodes, where each node has an integer Ai associated with it. Construct a tree using N nodes such that the value of the given function Z is maximized.

Z = Σ Stretch(u,v), for all u,v such that u < v and u, v are leaf nodes in the tree.

Stretch(u,v) is defined as: (Sum of values of nodes present on simple path between node u and v) \* (Length of the simple path)

Please note:

- A node x is said to be a leaf node if it is connected to exactly one other node in the tree, exception is a tree with 1 node, where the only node present in the leaf node.
- Length of a simple path is equal to number of nodes on simple path - 1.

## Input format

- First line contains an integer N denoting number of nodes in the tree.
- Next line contains N space separated integers denoting the value of each node i.e. Ai.

## Output format

Print N - 1 lines where each line contains

- Two space separated integers a b denoting an edge between node a and b in the tree.

[link]: https://www.hackerearth.com/practice/algorithms/graphs/depth-first-search/practice-problems/approximate/construct-tree-4ac7437c/
