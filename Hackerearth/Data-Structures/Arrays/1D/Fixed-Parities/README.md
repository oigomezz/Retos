# [Fixed parities][link]

Alice and Bob are playing a board game. They have n x n boards and two arrays a and b of length n. The value of each cell in the ith row and jth row is a[i] + b[j]. Alice asks q questions to Bob. In each question, Alice provides two cells A and B. She asks the following questions to Bob:

Are there any paths from A to B that contains the same parity as A and B.

**Note:** Bob can move from one cell to 8 neighbor cells in each step.

## Input format

- First line: An integer n denoting the length of arrays.
- Second line: n integers with ai representing array a.
- Third line: n integers with bi representing array b.
- Fourth line: An integer q denoting the number of test cases.
- For each test case:
  - First line: Two integers r1,c1 denoting the row and the column of A.
  - Second line: Two integers r2,c2 denoting the row and the column of B.

## Output format

For each query, if there exists a path (for example, C) from A to B that contains the same parity as A and B, then print YES. If the parity of A and B are different, then print NO.

[link]: https://www.hackerearth.com/practice/data-structures/arrays/1-d/practice-problems/algorithm/fixed-parity-440254c0/
