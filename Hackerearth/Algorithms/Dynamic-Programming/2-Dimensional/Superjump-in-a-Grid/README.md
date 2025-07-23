# [Superjump in a grid][link]

You are given a N \* M grid in which each cell consists of either 0 or 1. A cell (i,j) is blocked if its value is 1. Standing at a cell (i,j), you can perform the following steps.

1. You can move right to the very next cell which is not blocked.
2. You can move down to the very next cell which is not blocked.

You are initially located at cell (1,1). Determine the number of ways in which you can reach (N,M) starting from your initial location.

Since the answer can be large, print it modulo (10⁹ + 7).

## Input format

- The first line contains N and M denoting the number of rows and the number of columns.
- Each of the next N lines consists of a string of length M.

## Output format

Print a single line containing the number of ways to reach (N,M) from (1,1) modulo 10⁹ + 7.

[link]: https://www.hackerearth.com/practice/algorithms/dynamic-programming/2-dimensional/practice-problems/algorithm/superjump-in-a-grid-773f1e31/
