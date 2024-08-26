# Path Queries

You are given an undirected tree G with N nodes. Every node is assigned a value denoted by A[i]

A simple path u1 - u2 - ... - uk is said to be beautiful if the number of pairs of nodes (ui, ui+1) where A[ui] is odd and A[ui+1] is even and number of pairs of nodes (ui, ui+1) where A[ui] is even and A[ui+1] is odd are equal.

Given Q queries of the form:

- u val: Set the value of node u equal to val, i.e. set A[u] = val and find the number of ordered pairs (u,v) such that the simple path between node u and node v is beautiful.

## Input format

- The first line contains an integer T denoting the number of test cases.
- For each test case:
  - The first line contains two space-separated integers N Q denoting the number of nodes in the tree and the number of queries respectively.
  - Next line contains N space-separated integers denoting the array A.
  - Next N-1 lines contain two space-separated integers a,b, denoting an edge between node a and node b.
  - Next Q lines contains the queries.

## Output format

For each test case in a new line, print the answer for queries in a space-separated format.
