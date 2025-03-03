# Learning Graph

Monk once went to the graph city to learn graphs, and meets an undirected graph having N nodes, where each node have value val[i] where 1 <= i <= N. Each node of the graph is very curious and wants to know something about the nodes which are directly connected to the current node.

For each node, if we sort the nodes (according to their values), which are directly connected to it, in descending order (in case of equal values, sort it according to their indices in ascending order), then what will be the number of the node at k-th position, if positions are given starting from 1.

Now Graph gave this task to Monk. Help Monk for the same.

## Input format

- The first line will consist of 3 space separated integers N,M, k denoting the number of nodes, number of edges and value of k respectively.
- In next line, there will be N space separated integers val[i], where 1 <= i <= N, denoting the value of i-th node.
- In next M lines, each line contains 2 integers X and Y, representing an edge between X and Y.

## Output format

Print N lines, where i-th line contains the required node for the i-th node. If there is no such node, print -1.
