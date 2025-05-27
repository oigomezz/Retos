# [Minimize the value][link]

You are given a binary tree rooted at 1. Initially, all the nodes of the tree have some initial values Vi. Wave operation is to be applied on the tree.

After applying the wave operation,
Value of each node in the tree = Sum of all initial values of nodes in its subtree.

You are required to add 1 more node with value X to the tree such that:

1. The tree remains binary after adding the node to the tree.
2. After applying the wave operation to this tree (the tree after adding node with value X), the sum of tree is minimum.

Sum of tree = sum of values of all nodes in the tree.

Print the minimum sum of the tree.

## Input format

- First line of input contains 2 integers N and X , number of nodes in the tree and value of new node to add respectively.
- Second line contains N space separated integers denoting value of each node.
- Each of the following N-1 lines contains 2 integers u and v, representing edge between node u and node v.

## Output format

Print the minimum sum possible after adding node with value X and applying wave operation such that tree remains binary tree.

[link]: https://www.hackerearth.com/practice/algorithms/graphs/depth-first-search/practice-problems/algorithm/minimize-the-magic-05a3986c/
