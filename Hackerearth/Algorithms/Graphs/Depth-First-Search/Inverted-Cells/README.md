# [Inverted cells][link]

You are given a matrix n \* m . The matrix rows are numbered from 1 to n from top to bottom and the matrix columns are numbered from 1 to m from left to right. The cells of the field at the intersection of the x-th row and the y-th column has coordinates (x,y).

Every cell is empty or blocked. For every cell (x,y), determine if you change the state of cell (x,y) (empty to blocked or blocked to empty), then is it possible to reach cell (n,m) from (1,1) by going only down and right.

## Input format

- The first line contains two space-separated numbers n,m denoting the number of rows and columns.
- Next n lines contain symbols. If the symbol on (x,y) is '#', then the cell is blocked. Otherwise, if the symbol is '.', then the cell is empty.

## Output format

Print n lines where every line contains m numbers. Print 0 if it is impossible to reach (n,m). Otherwise, print 1.

[link]: https://www.hackerearth.com/practice/algorithms/graphs/depth-first-search/practice-problems/algorithm/inverted-cells-83eae42d/
