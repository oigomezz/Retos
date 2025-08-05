# [Gold Mines][link]

There is a rectangular grid of gold mine. The grid has R rows and C columns. So it has R\*C cells in total. The rows are numbered from 1 to R and the columns are numbered from 1 to C. The top most row has number 1, the row next to it has number 2 and so on. Similarly, the left most column has number 1, the column next to it has number 2 and so on. Each cell in the grid has a unique coordinate which is (x, y) where x is the row number and y is the column number of that particular cell.

Each cell in the grid has certain amount of gold in it. Total gold in a sub rectangle of the grid is the sum of all units of gold contained in the cells that are inside the rectangle. Your task is to find the total gold in the given sub rectangle.

A sub rectangle of the grid is defined by four integers x1, y1, x2 and y2. A cell (x, y) belongs to the sub rectangle if and only if x1 <= x <= x2 and y1 <= y <=y2.

## Input format

- First line of the input contains two space separated integers, R and C.
- It is followed by R lines, each line has C space separated integers. Each integer denotes the units of gold present in that particular cell.
- Next line has number Q.
- It is followed by Q queries each query in a single line. Each query is four space separated integers x1, y1, x2 and y2.

## Output format

For each query, you have to print a single number the total gold contained in that sub rectangle.

[link]: https://www.hackerearth.com/practice/algorithms/dynamic-programming/2-dimensional/practice-problems/algorithm/gold-mines-10/
