# [Alice and wheel-graph][link]

Alice has a wheel-graph: an undirected graph with n+1 nodes and 2\*n edges. In wheel-graph there are edges between n+1 and i for each integer 1 <= i <= n and edges between i mod n+1 and for each integer 1 <= i <= n. Undirected graphs are quite boring for Alice so she made a directed wheel-graph and now each edge has a direction.

Alice wants performs two types of queries:

- 1 a b - change orientation between nodes a and b. Now orientation is from a to b (before this query in graph was a edge from node b to node a).
- 2 a b - check if is b reachable from a.

Help her.

## Input format

- The first line of the input contains a single integer n, number of nodes without center node.
- Then follow 2\*n lines with edges description. The i-th of these lines contains two integers ai and bi, index of node the edge start from, index of node the edge goes to. It is guaranteed that edges formed a correct directed wheel-graph with n+1 nodes.
- Next line of the input contains a single integer q, number of queries.
- Then q lines follow with queries description. The i-th of these lines contains three integers typei, ai, bi,parameters of the i-th query.

## Output format

For each query of the second type print "Yes" if b can be reached from a and "No" otherwise.

[link]: https://www.hackerearth.com/practice/algorithms/graphs/depth-first-search/practice-problems/algorithm/alice-and-wheel-graph/
