# [Minimum Adjacent Difference][link]

You are given two arrays A,B, each containing N integers. You want to minimize the maximum absolute difference between two adjacent integers of the array A. You can do the following operation atmost K times:

- Choose an index i (1 <= i <= N) and swap A[i], B[i].

Find the minimum possible value of max |A[i] - A[i+1]|

## Input format

- The first line contains T denoting the number of test cases. The description of T test cases is as follows:
- For each test case:
  - The first line contains two integers N,K denoting the size of array A and the maximum number of operations to be performed respectively.
  - The second line contains N space-separated integers - denoting the elements of the array A.
  - The third line contains N space-separated integers - denoting the elements of the array B.

## Output format

For each test case, print the minimum possible value of max |A[i] - A[i+1]|.

[link]: https://www.hackerearth.com/practice/algorithms/dynamic-programming/introduction-to-dynamic-programming-1/practice-problems/algorithm/minimum-adjacent-difference-94b4c882/
