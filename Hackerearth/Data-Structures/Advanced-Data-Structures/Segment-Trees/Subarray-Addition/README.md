# Subarray Addition

You are given an array A having N integers. You take an array B of length N such that Bi = 0 for all 1 <= i <= N. You perform Q operations of the following two types:

1. L R X: add X to all elements of the subarray A[L...R]
2. L R: add Ai to Bi for all L <= i <= R.

Print the elements of the array B after Q operations.

## Input format

- The first line of input contains two integers N, Q denoting the length of the array A and the number of operations respectively.
- The second line contains N integers A1, A2, ..., An, denoting elements of the array A.
- Each of the next Q lines contains a description of one of the two types of operations.

## Output format

Print N integers B1, B2, ..., Bn, denoting elements of the array B after Q operations.
