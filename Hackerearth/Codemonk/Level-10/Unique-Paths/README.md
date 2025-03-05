# Unique paths

You are given a connected undirected graph containing N nodes and M edges. The task is very simple. You are provided two nodes u and v. You are required to check whether the path from u to v is unique or not. If there exists a path, you are required to determine the distance between the nodes u and v, then print -1. You must perform these operations for Q queries.

## Input format

- First line: Two space-separated integers N and M.
- Next M lines: Two space-separated integers u and v denoting that there is an edge between node u and v.
- Next line contains a single integer Q denoting the number of queries.
- Next Q lines: Two space-separated integers u and v.

## Output format

For each query, print the distance between the two nodes if there exists a unique path between the nodes in that query. Otherwise, print -1.
