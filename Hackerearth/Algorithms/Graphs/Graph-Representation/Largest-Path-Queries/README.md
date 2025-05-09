# [Largest path queries][link]

You are given an unweighted tree that contains only 1 node. You have to process the following two types of queries:

- 1 x : Add a new node: You are given an already-existing node , assuming that there are nodes in the tree till now. Now, add a new node numbered (N+1) with node x as its parent.
- 2 x: You are given a node x. Determine the length of the largest simple path in the tree starting from node x.

For each query of type 2, you must print the required answer. Note that the length of the path is equal to the number of edges in the path.

## Input format

- The first line contains a single integer T denoting the number of test cases.
- The first line of each test contains a single integer Q denoting the number of queries that you have to process.
- Each of the next Q lines contains two integers k and x where N is the total number of nodes in the tree till now. Here, k represents a query type and x is the node number.

## Output format

For each query of type 2, you are required to print the length of the largest simple path starting at node x.

[link]: https://www.hackerearth.com/practice/algorithms/graphs/graph-representation/practice-problems/algorithm/largest-path-queries-86ba3f71/
