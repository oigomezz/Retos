# [Grids Everywhere][link]

A n x m grid consists of 'n' rows and 'm' columns. You are given 'n' elements, where each ni denotes the sum of elements of the ith row of the grid. You are also given 'm' elements, where each mi denotes the sum of elements of the ith column of the grid. You need to construct the grid by filling the desired cells with values in the range [1, 5] inclusive such that when elements arranged row-wise (a11, a12, a21, a22) represent the lexicographically shortest solution of the grid. Here aij represents the element at ith row and jth column.

## Input format

- There are 't' test cases.
- For each test case you will be given 'n' - number of rows and 'm' - number of columns.
- This is followed by a line containing 'n' space separated integers 'ni', sum of elements of the ith row.
- Next line contains 'm' space separated integers 'mi', sum of elements of the ith column.

## Output format

You need to print the lexicographically shortest grid solution. There always exists a solution. This needs to be printed in 'n' lines, each line containing 'm' space separated elements of the 'ni' row.

As for a 2 x 2 grid print:

    a11 a12
    a21 a22

[link]: https://www.hackerearth.com/practice/algorithms/graphs/maximum-flow/practice-problems/algorithm/grids-everywhere/
