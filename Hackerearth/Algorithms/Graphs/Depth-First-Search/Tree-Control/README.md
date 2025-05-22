# [Tree Control][link]

You are given an undirected weighted tree, in which 1 is the root node. Control value of each node denoted by ci.

Let's take two nodes (V,U ) such that V is the ancestor of U. V controls U if the distance between U and V is less than or equal to the control value of U

Find the number of vertices controlled by each node.

**Task:** Print N integers — the i-th of these numbers should be equal to the number of vertices that the i-th vertex controls.

**Note** Assume 1-based indexing.

## Function Description

Complete the solve function provided in the editor. This function takes the following 4 parameters and returns the required answer:

- N: Integer denoting the number of nodes
- c: Integer array denoting control values of each node
- p: Parent array, where pi denotes the parent of the (i+1)-th node in the tree
- w: Integer array, where wi denotes weight of the edge between pi and (i+1)

The function must return array of N integers — the i-th integer equal to number of nodes that the i-th node controls.

## Input format

- The first line contains single integer N.
- The second line contains N integers ci — the control value of i-th node.
- The third line contains (N−1) integers. pi — the parent of the (i+1)-th node in the tree
- The fourth line contains (N−1) integers. wi — weight of the edge between pi and (i+1)

## Output format

Print N integers — the i-th of these integers equal to the number of nodes that the i-th node controls.

[link]: https://www.hackerearth.com/practice/algorithms/graphs/depth-first-search/practice-problems/algorithm/tree-control-48dc13f4/
