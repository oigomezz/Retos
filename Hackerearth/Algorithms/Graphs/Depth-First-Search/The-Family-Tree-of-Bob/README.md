# [The family tree of Bob][link]

Bob wants to know about his ancestors, therefore, he draws a graph of his family. In that graph, root is the eldest-known family member. The leaf node is a member who has no children.

You are given a Q query and N family members. They have to just print the k-th ancestors with respect to that query. A member can have only one parent.

Note: Print -1 if the query is incorrect, that is, if the k-th ancestor is not available. The root of the tree is 1.

## Input format

- The first line contains two space-separated integers N and Q denoting the number of nodes and the number of queries.
- Next N - 1 lines contain two space-separated integers u and v denoting an edge between node u and node v.
- Next Q lines contain two space-separated integers u and k.

## Output format

For each query, print a single line containing one integer.

[link]: https://www.hackerearth.com/practice/algorithms/graphs/depth-first-search/practice-problems/algorithm/family-tree-of-aman-f2e011b3/
