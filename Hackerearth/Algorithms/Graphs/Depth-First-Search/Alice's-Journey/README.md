# [Alice's Journey][link]

Alice has a weighted tree of N vertices. A tree is a connected acyclic graph with exactly N-1 edges.

Alice wants to visit all the vertices of the tree by following the edges that connect these vertices. But she wants to do so in minimum time. She can pick any tree vertex as the starting point of her journey. Let’s say her current position is C. Then she can move to any adjacent vertex of C, but it costs her time equal to the weight of the edge. She will continue the above moves until she visits all the vertices.

Calculate the shortest time when Alice can visit all the vertices if she can choose any vertex as her starting point.

## Input format

- The first line contains a single integer N denoting the number of vertices in the tree.
- The next N-1 lines contain 3 space-separated integers (u,v,w), denoting an edge between vertices u and v of weight w.

## Output format

Print a single integer denoting Alice's shortest time to visit all the vertices if she can choose any vertex as her starting point.

[link]: https://www.hackerearth.com/practice/algorithms/graphs/depth-first-search/practice-problems/algorithm/bobs-journey-2-809f1266/
