# [Subtree swap][link]

You are given an undirected tree with N nodes rooted at node 1. Every node has a value A[i] assigned to it. You are required to answer Q queries of the following type:

- U V X:
  - Select a subtree with U as the root node and subtree with V as the root node and swap their positions. That is, detach both the subtrees and swap their positions.
  - If node U is an ancestor of node V or node V is an ancestor of node U, the above Swap operation is not performed.
  - Find the sum of node values present in the subtree rooted at node X.
  - If the Swap operation is performed, then redo this operation. That is, swap the subtree with U as the root node and subtree with V as the root node.

Determine the required answer for Q queries.

## Input format

- The first line contains a single integer T that denotes the number of test cases.
- For each test case:
  - The first line contains an integer N.
  - The second line contains N space-separated integers denoting array A.
  - The next N-1 line contains two space-separated integers u v denoting an edge between node u and v.
  - The next line contains an integer Q.
  - The next Q lines contain three space-separated integers denoting the query.

## Output format

For each test case, print Q space-separated integers denoting the sum of node values present in the subtree rooted at node X after the swap operation is performed. Print the output for each test case in a new line.

[link]: https://www.hackerearth.com/practice/algorithms/greedy/basics-of-greedy-algorithms/practice-problems/algorithm/subtree-swap-f3734629/
