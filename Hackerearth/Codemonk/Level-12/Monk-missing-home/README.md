# Monk missing home

Spending a good amount of time in the Digital World, Monk was really missing his home and wanted to exit this world as soon as possible. Unlike the entry in the Digital World, there is a big barrier while exiting. A big tree T with N nodes, works as a Gatekeeper for the exit gate. Each node of a tree T has a value associated with it given as A1,A2,...,An.

In order to exit, T asked Monk to process N - 1 queries on itself.

In each query:

1. Monk will be given a edge number e.
2. Monk has to delete edge e from the tree T.
3. After deleting the edge, Monk has to print total number of unordered pairs (u, v) such that there exits path from u to v and the absolute difference, i.e | Au - Av | ≤ D.

**Note:** Once an edge is deleted, it will be deleted permanently.

Monk is really missing his home, please help him.

## Input format

- First line of input will consists of two integers N and D.
- Next line will consists of N integers A1,A2,...,An.
- Next N-1 lines will consists of two integers u and v. It denotes that i-th edge consists of two nodes u and v.
- Next N-1 lines will consists of one integer e denoting the queries.

## Output format

For each query, print the total number of unordered pairs (u, v) such that there exits path from u to v and | Au - Av | ≤ D
