# [The minimum cost of a path][link]

You are given a 2D matrix containing N rows and M columns. You are currently standing at cell (1,1) and you want to reach cell (n,m).

You can only move right or down from your current cell, that is, if you are currently in cell (i,j), then you can either move to cell (i+1,j) or cell (i,j+1). You cannot move out of the matrix.

Each cell of the grid has some cost associated with it which you have to pay when you land at that cell.

Each cell has a number K associated with it. Now, the cost of that cell is defined as the maximum number of times you can divide K by a positive integer X that is greater than 1 until K becomes 1. Here, K must be divisible by X.

The cost of a path is defined as the sum of the costs of all the cells in the path.

Note: You also have to pay the cost at cell (1,1) as you are standing on it.

You are required to determine the minimum cost to reach from cell (1,1) to cell (n,m).

## Input format

- The first line of the input contains T denoting the number of test cases.
- The first line of each test case contains two integers N and M denoting the number of rows and columns respectively.
- The next N lines of each test case contain integers representing the numbers on each cell of the grid.

## Output format

For each test case, print a single line containing the minimum cost.

[link]: https://www.hackerearth.com/practice/algorithms/dynamic-programming/2-dimensional/practice-problems/algorithm/minimum-cost-path-in-a-grid-2-2e1df6ef/
