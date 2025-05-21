# [Flip Color][link]

Given an undirected tree with N nodes rooted at node 1, every node is assigned a color which is either black denoted by 1 or white denoted by 0.

We will apply Q operations on the tree as follows:

- For a given node X and all its ancestors upto the root, flip their colors i.e. if color is white set it to black and vice-versa.

After Q operations on the tree, find the number of nodes which are colored black.

## Input format

- First line contains two space separated integers N and Q denoting number of nodes and queries respectively.
- Second line contains N space separated integers denoting the colors of N nodes.
- Next N-1 lines contains two space separated integers u and v denoting an edge between node u and v.
- Next line contains Q space-separated integers denoting the node X, for that given operation.

## Output format

Print an integer, denoting the number of nodes which are colored black after applying Q operations on the tree.

[link]: https://www.hackerearth.com/practice/algorithms/graphs/depth-first-search/practice-problems/algorithm/flip-color-16c8a423/
