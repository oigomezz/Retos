# Infinite K-tree

You're given a K-ary infinite tree rooted at a vertex numbered 1. All its edges are weighted 1 initially.

Any node X will have exactly K children numbered as:

    [K*X+0, K*X+1, K*X+2, ... , K*X+(K-1)]

You are given Q queries to answer which will be of the following two types:

1. **1uv:** Print the shortest distance between nodes u and v.
2. **2uvw:** Increase the weight of all edges on the shortest path between u and v by w.

## Input format

- The first line contains two space-separated integers K and Q.
- Next Q lines contain queries which will be of 2 types:
  - Three space-separated integers 1, u, and v.
  - Four space-separated integers 2, u, v, and w.

## Output format

For each query of type (1uv), print a single integer denoting the shortest distance between u and v.
