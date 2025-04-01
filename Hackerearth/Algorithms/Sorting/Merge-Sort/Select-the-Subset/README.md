# [Select the subset][link]

You are given an array A and B of size N.

You must select a subset of indices from 1 to N such that for any pair of indices (x,y), x!=y in the subset one of the following conditions holds true:

- A[x] < A[y] and B[x] < B[y].
- A[x] > A[y] and B[x] > B[y].
- A[x] == A[y] and B[x] != B[y].

Your task is to determine the largest possible size of a subset that satisfies the provided conditions.

**Note:** Assume 1 based indexing.

## Input format

- The first line contains an integer T that denotes the number of test cases.
- For each test case:
  - The first line contains an integer N.
  - The second line contains N space-separated integers that denotes the array A.
  - The third line contains N space-separated integers that denotes the array B.

## Output format

For each test case, print the largest possible size of a subset that satisfies the provided conditions in a new line.

[link]: https://www.hackerearth.com/practice/algorithms/sorting/merge-sort/practice-problems/algorithm/choose-subset-d983994d/
