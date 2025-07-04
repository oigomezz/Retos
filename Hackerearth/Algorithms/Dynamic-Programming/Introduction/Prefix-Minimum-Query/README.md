# [Prefix Minimum Query][link]

You are given an array A having N integers. You have to answer Q queries. The i-th query is denoted by two integers Li,Ri. The answer to the i-th query is A[Li] + min(A[Li], A[Li+1]) + ... + min(A[Li], A[Li+1], ..., A[Ri]).

For each query find the answer.

**Note:** Since the size of the input and output is large, please use in memory stack size accordingly otherwise you may see error.

## Input format

- The first line of input contains two integers N,Q denoting the length of the array A and the number of queries respectively.
- The second line contains N integers A1,A2,...,AN denoting elements of the array A.
- Each of the next Q contains two space-separated integers Li,Ri.

## Output format

For each query, print the answer in a separate line.

[link]: https://www.hackerearth.com/practice/algorithms/dynamic-programming/introduction-to-dynamic-programming-1/practice-problems/algorithm/prefix-minimum-query-4d47a2ee/
