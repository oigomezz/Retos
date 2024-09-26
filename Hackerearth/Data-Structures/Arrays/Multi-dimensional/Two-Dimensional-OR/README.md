# Two Dimensional OR

Given an n by m two dimensional 2D grid containing positive integers values, you have to answer Q queries.

In the ith query, you will be given the row and column of a start cell, (x1,y1), and the row and column of an end cell, (x2,y2). It is guaranteed that x1 <= x2, and y1 <= y2. For each query, you should return the Bitwise OR of the values in all cells (i,j) satisfying the condition x1 <= i <= x2, and y1 <= j <= y2.

## Input format

- The first line contains two integers n, and m denoting the number of rows and columns in the grid.
- The ith line among the next n lines each contains m integers, ai1,ai2,...,aim.
- The next line contains an integer Q denoting the number of queries.
- The remaining Q lines each contain 4 integers x1,y1,x2,y2 denoting the coordinates of the start and end cell, respectively.

## Output format

The output should contain Q lines, the ith of them should be the answer to the ith query.
