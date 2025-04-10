# [Operations on a tree][link]

You are given an undirected tree G with N nodes. You are also given an array A of N integer elements where A[i] represents the value assigned to node i and an integer K.

You can apply the given operation on the tree at most once:

- Select a node x in the tree and consider it as the root of the tree.
- Select a node y in the tree and update the value of each node in the subtree of y by taking its XOR with K. That is, for each node u in the subtree of node y, set A[u] = A[u] XOR K.

Find the maximum sum of values of nodes that are available in the tree, after the above operation is used optimally.

## Input format

- The first line contains a single integer T that denotes the number of test cases.
- For each test case:
  - The first line contains an integer N.
  - The second line contains an integer K.
  - The third line contains N space-separated integers denoting array A.
  - Next N-1 lines contain two space-separated integers denoting an edge between node u and v.

## Output format

For each test case, print the maximum possible sum of values of nodes present in the tree. Print the output for each test case in a new line.

[link]: https://www.hackerearth.com/practice/algorithms/greedy/basics-of-greedy-algorithms/practice-problems/algorithm/operation-on-tree-ae14ee70/
