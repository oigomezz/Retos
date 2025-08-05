# [Longest Increasing Path][link]

There is a 2D matrix of N rows and M columns. Rows are number 1 to N from top to bottom and columns 1 to M from left to right. You are standing at (1,1).

From, A [ i ] [ j ] you can move to A [ i + 1 ] [ j ] if A [ i + 1 ] [ j ] > A [ i ] [ j ]. Or, from, A [ i ] [ j ] you can move to A [ i ] [ j + 1 ] if A [ i ] [ j + 1 ] > A [ i ] [ j ].

Moving from (1,1), what is the longest path that you can travel?

## Input format

- First line contains, T, the number of testcases.
- Each testcase consists of N, M.
- Each of the next N lines contain M integers each.

## Output format

For each testcase, print the length of the longest path from (1,1).

[link]: https://www.hackerearth.com/practice/algorithms/dynamic-programming/2-dimensional/practice-problems/algorithm/longest-increasing-path-9/
