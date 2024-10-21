# Make Permutation

A permutation is a sequence of integers from 1 to N of length N containing each number exactly once. For example (1), (4,3,5,1,2), (3,2,1) are permutations, and (1,1), (4,3,1), (2,3,4) are not.

An array B is called good if it can be converted to a permutation by applying the following operation any number of times (possibly zero):

- Choose an index i of B of and a positive integer x, then set Bi = Bi - x.

For example, the arrays [1,3,5], [1,3,3], [2,2] are good arrays while the arrays [1,2,2], [2,4,1,1] are not good.

You are given an array A containing N integers. Find the number of good subarrays of A.

## Input format

- The first line contains T denoting the number of test cases. The description of T test cases is as follows:
- For each test case:
  - The first line contains a single integer N denoting the size of array A.
  - The second line contains N integers A1,A2,...,An - denoting the elements of A.

## Output format

For each test case, print the answer in a separate line.
