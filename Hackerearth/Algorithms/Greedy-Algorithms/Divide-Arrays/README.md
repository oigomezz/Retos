# [Divide arrays][link]

You are given an array A of N integers. Find the smallest index i such that:

- mex(A[1], A[2], ..., A[i]) = mex(A[i+1], A[i+2], ..., A[N])

If no such index exists, print -1.

## Note

- 1-based Indexing is followed.
- mex of an array of elements is defined as the minimum non-negative number missing from the array.

## Input format

- The first line contains an integer T denoting the number of test cases.
- For each test case:
  - The first line of each test case contains an integer N denoting the number of elements in array A.
  - The second line contains N space-separated integers denoting the elements of the array.

## Output format

For each test case in a new line, print the smallest index satisfying the condition.

[link]: https://www.hackerearth.com/practice/algorithms/greedy/basics-of-greedy-algorithms/practice-problems/algorithm/divide-array-3-10ef1aae/
