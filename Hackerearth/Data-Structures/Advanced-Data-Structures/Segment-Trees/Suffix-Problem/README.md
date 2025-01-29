# [Suffix problem][link]

You are given an array A containing N integers where every integer is represented as a 23-bit binary string. You are also given the following function:

    F(x,y) = Length of Longest Common Suffix of x and y

Write a program to resolve Q queries of the following types:

- 1 x y : Update A[x] = y
- 2 L R x: Print sum of F(A[i], x) for L <= i <= R

## Input format

- First line: Two space-separated integers N and Q
- Second line: N space-separated integers (denoting the array A)
- Next Q lines: Query of either type

## Output format

For each query of the second type, print the required sum.

[link]: https://www.hackerearth.com/practice/data-structures/advanced-data-structures/segment-trees/practice-problems/algorithm/utkarsh-and-special-function-5a877e7c/
