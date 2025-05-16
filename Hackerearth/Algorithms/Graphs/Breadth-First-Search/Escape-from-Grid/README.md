# [Escape from grid][link]

Assume that you are given a two-dimensional grid G that contains N rows and M columns. The grid G consists of only three integers (0, 1, and 2).

- 0 denotes an empty cell.
- 1 denotes that a cell contains a plant.
- 2 denotes a cell where you are standing initially.

You can move into an adjacent cell if that adjacent cell is empty. Two cells are adjacent if they share a side. In other words, if a cell is empty, then you can move in one of the four directions, Up, Down, Left, and Right.

You cannot move out of the grid G.

Your task is to find the length of the shortest path to reach one of the boundary edges of the grid without stepping on a plant. The length of a path is equal to the number of moves you make.

**Note:** It is guaranteed that there is only one cell with value 2 (you are standing in only one cell initially).

## Input format

- First line: Two space-separated integers, N and M, denoting the number of rows and columns in the grid G respectively.
- Next N lines: M space-separated integers denoting the rows of the grid G.

## Output format

Print the length of the shortest path to reach one of the boundary edges of the grid without stepping on a plant. If it is not possible to reach the edge of the grid, then print -1.

[link]: https://www.hackerearth.com/practice/algorithms/graphs/breadth-first-search/practice-problems/algorithm/escape-from-grid-google-ff752cb1/
