# [Proving your intelligence to your girlfriend][link]

Ashi is interested in checking the algorithmic skills of her boyfriend. So, she sets up a special 2-D graph for him. The 2-D graph looks like a maze with N rows each containing N nodes.
To connect these nodes, Ashi uses the following algorithm:

1. She selects two integers k1, k2 and computes the k1th and k2th fibonacci number, fib(k1) and fib(k2) respectively.
2. She takes the first row and selects the first two nodes in that row and adds an edge of weight (fib(k1) + fib(k2))%MOD. For, the next pair of consecutive nodes, she adds an edge of weight (fib(k1+1) + fib(k2+1))%MOD, then for the next pair (fib(k1+2) + fib(k2+2))%MOD and so on till the end of the row.
3. For the remaining rows, she uses the same algorithm incrementing the fibonacci number the same way as earlier.
4. Then she selects two more integers k3 and k4 and computes fib(k3) and fib(k4) respectively.
5. She, like filling rows, fills the columns by starting from the first column, finish adding edges in that and then move on to the next column

She wants her boyfriend to select a subset of edges such that all the nodes are connected with each other by some path and the total sum of edges in the subset is minimum over all possible subsets of edges that maintain the connectivity of the graph.

## Input format

There is only one line in input containing five space separated integers: N k1 k2 k3 k4

## Output format

Desired Output.

[link]: https://www.hackerearth.com/practice/algorithms/graphs/minimum-spanning-tree/practice-problems/algorithm/proving-your-intelligence-to-your-girlfriend-1/
