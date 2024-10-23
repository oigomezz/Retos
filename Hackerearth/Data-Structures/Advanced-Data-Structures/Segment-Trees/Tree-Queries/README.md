# Tree queries

You are given a tree T with N nodes rooted at node 1. Each node has a value A[i] associated with it.

You are required to perform Q queries where each query is of type:

- 1 u x: Increment the value associated with node u by x.
- 2 p: Find the shortest distance of any node from the root that has a value strictly greater than p. If no such node exists, then print -1.

**Note:** There exists at least 1 query of type 2.

## Input format

- The first line contains an integer T denoting the number of test cases.
- The first line of each test case contains an integer N.
- The second line of each test case contains N space-separated integers denoting array A.
- Next N -1 lines of each test case contain two space-separated integers denoting the edge.
- The next line of each test case contains an integer Q denoting the number of queries.
- Next Q lines of each test case contain queries.

## Output format

For each test case, print the answer of queries of type 2 in a new line.
