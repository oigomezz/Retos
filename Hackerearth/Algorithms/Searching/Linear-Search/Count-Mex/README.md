# [Count Mex][link]

The MEX of an array is the minimum non-negative integer that is not present in it. For example,

- The MEX of array [2,5,0,1] is 3, because it contains 0,1,2 and 5 but not 3.
- The MEX of array [1,2,5] is 0, because 0 is the smallest non-negative integer not present in the array.
- The MEX of array [0,1,2,3] is 4.

You are given a permutation P of the integers {0,1,2,...,N-1}.

For each i from 1 to N, find the number of subarrays of the permutation P such that the MEX of the subarray is equal to i.

An array B is a subarray of an array A if B can be obtained from aa by deletion of several (possibly, zero or all) elements from the beginning and several (possibly, zero or all) elements from the end. In particular, an array is a subarray of itself.

## Input format

- The first line of input contains an integer T denoting the number of test cases. The description of each test case is as follows:
  - The first line of each test case contains an integer N denoting the length of the permutation P.
  - The second line of each test case contains N integers P[1], P[2], ..., P[N], denoting the elements of the permutation P.

## Output format

For each test case, print N space-separated integer where the i-th integer denotes the number of subarrays of the permutation P such that the MEX of the subarray is equal to i.

[link]: https://www.hackerearth.com/practice/algorithms/searching/linear-search/practice-problems/algorithm/count-mex-8dd2c00c/
