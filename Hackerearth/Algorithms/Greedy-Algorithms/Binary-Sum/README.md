# [Binary Sum][link]

Given an array S of N length consisting of only binary numbers (0 or 1). We need to decompose S into K consecutive non-empty subarrays such that every element is present in only one subarray.

Say subarrays are S[1], S[2], S[3], .... , S[K]. Choose an array B , which is a permutation of 1 to K i.e. it is of size K and include every element from 1 to K.

Now , form a new array V = S[B[1]] + S[B[2]] + ...... + S[B[K]].

Suppose, X is equal to the count of subarrays in V such that sum of elements in the subarray is greater than the Floor(length of the subarray / 2).

Aim is to maximize X.

## Input format

- First line contains two space-separated integers : N and K
- Second line contains N space-separated integers denoting array S.

## Output format

- In the first K lines, print one integer denoting end index of i-th subarray (indexes are 1 based).
- In next line print K space separated integers, denoting array B (permutation of 1 to K)
- End index of subarray should be in increasing order.

[link]: https://www.hackerearth.com/practice/algorithms/greedy/basics-of-greedy-algorithms/practice-problems/approximate/binary-sum-2c11887a/
