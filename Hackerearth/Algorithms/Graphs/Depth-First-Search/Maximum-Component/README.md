# [Maximum component][link]

You are given a graph consisting of N nodes. Initially, there is no edge in the graph. You have to process Q queries of the following two types:

- 1 X Y: connect nodes X and Y with an undirected edge.
- 2 K: Print the size of the largest connected component if K extra undirected edges are added between any pair of nodes of the graph.

Note that the edges connected in the type 2 query are not considered in further queries.

**Note:** Since the size of input-output is large, prefer using fast input-output methods.

## Input format

- The first line of input contains N denoting the number of nodes and Q denoting the number of queries respectively.
- Q lines follow. Each of these lines contains an integer type[i], denoting the type of the i-th query. if type[i] is 1, it contains two more integers X, Y, if type[i] = 2, it contains an integer K.

## Output format

For each query of type 2, print the size of the largest connected component in a separate line.

[link]: https://www.hackerearth.com/practice/algorithms/graphs/depth-first-search/practice-problems/algorithm/maximum-component-afeef0fa/
