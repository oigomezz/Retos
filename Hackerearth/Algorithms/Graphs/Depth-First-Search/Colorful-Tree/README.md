# [Colorful Tree][link]

You are given a tree that contains N nodes, where every node i is colored with some color Ci.

The distance of a node V from a node U is defined as the number of edges along the simple path from the node U to the node V. Your task is to answer M queries of the following type:

- K C: Determine the distance of most distant node of color C from node K. If there is no node of color C in the tree, then print -1.

## Input format

- First line: Two integers N and M.
- Next line: N space-separated integers, where the i-th integer is Ci denoting the color of the i-th node.
- Next N-1 lines: Two integers U and V representing an edge between nodes U and V.
- Next M lines: Two integers K and C.

## Output format

For each query, print the distance of most distant node of color C from the node K. The answer for each query should come in a new line.

[link]: https://www.hackerearth.com/practice/algorithms/graphs/depth-first-search/practice-problems/algorithm/colorful-tree-1-28334713/
