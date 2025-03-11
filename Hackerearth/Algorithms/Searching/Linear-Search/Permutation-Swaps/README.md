# [Permutation Swaps][link]

A permutation of length N is an array of N integers such that every integer from 1 to N appears exactly once. For example, [2,3,4,1,5] is a permutation of length 5, while [1,2,2], [4,5,1,3] are not permutations.

You are given an array A having N integers. You can apply the following operation on the array A any number of times:

- Choose two indices i,j such that 1 <= i < j <= N, then decrease 1 from A[i] and add 1 to A[j].

Find if it is possible to convert the array A into a permutation of length N.

## Input format

- The first line of input contains an integer T denoting the number of test cases. The description of each test case is as follows:
  - The first line of each test case contains an integer N denoting the length of the array.
  - The second line of each test case contains N integers A[1], A[2], ..., A[N], denoting the elements of the array A.

## Output format

For each test case, print YES if it is possible to obtain a permutation from the array A using the given operation, otherwise print NO.

[link]: https://www.hackerearth.com/practice/algorithms/searching/linear-search/practice-problems/algorithm/guess-permutation-2-be0b2b90/
