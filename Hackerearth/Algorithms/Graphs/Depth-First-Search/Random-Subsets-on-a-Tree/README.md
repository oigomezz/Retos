# [Random subsets on a tree][link]

You are given a tree that is rooted at 1 and contains N nodes. Each node u has a value assigned to it that is denoted as Val[u]. A subset of nodes is selected in a random manner. Any node can be selected with equal probability.

The value of the subset is defined as follows:

- Let the lowest common ancestor of these nodes be L. If Val[L] is greater than Val[u] for all u belonging to this subset, then the score of this subset is u. Otherwise, the score is 1. For an empty subset, the score is 0.

You must determine the expected score of the subset. The answer can be represented as P/Q.

Print the answer as P/Q modulo 10⁹ + 7.

## Input format

- First line: A single integer N denoting the total number of nodes in the tree.
- Next N-1 lines: Two space-separated integers u and v denoting an edge between u and v.
- Next line: N space-separated integers where the i-th integer denotes Val[i].

## Output format

Print the required value modulo 10⁹ + 7.

[link]: https://www.hackerearth.com/practice/algorithms/graphs/depth-first-search/practice-problems/algorithm/random-subset-on-a-tree-22172a94/
