# [Special Edge][link]

Given a connected, undirected graph G with N nodes and M edges. Every node has a value assigned to it, denoted by the array A.

An edge E is said to be special iff :

- There exists at least one pair (u,v), u < v such that any simple path between node and will always include the edge E.
- The strength of such an edge is defined as Σ Au x Av over all such pairs.

Among all the special edges, find the special edge with the maximum strength in the graph.

If there exists more than one answer, suppose edge E(a,b) and E'(a',b') where a < b & a' < b'

- Return the edge with smaller node as the first value in the pair i.e. a, a'.
- If, there still exists more than one answer, return the edge with smaller node as the second value in the pair i.e. b,b'.

If there does not exists any such edge, return pair (n+1,n+1)

## Input format

- First line contains two space-separated integers N, M.
- Next line contains N space-separated integers denoting the array A.
- Next M lines contains two space-separated integers denoting an edge.

## Output format

Print two space-separated integers a b, denoting the special edge with maximum strength. Please note a < b.

[link]: https://www.hackerearth.com/practice/algorithms/graphs/graph-representation/practice-problems/algorithm/special-edge-3-1e932e1e/
