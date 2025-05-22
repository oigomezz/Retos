# [A strange matrix][link]

You are given a matrix A containing N rows and M columns and an integer C.

Initially, all cells are assigned some value less or equal to C. Aij is the value of the i-th row and j-th column.

Each second all cell's value is increased by 1 but it can increase maximum up to C after that value of Aij is unchanged.

On the 0-th second, you are at (1,1) cell and want to go to (N,M) cell.

At any point in time, you can jump to any adjacent cell. If you are at (i,j) , then you can go to any of the adjacent cells, (i-1,j), (i+1,j), (i,j+1), and (i,j-1). You can move to the adjacent cells only on one condition:

- You can move to any adjacent cell if and only if the value of the cell, where you are standing, is equal to the value of the adjacent cell and you can not go outside of the matrix.

**Note:** Jump time is negligible.

Your task is to determine the minimum time to reach (N,M) from the cell.

## Input format

- The first line contains three integers N,M and C denoting the total number of rows, total number of columns, and maximum height of each cell respectively.
- Next N lines contain M integers representing a matrix of N \* M dimension.

## Output format

Print single integer minimum time to reach (N,M) cell.

[link]: https://www.hackerearth.com/practice/algorithms/graphs/depth-first-search/practice-problems/algorithm/strange-matrix-8b96f2ab/
