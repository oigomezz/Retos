# [Rooted trees][link]

You are given a rooted tree of N nodes. Each node i contains a value ai. Initially, all values of the node are 0, your task is to process Q queries of the following two types:

- 0 v x: for every node u in a subtree of v if au < Y add x to au.
- 1 v print the value au

The tree is rooted at -1.

## Input format

- Each test contains multiple test cases.
  - The first line contains t denoting the number of test cases.
  - The first line of each test case contains two integers N, Q, and Y. These integers describe the size of the tree, the number of the queries, and the integer described in the statement respectively.
  - The i-th of the next n-1 lines contains two integers ui and vi which means that there is an edge between nodes ui and vi.
  - Each of the next Q lines contains a query of the following two types:
    - 0 v x.
    - 1 v.

## Output format

For each query of type 1 v, print av.

[link]: https://www.hackerearth.com/practice/algorithms/graphs/graph-representation/practice-problems/algorithm/hemose-asking-bakry-about-trees-e9598556/
