# [Graphs][link]

You are given an undirected graph G that contains n nodes and m edges. It is also mentioned that G does not contain any cycles. A sequence of nodes (A1,A2,..., Ak) is special if distance d(Ai,Ai+1) = f.i for all 1 <= i < k , and all Ai are distinct. Determine the size of a maximal special sequence. Hence, the one with maximum k.

## Note

- If A and B are not connected, then d(A,B) = Inf, else d(A,B) = the number of edges in the path from A to B.
- Any node can be selected as a sequence of size 1.

## Input format

- First line: Three integers n, m, and f.
- Next second to (m+1)th lines: Two integers x and y , x!= y that denotes an edge between x and y.

## Output format

Print the maximum value of k.

[link]: https://www.hackerearth.com/practice/algorithms/graphs/breadth-first-search/practice-problems/algorithm/great-graphs-afc1a343/
