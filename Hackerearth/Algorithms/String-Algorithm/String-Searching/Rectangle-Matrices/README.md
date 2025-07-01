# [Rectangle matrices][link]

You are given a rectangle matrix of size 10¹⁸ x 10¹⁸. The rows of the matrix are numbered 1 to 10¹⁸ from top to bottom and the columns of the matrix are numbered 1 to 10¹⁸ from left to right. The cell of the field at the intersection of the x-th row and y-th column is represented by (x,y).

A rabbit is standing at cell (1,1). The rabbit can move from a cell (x,y) to a cell (2\*x, y) or (x,2\*y) in a few seconds because of its good speed. Also, it can move to (x, y-x) or (x-y, y).

**Note:** The rabbit cannot move out of the bounds of the matrix.

You purchase food for the rabbit for the next q days. You place the food in the cell (xi, yi) on the i-th day but you are unsure if these cells are reachable. Your task is to determine if you can reach from the cell (1,1) to the cell (xi,yi).

## Input format

- First line: Integer q denoting the number of days.
- Next q lines: Two space-separated integers xi and yi denoting the coordinates where the food is placed

## Output format

For each of q days, print Yes in a single line if there is a path from cell (1,1) to cell (xi,yi) ensuring all the requirements are met. If it is not possible, print No.

[link]: https://www.hackerearth.com/practice/algorithms/string-algorithm/string-searching/practice-problems/algorithm/jump-and-achieve-1-4588741c/
