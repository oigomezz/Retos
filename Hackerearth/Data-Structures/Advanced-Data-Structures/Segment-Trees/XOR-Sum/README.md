# XOR sum

You are given an array A of size N. Now you are given Q queries to be performed over this array. In each query, you are given 2 space separated integers L and R. For each query, you need to you need to find the summation of the xor-sum of all triplets (i,j,k) of the sub-array L...R, where L <= i < j < k <= R.

## Input format

- The first line contains a single integerN.
- The next line contains array A of N integers.
- The next line contains 2 space separated integers Q and 2.
- Each of the next Q lines contains two space separated integers L and R.

## Output format

Print Q lines, the ith line denoting the answer to the ith query, Modulo 10⁹ + 7.
