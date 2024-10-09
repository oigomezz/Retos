# MST revisited

Given an undirected graph of N nodes and N weighted edges, it doesn't contain parallel edges nor self loops, it's guaranteed the graph will always remain connected.

you have to support Q queries, in each query you will be given one edge to delete and one edge to add in such a way to graph will remain connected, after each query you have to tell the cost of minimum spanning tree.

you have to provide an online solution (i.e. you can't see future queries until you answer the current one)

## Input format

- First line contains two integers N and Q.
- Each of the next N lines describe an edge by 3 integers u, v, c, it means there's an edge connecting nodes u and v and has weight equal to c.
- Each of the next Q lines describe a query by 5 integers x1, x2, x3, x4, x5, let ans be the answer to previous query (if this is first query then ans = 0). now let a = x1 + (ans mod 100), b = x2 + (ans mod 100), u = x3 + (ans mod 100), v = x4 + (ans mod 100), c = x5 + (ans mod 100), it means to delete edge connecting nodes a and b and add edge connecting u and v and has weight equal to c.

## Output format

Output the answer to each query in new line, the answer is one integer equal to sum of weights of minimum spanning tree of the graph.
