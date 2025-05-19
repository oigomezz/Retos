# [Prime cells][link]

You are given a matrix M of R rows and C columns. You are required to maximize the size of a prime cell. A prime cell is the largest group of connected cells. A cell may only be connected with its adjacent cells in the direction up, down, left, and right that has the same count of prime factors. You are allowed to perform any number of operations. In one operation, you can change a number to another number. A cost is associated to change the number. This cost is the absolute difference between the highest prime factors of both the numbers. The maximum value of the modified matrix should not exceed the maximum value of the input matrix.

**Note:** Assume that the highest prime factor and the count of prime factors for 1 is 1. If two prime cells with the same size are found the one with the largest score will be considered.

Your task is to maximize the score.

## Input format

- First line: Two space-separated integers R and C denoting the number of rows and the number of columns respectively.
- Next R lines: C space-separated integers denoting the value of matrix Mij.

## Output format

Your task is to print the two space-separated integers R and C denoting the number of rows and the number of columns respectively. These integers must be followed by the modified matrix from a new line.

[link]: https://www.hackerearth.com/practice/algorithms/graphs/breadth-first-search/practice-problems/approximate/prime-islandindeed-d7a30488/
