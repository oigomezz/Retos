# [Length of a valley][link]

You are given an integer array A consisting of N elements. For each element, you are required to find the length of the valley that is defined as:

Let i be the current index and l and r be the leftmost and rightmost index satisfying this property A[l] > A[l+1] > ... > A[i-1] > A[i] < A[i+1] < ... < A[r-1] < A[r], then (r-l+1) is the length of the valley.

## Input format

- The first line contains an integer T denoting the number of test cases.
- The first line of each test case contains an integer N denoting the number of elements in array A.
- The second line of each test case contains N space-separated integers of array A.

## Output format

Print T lines. For each test case, print N space-separated integers denoting the length of the valley for each index.

[link]: https://www.hackerearth.com/practice/algorithms/dynamic-programming/introduction-to-dynamic-programming-1/practice-problems/algorithm/hill-150045b2/
