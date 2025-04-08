# [Flip AB][link]

Given two grids, both with n rows and m columns, and cells containing either the letter 'A' or the letter 'B'. Determine if it is possible to use either of the subsequent operations any number of times, including 0, to transform the first grid, grid1, to the second grid, grid2:

- **ROW FLIP:** In this operation, you choose a row in grid1 and flip all the characters in the chosen row.
- **COLUMN FLIP:** In this operation, you choose a column in grid1 and flip all the characters in the chosen column.

A flip changes the letter 'A' to letter 'B', and vice-versa.

Your program should output "YES" (without quotes) if it is possible to convert grid1 to grid2, and "NO" (without quotes) otherwise.

**NOTE:** You can perform the operations on grid1 only.

## Input format

- The first line contains an integer t, denoting the number of test cases.
- The first line of each test case contains two integers n and m, denoting the number of rows, and columns both grids have.
- The following n lines of each test case contain a string of length m having characters as either 'A' or 'B' - denoting the characters in grid1.
- The final n lines of each test case contain a string of length having characters as either 'A' or 'B' - denoting the characters in grid2.

## Output format

Output a string "YES" (without quotes) if it is possible to convert grid1 to grid2, and a string "NO" (without quotes) otherwise.

[link]: https://www.hackerearth.com/practice/algorithms/greedy/basics-of-greedy-algorithms/practice-problems/algorithm/flip-ab-26df82b3/
