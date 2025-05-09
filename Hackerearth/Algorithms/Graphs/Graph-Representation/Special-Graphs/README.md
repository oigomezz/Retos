# [Special graphs][link]

There exist a graph with N nodes that are numbered from 1 to N. There exists an edge between two nodes (u,v). Now, u != v if u divides v or vice versa. Node 1 is not connected to any other node.

Find the minimum size of set S of nodes such that all the nodes of this graph except node 1 is covered by this set. A node is said to be covered if it is present in this set or there exists at least one node in the set with which it is directly connected, that is, there is an edge between them.

You must cover all the nodes but not the edges.

## Input format

- The first line contains an integer Q denoting the number of queries.
- The next Q lines contain an integer N denoting the number of nodes in the graph.

## Output format

Print the minimum size of set S for each query in a separate line.

[link]: https://www.hackerearth.com/practice/algorithms/graphs/graph-representation/practice-problems/algorithm/special-graph-2-3b2bf33c/
