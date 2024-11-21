# Little Shino and Path Divisor

There is no partial marking in the problem.

Given a weighted undirected tree of N nodes and Q queries. Each query contains an integer D. For each query, find the number of paths in the given tree such that all the edges in the path are divisible by D.

## Input format

- First line contains two space separated integers, N and Q, denoting number of nodes in the tree and number of queries.
- Next N-1 line contains three space separated integers, X, Y and W, denoting that there is an edge between X and Y of weight W.
- Next Q lines contains one integer each, D.

## Output format

For each query, print number of paths such that all the edges in the path are divisible by D in new line.
