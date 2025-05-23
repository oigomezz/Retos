# [Separating Numbers][link]

We are given a tree with N nodes. Each node has a color Ci. We are also given N-1 queries and in each query we are told to destroy a previously undestroyed edge. Every time we destroy an edge, we have to report the number of pairs of nodes that get disconnected. Here, two nodes i and j are said to be disconnected if before the destruction you could reach from i to j using edges not yet destroyed , and if Ci = Cj.

## Input format

- The first line contains a single integer N.
- The next N-1 lines contain two space separated integers a and b which means that there is an edge between a and b in the tree.
- The next line contains N space separated integers where the i-th integer denotes the value of Ci.
- The last line contains N-1 space separated integers Di - the i-th integer denotes that the Di-th edge (in the order in which edges are given in input) is deleted in the i-th step.

## Output format

For every deleted edge, output the number of disconnected values on a new line.

[link]: https://www.hackerearth.com/practice/algorithms/graphs/depth-first-search/practice-problems/algorithm/separating-numbers-6fe976a9/
