# [Rasta and The Matrix][link]

Rasta loves matrices. He has a 10¹⁸ × 10¹⁸ matrix. Every cell has a color, initially white.

Rasta also loves queries. He asks you to perform q queries. We have queries of two types:

- 1 x l r: if x = 0, then it means that you should change the color of all cells in rows l, l+1, ..., r (white to black and black to white). Otherwise (x = 1) you should do this to columns number l, l+1, ... r.
- 2 l r x y: You should print the number of black cells in subrectangle of this matrix, consisting of rows number l, l+1, ..., r and columns number x, x+1, ..., y.

## Input format

- The first line of input contains one number, n (1 ≤ n ≤ 10⁵).
- The next n lines each line contains one query.

## Output format

For each query of type 2 print the answer modulo 10⁹ + 7 in one line.

[link]: https://www.hackerearth.com/practice/data-structures/advanced-data-structures/segment-trees/practice-problems/algorithm/rasta-and-the-matrix/
