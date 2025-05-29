# [Largest Windmill][link]

We define a windmill graph as a graph G centered on node c with at least 5 adjacent paths. One of these paths has to have length at least 3 and it is interpreted as the base of the windmill. The remaining paths have length exactly 1 and are interpreted as the sails of the windmill.

For a given tree T with N nodes, the goal is to find the size of its largest subgraph (in terms of the number of nodes) which is a windmill graph and it’s center vertex. If there are many such largest subgraphs, take the one with the smallest center vertex. If no windmill graph is a subgraph of T, then the answer is 1.

## Input format

- On the first line, there is a single integer N denoting the number of nodes in the tree T.
- Then, N-1 lines follow:
  - Each of them contains two space-separated integers u and v and denotes that there is an edge between nodes u and u in the tree.

## Output format

If there is no subgraph of T which is a windmill graph output 1 in a single line. Otherwise, output two space-separated integers result and c, where result is the size of the largest windmill subgraph of T and c is the smallest center node among all the largest windmill subgraphs of T.

[link]: https://www.hackerearth.com/practice/algorithms/graphs/depth-first-search/practice-problems/algorithm/largest-windmill/
