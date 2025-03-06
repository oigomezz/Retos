# Monk and Hops

Monk has a connected graph with N nodes and M weighted undirected edges.

You need to travel from node 1 to node N using a path with the minimum cost. If many such paths with minimum cost exists you need the one with the minimum hops.

Path is a sequence of vertices v1,v2,...,vk such that:

- All vi are distinct.
- vi and v(i+1) are connected by an edge for 1 <= i <= m-1.

Cost of a path is the sum of weight of edges (vi, v(i+1)) ∀i 1 <= i <= m-1.

Hops in a path are the number of pair of adjacent edges in the path such that weight of one edge is even and the other is odd, i.e., the number of pair of edges ((vi, v(i+1)), (v(i+1), v(i+2))) such that weight of one edge is even and the other is odd.

**NOTE:** The graph may contain multiple edges between same pair of nodes. It does not contain self loops.

## Input format

- First line contains the two integers N and M, denoting the number of nodes and the number of edges in the graph.
- M lines follow each containing three integers U, V and W, denoting that there exists an edge between nodes U and V with weight W.

## Output format

Output, on a single line two space separated integers, the cost and the number of hops of the path.
