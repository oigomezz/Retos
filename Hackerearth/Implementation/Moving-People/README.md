# Moving People

The people of your city are living in a N x M grid. If a person is out of the grid after multiple instructions, then that person is not counted in further steps.

Initially, there is at most one person in every cell of this grid. You can perform Q operations or query of the following types:

1. X Y: Move every person that is currently residing in the grid, X column left of their cells and Y column above of their cells. If X is negetive, then move people abs(X) column right of their cells. Also, if Y is negative, then move people abs(Y) column down of their cells.

2. Calculate the numbner of people that are currently living in the grid.

## Input format

- First line: Three integers, N,M, and Q denoting the number of rows that are available in the grid, number of columns that are available in the grid, and number of instructions.
- Next N lines: A string consisting of only 0 and 1. In the ith string, the jth character is 1 if there is a person in that cell, otherwise there will be 0
- Next Q lines: One of the 2 types of operations as stated above.

## Output format

For each 2nd type of query, print the number of persons that are available in the grid at the time of that query.
