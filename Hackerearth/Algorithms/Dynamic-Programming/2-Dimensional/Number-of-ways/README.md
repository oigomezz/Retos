# [Number of ways][link]

There is an N\*M grid in which there are N rows and M colums. A cell (i,j) is defined as the i-th row from the top and j-th column from left. You are located at (1,1) initially and can perform the following steps any number of times:

1. You can move any number of steps downwards.
2. You can move any number of steps towards the right.

There are some obstacles in the path.

You are initially located at (1,1) and wants to reach (N,M) but you are interested in knowing the number of ways you can reach (N,M) from (1,1). Since these numbers can huge, print it modulo 10⁹ + 7.

Two ways are considered different if they have a different number of steps or differ in some positions.

## Notes

1. You can never move out of the grid.
2. You cannot ignore the conditions.
3. The first cell (1,1) and the last cell (N,M) do not contain obstacles.
4. A free cell is denoted by . and an obstacle is denoted by \*.

## Input format

- The first line contains T denoting the number of test cases.
- The first line of each test case contains the number of rows N and the number of columns M.
- Each of the next N lines of each test case consist of a string of length M.

## Output format

For each test case, print a single line denoting the number of ways to reach (N,M) from (1,1) modulo 10⁹ + 7.

[link]: https://www.hackerearth.com/practice/algorithms/dynamic-programming/2-dimensional/practice-problems/algorithm/rook-path-142e55ee/
