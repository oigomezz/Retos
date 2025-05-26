# [Sum of shortest paths][link]

Consider that D(G,u,v) is defined as the number of edges on the shortest path from u to v in a graph G.

You are given a tree T with N vertices and Q queries of the following type:

- If we add edge (a,b) to the tree T, obtaining graph G, then what is the value of Σ D(G,u,v) ?

**Note:** The queries are independent in nature.

## Input format

- First line: Two integers N,Q
- N-1 lines: Two integers x and y representing that there exists an edge (x,y) in the tree T.
- Next Q lines: Two integers a and b representing the query where a new edge (a,b) is added.

## Output format

Print Q lines where the i-th line contains the answer for the i-th query in the chronological order.

[link]: https://www.hackerearth.com/practice/algorithms/graphs/depth-first-search/practice-problems/algorithm/find-the-sum-of-shortest-paths-b47a96cd/
