# [Permutation and Inversions][link]

For a permutation P of N numbers, let us define the cyclic shift of P as another permutation Pd such that Pd[i] = P[i+1] for all i from 1 to N-1, and Pd[N] = P[1].

We can create N distinct permutations by applying the cyclic shift operation N times.

For an array P of N numbers, let us define the number of inversions in it as the number of pairs (i,j) such that i < j and P[i] > P[j].

For each of the N distinct permutations created by applying the cyclic shift operations on the initial permutation, consider it as an array of N numbers and find the number of inversions in it. Print the bitwise XOR of the number of inversions in each newly created permutation.

You need to handle T test cases each containing a new permutation.

## Input format

First line of input contains an integer T, denoting the number of test cases. Each test case contains 2 lines. First line of each test case contains a single integer N, denoting the number of elements in the permutation P. Next line of each test case contains N space separated integers denoting the permutation P.

## Output format

For each testcase, print an integer, the bitwise XOR of the number of inversions in each permutation which are created by cyclic shifts on the initial permutation.

[link]: https://www.hackerearth.com/practice/data-structures/advanced-data-structures/fenwick-binary-indexed-trees/practice-problems/algorithm/permutation-and-inversions-43b5147e/
