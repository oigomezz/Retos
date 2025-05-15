# [Two gold mines][link]

You have given a n x n matrix containing empty spaces or walls. You have a team of 2 players where the position of each player is given. There are 2 gold mines on the map. Your aim is to pick gold from both these mines.

You are required to find the minimum time required to pick gold from both gold mines.

In one second, they all simultaneously can move in any of the four directions and any player can pick any number of gold including 0.

## Input format

- The first line contains t denoting the total number of test cases.
- The first line of each test case contains an integer n denoting the number of rows and columns in the matrix.
- The next n lines of each test case contain characters denoting the rows of the matrix.
  - "." denotes an empty cell.
  - "#" denotes a wall.
  - "^" denotes a player.
  - "\*" denotes a gold mine

## Output format

The output contains the following two lines:

- The first line contains "Yes" (without quotes) if it is possible to collect both the mines or "No" (without quotes) if you are unable to pick both the mines.
- The second line contains the minimum time required to pick both the gold mines.

In the case of "No", do not print the second line.

[link]: https://www.hackerearth.com/practice/algorithms/graphs/breadth-first-search/practice-problems/algorithm/ujjwals-mine-9eacab11/
