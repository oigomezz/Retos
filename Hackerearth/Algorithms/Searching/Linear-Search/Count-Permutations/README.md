# [Count Permutations][link]

From a permutation P of length N, Alice constructs an array A of length N such that A[i] = max(P[1], P[2], ..., P[i]). For example, if P = [2,1,3,5,4], then Alice constructs the array A = [2,2,3,5,5].

You are given an array A containing N integers. Find the number of permutations of length N from which Alice can construct the given array A. Since the answer can be very large, print it modulo 10⁹ + 7.

## Input format

- The first line contains T denoting the number of test cases. The description of T test cases is as follows:
- For each test case:
  - The first line contains a single integer N denoting the size of array N.
  - The second line contains N integers A[1], A[2], ..., A[N] denoting the elements of A.

## Output format

For each test case, print the number of permutations, modulo 10⁹ + 7 of length N from which the given array A can be constructed.

[link]: https://www.hackerearth.com/practice/algorithms/searching/linear-search/practice-problems/algorithm/count-permutations-2-b1453c05/
