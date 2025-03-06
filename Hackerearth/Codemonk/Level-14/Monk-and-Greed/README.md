# Monk and Greed

Monk needs some help with the following question he got for his homework. You being his best friend have promised to help. The question is as follows:

You are given a connected graph with N nodes and M edges. You are also given two nodes U and V. The edges are undirected and have weights. Also, the node has a value A[i].

Define a subgraph as a subset of the edges of a graph G together with any vertices that are their endpoints. The value of an edge in the subgraph is the same as the value of the corresponding edge in G, so is the value of a node. Subgraph should be connected.

Let S be the sum of values of nodes in the subgraph and let X be the minimum weight of edge present in the subgraph. You taken into consideration a subgraph that satisfies the following conditions:

1. Nodes U and V are a part of the subgraph.
2. There exists a path between them(considering edges of the subgraph only).
3. X is maximum.
4. If this maximum X is same for two or more such subgraphs, you take the one with maximum S.
5. Subgraph should be connected.

Output the value of X and S for this subgraph.

**NOTE:** the graph may contain self loops and multiple edges between same pair of nodes.

## Input format

- First line contains two integers N and M.
- Second line contains N integers where the i-th integer represents A[i].
- Next M lines contain three integers a,b and w denoting an edge between a and b with weight w.
- Next line contains two integers U,V.

## Output format

Output two space separated integers that is the answer to the problem.
