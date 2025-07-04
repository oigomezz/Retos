# [Prefix XOR Sum][link]

You are given an array A containing N integers and Q queries. Each query is denoted by two integers L,R. The answer to a query is A[L] + (A[L] ⊕ A[L+1]) + ... + (A[L] ⊕ A[L+1] ⊕ A[L+2] ⊕ ... ⊕ A[R]), where ⊕ denotes the bitwise XOR operator.

## Input format

- The first line contains two integers N denoting the size of array A and Q denoting the number of queries.
- The second line contains N space-separated integers A1,A2,...,AN denoting the elements of A.
- Each of the next Q lines contains two integers L,R.

## Output format

For each test query, print the answer in a separate line.

[link]: https://www.hackerearth.com/practice/algorithms/dynamic-programming/introduction-to-dynamic-programming-1/practice-problems/algorithm/prefix-xor-sum-0e16e052/
