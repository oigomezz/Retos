# [K-th mean path][link]

Given a weighted rooted tree with n vertices. Let's call simple path from u to v vertical iff u != v and u is on simple path from root to v. The weight of the path is a sum of weights for all edges in the path. The mean weight of the path is a weight of the path divided by number of edges in it. Calculate mean weight of each vertical path, sort them and print k-th value in sorted order.

## Input format

- The first line of input contains two integers n and k (2 <= n <= 10⁶). It is guaranteed that there are at least k vertical paths in the given tree.
- Next n -1 lines contain description of edges u,v,c (1 <= u,v <= n, 1 <= c <= 10⁶).

The root of the tree is vertex 1.

## Output format

Print the k-th minimal mean weight as an irreducible fraction.

[link]: https://www.hackerearth.com/practice/data-structures/advanced-data-structures/fenwick-binary-indexed-trees/practice-problems/algorithm/k-th-mean-path/
