# Tree query

You are given a directed acyclic graph G with N nodes and M directed edges. For a directed edge (u,v), it is said that this edge emerges out of node u.

Define a sink node as a node such that no edge emerges out of it.

Monk has given you the power to reverse all the edges of the graph together.

You want the maximum number of nodes that can be called as sink node, in the given graph. For this you can either go with the given graph or use Monk's power to reverse all edges of the graph.

1. An isolated node is a sink node.
2. Assume no self loops and at most one directed edge from a vertex to another.

## Input format

- First line contains two integers N and M, denoting the number of nodes and edges in the graph.
- Next M lines contain two integers X and Y, denoting that theres a directed edge from node X to Y.

## Output format

Output a single integer that is the answer to the problem.
