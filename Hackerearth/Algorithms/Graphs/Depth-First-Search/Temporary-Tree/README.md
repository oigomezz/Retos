# [Temporary Tree][link]

You are gifted a tree consisting of N vertices. There are two types of edges each with a weight val and denoted by a type value that is either 0 or 1. A pair (i,j), where i < j is called GOOD if, while traversing from vertex i to vertex j, we never pass through an edge of type 0.

Your task is to calculate the sum of the path’s weight of all the GOOD pairs present in the tree. Print the final answer modulo 10⁹ + 7.

## Input format

- The first line of input contains an integer T, denoting the number of test cases.
- The first line of each test case contains the integer N.
- The next N-1 line contains four integers A, B, type and val where A and B represents the vertices of the tree, type represent the type of the edge and val define the edge weight.

## Output format

For each test case, print an integer denoting the sum of the path's weight of all the GOOD pairs modulo 10⁹ + 7.

[link]: https://www.hackerearth.com/practice/algorithms/graphs/depth-first-search/practice-problems/algorithm/temporary-tree-07d4d9a3/
