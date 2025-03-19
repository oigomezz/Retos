# [Failed ranges][link]

You are given two sorted arrays A and B of sizes N and M respectively. C is the following:

- An array of size N∗M such that C[k]=(A[i] + B[j]) for all possible i and j.
- C is a sorted array.

## Task

You are given two integers X and Y. Determine all the possible pairs of i,j such that A[i] + B[j] is:

- Greater than the Xth greatest element of array C
- Less than the Yth greatest element of array C

This means that you have to determine all possible i and j such that Xth greatest< A[i] + B[j] < Yth greatest

## Input format

- The first line contains two space-separated integers N and M as described in the problem statement.
- The second line contains N space-separated integers denoting the elements of array A.
- The third line contains M space-separated integers denoting the elements of array B.
- The fourth line contains two space-separated integers X and Y as described in the problem statement.

## Output format

Print the output in two lines as follows:

- First line: Print the number of pairs of i and j that satisfy the input that is provided.
- Second line: Print all such pairs as described in the output format in sorted order.

[link]: https://www.hackerearth.com/practice/algorithms/searching/binary-search/practice-problems/algorithm/failed-ranges-8d8e811d/
