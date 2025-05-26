# [Connecting the special nodes][link]

You are given a graph of N nodes. The graph consists of connected components. Some of the connected components contain a special node and each component contains at most one special node. You are required to maximize the number of edges in the given graph such that it follows these constraints:

- No self-loop or multiple edges should be present.
- No connected components with more than one special node should be present.
- Each node in the graph should belong to a component with exactly one special node.

If you add an edge between two nodes that belong to the same component in the graph, then the total cost involved is 0. Whereas, if you connect two nodes that belong to different components, then the cost is equal to the product of the sizes of both the components.

Your task is to maximize the number of new edges in the graph and calculate the minimum cost that will be involved in performing the required task.

## Input format

- First line: Three integers N,M and K representing the number of nodes, number of edges, and number of special nodes in the graph respectively.
- Next M lines: Two integers u and v representing an undirected edge from the node u to node v.
- Next line: An empty line
- Next line: K space-separated integers each representing the special nodes in a connected component.

## Output format

Print the maximum number of new edges that can be added to the graph and the minimum cost of doing so.

[link]: https://www.hackerearth.com/practice/algorithms/graphs/depth-first-search/practice-problems/algorithm/jenny-and-water-7-d0337cc3-ec2c1136/
