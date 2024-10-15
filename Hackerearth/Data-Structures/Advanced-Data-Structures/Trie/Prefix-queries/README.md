# Prefix queries

You are given an undirected tree with N nodes rooted at node 1. Every node has a value A[i] assigned to it. You are required to answer Q queries of the following type:

- VX : Find the longest length prefix that is common in the binary representation of V and the binary representation of node value of any of the ancestors of node X including node X itself. Also, the binary representation should be of length 62 and of the order from Most Significant Bit to Least Significant Bit.

Find the required answer for Q queries.

- Assume 1-based indexing.
- A node u is said to be an ancestor of node v, if node u lies on a simple path between the root and node v.
- The prefix of a binary representation is defined as a contiguous set of bits from the starting of the representation.

## Input format

- The first line contains a single integer T that denotes the number of test cases.
- For each test case:
  - The first line contains an integer N.
  - The second line contains N space-separated integers denoting array A.
  - Next N-1 lines contain two space-separated integers uv denoting an edge between node u and v.
  - The next line contains an integer Q.
  - Next Q lines contain two space-separated integers VX denoting the query.

## Output format

For each test case, print Q space-separated integers denoting the longest length common prefix for Q queries. Print the output for each test case in a new line.
