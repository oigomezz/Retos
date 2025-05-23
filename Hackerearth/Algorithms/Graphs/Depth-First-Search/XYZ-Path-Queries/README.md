# [XYZ Path queries][link]

Given a tree with N nodes (numbered 1 to N). For each valid i, the i-th node has a value of A[i] associated with it.

Your target is to handle the queries of the following 4 types

- "1 X Y": Sum of values of all the nodes in the path from X to Y.
- "2 X Y": Sum of pairwise OR of every possible pair in the path from X to Y i.e. ∑(a[i] | a[j]) where i < j.
- "3 X Y": Sum of OR of all triplet in the path from X to Y i.e. ∑(a[i] | a[j] | a[k]) where i < j < k.
- "4 X Y": Sum of OR of all groups of type (a,b,c,d) in the path from X to Y i.e. ∑(a[i] | a[j] | a[k] | a[l]) where i < j < k < l.

For each query answer can be very large so print it MODULO 1000000007 (1e9 + 7).

## Input format

- First-line contains N, the number of nodes in the tree.
- Next line contains N space-separated integers denoting A[i].
- Next N-1 lines contain two space-separated integers x and y which denote that there is an edge between node u and node v.
- The next line contains Q, the number of queries to process.
- Next, Q lines follow with one of the four queries per line.

## Output format

For each query print a single integer denoting it's sum as described in the problem.

[link]: https://www.hackerearth.com/practice/algorithms/graphs/depth-first-search/practice-problems/algorithm/path-queries-ba308c8e/
