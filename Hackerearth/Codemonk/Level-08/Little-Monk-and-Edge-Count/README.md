# Little Monk and Edge Count

Monk is struggling with a problem on graph and needs your help.

Given an undirected graph of N nodes and N - 1 edges. There is a unique path from any node to any other node. For a given edge e, he needs to find number of pairs (a,b), considering a and b as nodes of graph, such that e lies in the path between node a and node b.

## Input format

- First line of input contains two space separated integers, N and Q , denoting the number of nodes and number of queries.
- Next N - 1 lines contain two space separated integers, a and b, each, denoting there is an edge between a and b. i-th line denotes i-th edge.
- Next Q lines contain one integer x, denoting the x-th edge.

## Output format

For each query, print the number of pairs of nodes (a,b) such that x-th edge lies in the path between a and b.
