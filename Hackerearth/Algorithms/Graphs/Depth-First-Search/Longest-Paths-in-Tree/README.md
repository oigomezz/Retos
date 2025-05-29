# [Longest Paths in Tree][link]

You are given a tree. Simple path of length m is a sequence of vertices v1,v2,..,vm such that

- All vi are distinct.
- vi and vi+1 are connected by edge for 1 <= i <= m-1.

For each vertex find length of longest simple path that goes through this vertex. Also count number of this paths. Two paths considered distinct if set of vertices of this paths differ.

## Input format

- First line of input contains single positive integer n, number of vertices of the tree.
- Next n-1 lines contains pairs space-separated integers ui,vi, edges of the tree.

## Output format

Output n lines. i-th line must contain two integers -- length of the longest simple path containing vertex i and number of such paths.

[link]: https://www.hackerearth.com/practice/algorithms/graphs/depth-first-search/practice-problems/algorithm/longest-paths-in-tree/
