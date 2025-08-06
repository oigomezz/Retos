# [A minimum sorting][link]

You are given two arrays A and B of size N. Your task is to sort array A (non-decreasing) by using the following operation for the minimum number of times.

Operation steps are:

1. Select any index i such that 1 <= i < N.
2. Swap Ai and Bi+1.
3. Swap Ai+1 and Bi.

If there is a way to sort array A using the above operation, then find the minimum number of operations that must be performed. If it is impossible to sort the array, then print -1.

## Input format

- The first line contains an integer T denoting the number of test cases.
- For each test case:
  - The first line of each test case contains an integer N denoting the number of elements in arrays A and B.
  - The second line of each test case contains N space-separated integers of array A.
  - The third line of each test case contains N space-separated integers of array B.

## Output format

For each test case, print a single line indicating the minimum number of operations if sorting can be done. If it is not possible to sort the array, print -1.

[link]: https://www.hackerearth.com/practice/algorithms/dynamic-programming/bit-masking/practice-problems/algorithm/minimum-sorting-5b67382a/
