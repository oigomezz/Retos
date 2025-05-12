# [Min-Max Weighted Edge][link]

Given a tree with N nodes and N-1 bidirectional edges, and given an integer S. Now, you have to assign the weights to the edges of this tree such that:

1. The sum of the weights of all the edges is equal to S.
2. For every possible diameter of the tree, the maximum weight over all the edges covered by its path is the minimum possible

You have to output this minimum possible edge weight.

**Note:** The diameter of a tree is the number of nodes on the longest path between two leaves in the tree.

## Input format

- The first line of the input contains an integer T, the total number of test cases.
- The first line of each test case contains two space-separated integers N and S, the number of nodes in a tree and the integer S as mentioned in the problem statement.
- Then the N - 1 lines follow, each containing two space-separated integers u and v representing that there is a bidirectional edge between the nodes u and v.

## Output format

For each test case output the minimum possible edge weight which satisfies the above-mentioned conditions.

[link]: https://www.hackerearth.com/practice/algorithms/graphs/graph-representation/practice-problems/algorithm/min-max-weighted-edge-ni-f211b5cb/
