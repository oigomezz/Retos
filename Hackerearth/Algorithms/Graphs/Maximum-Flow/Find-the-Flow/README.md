# [Find the Flow][link]

Given a directed flow network where each edge has a capacity of flow it could allow, find the maximum flow over the network from source(S) to sink(T).

Network will follow these rules:

- Only one source(S) and only one sink(T).
- Other than source and sink, nodes are represented with alphabets [A - O].
- There are no self loops.
- There will be no initial dead ends other than T.
- For any pair of nodes, direction of edges between them will be in single direction.

## Input format

- First line has an integer E- number of edges.
- Next E lines have three values Vi Vj Cx which implies there is a node from Vi to Vj with capacity Cx.

## Output format

Print a single integer which is the maximum flow from source to sink.

[link]: https://www.hackerearth.com/practice/algorithms/graphs/maximum-flow/practice-problems/algorithm/find-the-flow/
