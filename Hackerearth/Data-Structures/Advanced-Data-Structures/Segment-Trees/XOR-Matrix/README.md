# [XOR Matrix][link]

A square matrix of size x \* x will be beautiful if XOR of every two adjacent cells equal to 1. We will consider cells of a square matrix as adjacent if they have a common side, that is for cell (r,c) cells (r, c-1), (r,c+1), (r-1,c) and (r+1,c) are adjacent to that (if they're in the matrix).

You're given a square matrix A of size N \* N, where value of each cell equal to 0 or 1. You are given Q queries and in each query you are given top left cell (x1,y1) and bottom right cell (x2,y2) of a submatrix, find the side length of largest possible beautiful square matrix inside the submatrix given in query.

Top left cell of N \* N size matrix is (1,1) and bottom right cell is (N,N). A single cell is also beautiful.

## Input format

- First line will contain T, number of testcases. Then the testcases follow.
- First line of each test case contain a single integer N, side length of matrix.
- Next each N lines each conatins N space separated integer denoting value of each cell.
- Next line contains a integer Q denoting number of queries.
- Next Q lines each contains four integers x1, y1, x2, y2.

## Output format

For each query, output in a single line the length of largest possible beautiful square matrix inside the submatrix given in query.

[link]: https://www.hackerearth.com/practice/data-structures/advanced-data-structures/segment-trees/practice-problems/algorithm/xor-matrix-3-233eaca4/
