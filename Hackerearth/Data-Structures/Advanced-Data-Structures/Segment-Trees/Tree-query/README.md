# [Tree query][link]

A tree is a simple graph in which every two vertices are connected by exactly one path. You are given a rooted tree with n vertices and a lamp is placed on each vertex of the tree.

You are given q queries of the following two types:

- 1 v: You switch the lamp placed on the vertex v, that is, either from On to Off or Off to On.
- 2 v: Determine the number of vertices connected to the subtree of v if you only consider the lamps that are in On state. In other words, determine the number of vertices in the subtree of v, such as u, that can reach from v by using only the vertices that have lamps in the On state.

**Note:** Initially, all the lamps are turned On and the tree is rooted from vertex number 1.

## Input format

- First line: Two integers n and q denoting the number of vertices and queries.
- Next n-1 lines: Two number ai and bi denoting an edge between the vertices ai and bi.
- Next Q lines: Two integers ti and vi, where ti is the type of the ith query.

## Output format

For every query of type 2, print the answer in a single line.

[link]: https://www.hackerearth.com/practice/data-structures/advanced-data-structures/segment-trees/practice-problems/algorithm/tree-query-3-5d98588f/
