# Guess Permutation

A permutation of length N is an array of N integers such that every integer from 1 to N appears exactly once. For example, [2,3,4,1,5] is a permutation of length 5, while [1,2,2], [4,5,1,3] are not permutations.

For a given array B of length N+1, the difference array is an array A of length N such that A[i] = B[i+1] - B[i] for each 1 <= i <= N. For example, the difference array of the array [3,7,5,1,4] is [4,-2,-4,3].

Alice gives you an array A of length N. Find a permutation P of length N+1 such that the difference array of the permutation P and the given array A are equal. Print -1 if no such permutation exists.

## Input format

- The first line of input contains an integer N denoting the number of test cases. The description of each test case is as follows:
  - The first line of each test case contains an integer N denoting the length of the permutation.
  - The second line of each test case contains N integers A[1], A[2], ..., A[N], denoting the elements of the array A.

## Output format

For each test case, print -1 if no suitable permutation exists or print N+1 space-separated integer denoting the elements of the permutation.
