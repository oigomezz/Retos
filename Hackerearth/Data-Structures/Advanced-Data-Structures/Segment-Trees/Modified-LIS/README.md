# [Modified LIS][link]

You are given a sequence of N integers as A1, A2, ... , AN. Let B be a sub-sequences of A, of maximum possible length (say k), such that each of them satisfies following conditions:

- |Bi| > |Bi-1|
- Bi \* Bi-1 < 0

for all i = 2, 3, ... k

Find number of distinct sub-sequences of length k that satisfy above conditions. Two sub-sequences are distinct if they are made up using different set of indices of sequence A.

## Input format

First line contains one integer N, denoting the size of input array. Next line contains N space separated integers, denoting the array A.

## Output format

Print two space separated integers, first one k, denoting the maximum possible size of such a sub-sequence and second integer d, the number of all such sub-sequences. Since d can be large, print it modulo 10⁹ + 7.

[link]: https://www.hackerearth.com/practice/data-structures/advanced-data-structures/segment-trees/practice-problems/algorithm/modified-lis-1/
