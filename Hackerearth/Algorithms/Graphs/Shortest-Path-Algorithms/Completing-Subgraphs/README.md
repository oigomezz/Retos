# [Completing Subgraphs][link]

There's some unweighted graph with N nodes and M edges. You have to respond to queries of 3 forms:

1. Given some interval of nodes [l,r], you need to add edges between every pair of these nodes (even if they are already connected by an edge)
2. You need to remove all edges added in the i-th query of type 1.
3. Given nodes u and v, you need to print the shortest path from u to v, or say that it doesn't exist.

## Input format

- First line of input contains the integers N and M.
- The next M lines of input contain 2 space-separated integers u and v, indicating a bidirectional edge between nodes u and v. There can be multiple edges between the same pair of nodes, and edges starting and ending in the same node.
- The next line contains the integer Q.
- The next Q lines of input are of one of the following formats:
  - 1 l r : perform the first query with the range [l,r]
  - 2 i : remove all edges added in the i-th query of type 1.
  - 3 u v : Print the length of the shortest path between nodes u and v.

It's guaranteed that for every query of type 2, the corresponding query of type 1 will appear before the type 2 query.

## Output format

For every query of type 3, output a single line with a single integer: the requested shortest path length if it exists, or -1 if it doesn't.

[link]: https://www.hackerearth.com/practice/algorithms/graphs/shortest-path-algorithms/practice-problems/algorithm/completing-subgraphs-8a55d9a5/
