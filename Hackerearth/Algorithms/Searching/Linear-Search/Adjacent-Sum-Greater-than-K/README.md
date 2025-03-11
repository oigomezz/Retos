# [Adjacent Sum Greater than K][link]

A permutation of length N is an array of N integers such that every integer from 1 to N appears exactly once. For example, [2,3,5,4,1] is a permutation of length 5, while [1,2,2], [4,5,1,3] are not permutations.

You are given two integers N,K. Find a permutation P of length N such that P[i] + P[i+1] >= K for each 1 <= i < N. If there are multiple permutations find the lexicographically smallest one. Print -1 if no such permutation exists.

A permutation P is lexicographically smaller than a permutation Q of the same length N if there exists an index 1 <= i <= N such that P[1] = Q[1], P[2] = Q[2], ... and P[i] < Q[i].

## Input format

- The first line of input contains an integer T denoting the number of test cases. The description of each test case is as follows:
- The first line of each test case contains two integers N,K.

## Output format

For each test case, print -1 if no suitable permutation exists, otherwise print the lexicographically smallest permutation satisfying the conditions.

[link]: https://www.hackerearth.com/practice/algorithms/searching/linear-search/practice-problems/algorithm/adjacent-sum-greater-than-k-f41e3ec4/
