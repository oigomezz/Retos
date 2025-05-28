# [Little Shino and K Ancestor][link]

Assume that you are given an undirected rooted tree with N nodes and an integer K. Node 1 is the root of the tree. Each node is uniquely numbered from 1 to N. Additionally, each node also has a color and the color is an integer value.

**Note:** Different nodes can have the same color.

For each node, you are required to find the K-th closest ancestor from that node which has the same color.

## Input format

- The first line consists of two integers, denoting N and K.
- The second line is an array A of length N, represented as space separated integers. Here is the color-value of i-th node in the tree.
- This is followed by lines comprising of two space separated integers x and y, which denotes that there is an edge between nodes that are numbered x and y.

## Output format

Print N space separated integers, where i-th integer denotes the K-th closest ancestor from i-th node which has the same color. If no such ancestor exists, print 1.

[link]: https://www.hackerearth.com/practice/algorithms/graphs/depth-first-search/practice-problems/algorithm/little-shino-and-k-ancestor-57fdef57/
