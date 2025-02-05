# [Joseph and Tree][link]

Joseph loves games about a tree! His friend Nick invented a game for him!

Initially, there is a rooted weighted tree with N vertices numbered 1 ... N. Nick guarantees that the tree is connected, and there is a unique path between any vertices! Also he gave us Q queries on it of following type:

- v and k : Let S denote the sorted (non decreasing order) array of shortest distances from v to any other vertex from subtree rooted v. Answer will be k-th element of S. If such a number does not exist, i.e. the S has less than k elements, answer is 1. Note that v is not included in his own subtree.

All the indices in the queries are 1-based. Root of the tree is node 1.

But it turns out, Joseph has an exam tomorrow, and he doesn't have time for playing a game! And he asks your help!

## Input format

- The first line contains a single integer N denoting the number of vertices of the tree.
- The next N-1 lines contain three integers ai,bi and wi, denoting that there is an edge between vertices ai and bi with weight wi.
- The next line contains a single integer Q denoting the number of queries.
- The next Q lines contain two integers vi and ki, denoting the query described above.

## Output format

Print the answer for each query. Note that if there is no such element, print 1.

[link]: https://www.hackerearth.com/practice/data-structures/advanced-data-structures/segment-trees/practice-problems/algorithm/joseph-and-treeaugclash/
