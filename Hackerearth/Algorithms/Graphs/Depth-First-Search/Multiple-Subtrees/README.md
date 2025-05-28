# [Multiple Subtrees][link]

You are given a tree (not necessarily binary) with a special property which is, forming multiple sub-trees.
This happens as follows:

A random node of the tree is broken. After this, the node along with its immediate parents up to the root vanishes from the tree.

The tree has N number of nodes and nodes are numbered from 1 to N. The root of the tree is numbered as 1.

Given the number on one of its node, you have to tell the number of sub-trees that would be formed in-case the node is broken.

## Input format

- First line contains an integer N, denoting number of nodes in the tree.
- N-1 lines follow. Each of the N-1 lines contains two integers u and v,denoting there is a bidirectional edge between nodes u and v.
- The next line contains an integer Q denoting the number of queries.
- The next Q lines contain an integer each denoting the number of node that will break.

## Output format

For each query, print the number of sub-trees that will be formed if the node given in the query breaks. Answer for each query should come in a new line.

[link]: https://www.hackerearth.com/practice/algorithms/graphs/depth-first-search/practice-problems/algorithm/destructive-tree-explosion-45170564/
