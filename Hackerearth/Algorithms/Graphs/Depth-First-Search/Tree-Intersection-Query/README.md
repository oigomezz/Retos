# [Tree Intersection Query][link]

You are given a tree consisting of N nodes. You have to answer Q queries. The q-th query consists of a node xq and a set of kq distinct nodes {v1,v2,..., vkq}. The answer to the q-th query is the number of pairs (i,j) such that 1 <= i < j <= kq and the node xq lies on the path between the nodes vi and vj.

## Input format

- The first line of input contains two integers N denoting the number of nodes in the tree and Q denoting the number of queries.
- N-1 lines follow. The i-th line contains two integers Xi,Yi denoting an edge between the nodes Xi,Yi. It is guaranteed that the given nodes and edges form a tree.
- 2 \* Q lines follow. The (2 \* q - 1)-th of these lines contains two integers xq, kq, and the 2\*q-th line contains kq space-separated distinct integers {v1,v2,..., vkq}.

## Output format

For each query, print the answer in a separate line.

[link]: https://www.hackerearth.com/practice/algorithms/graphs/depth-first-search/practice-problems/algorithm/tree-intersection-query-ba554a53/
