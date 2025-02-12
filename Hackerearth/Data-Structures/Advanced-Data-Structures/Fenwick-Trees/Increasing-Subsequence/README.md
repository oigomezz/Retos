# [Increasing Subsequence][link]

Given an array, A, having N integers, an increasing subsequence of this array of length k is a set of k indices i1,i2,...,ik, such that 1 <= i1 < i2 < ... < ik <= N and A[i1] < A[i2] < ... < A[ik].

Energy of a subsequence is defined as sum of difference of consecutive numbers in the subsequence. For a given integer k, you need to find out the maximum value of energy among energies of all increasing subsequences of length k.

**Hint:** Among all increasing sequences of length k ending at an index, find the sequence with minimum value of starting point

## Input format

- First line consists of two space separated integer denoting N and k.
- Second line consists of N space separated integers denoting the array A.

## Output format

Print the maximum value of energy among energies of all increasing subsequences of length k. If there are no increasing subsequences of length k in the array, print "-1" (without quotes")

[link]: https://www.hackerearth.com/practice/data-structures/advanced-data-structures/fenwick-binary-indexed-trees/practice-problems/algorithm/increasing-subsequence-1-2d4df2d3/
