# Range queries

You are given a permutation of N numbers that are denoted by array A.

You are also given Q queries of the form:

- L R: For all the subsequences from the subarray A[L], A[L+1], ..., A[R] such that the length of subsequence is equal to the maximum element present in the subsequence, find the bitwise XOR of all the elements present in these subsequences.

Find the answer for Q queries.

## Input format

- The first line contains a single integer T that denotes the number of test cases.
- For each test case:
  - The first line contains an integer N.
  - The second line contains an integer Q.
  - The third line contains N space-separated integers denoting the array.
  - Next Q lines contains the queries.

## Output format

For each test case, print Q space-separated integers denoting the answer for queries in a new line.
