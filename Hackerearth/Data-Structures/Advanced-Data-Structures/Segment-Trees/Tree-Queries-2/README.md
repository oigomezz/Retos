# [Tree queries][link]

You are given a tree T with N nodes rooted at 1. The i.th node of the tree has been assigned value A[i]. You are required to handle two types of queries:

- 1 v x: Update the value of node v to x, that is A[v] = x.
- 2 v: Consider the multiset of values of nodes present in the subtree of node v. Consider all non-empty subsets of this set. Alice and Bob play a game on each of these subsets (independently) alternating turns.
  - For each subset, Alice starts the game. In each turn, the current player must choose some element of the current subset and reduce it to some non-negative element. The player who cannot make a move loses. Note that it is necessary to reduce or decrease the element.
  - You need to find the number of subsets where Bob is guaranteed to win. The number of subsets can be very large, output it modulo 10⁹ + 7.

## Input format

- The first line contains an integer that denotes the number of nodes in tree T.
- The second line contains N space-separated integers denoting the initial value on the nodes of the tree(A[i])
- (N -1) lines follow. Each of these lines contains two space-separated integers u and v denoting that there is an edge between these two nodes.
- The next line contains an integer Q denoting the number of queries.
- Q lines follow. Each line is a query of the type 1 v x or 2 v.

## Output format

For each query of type 2 v, print the number of non-empty subsets of the multiset of values present in a subtree of node v when Bob wins.

[link]: https://www.hackerearth.com/practice/data-structures/advanced-data-structures/segment-trees/practice-problems/algorithm/tree-queries-6-e4926f2e/
