# [Shift and Replace][link]

You are given an array A of N integers. The following two operations can be performed on the provided array and each operation costs 1 unit.

1. Change the value of any element (only one element).
2. Perform cyclic shifts to the array to left by 1 unit. For example, if an array is 2 3 1 4 and 1 left shift is performed, then the array becomes 3 1 4 2.

You are given Q queries of type X B. For each query, you must replace the value of the element at index X with B. Find the minimum cost required to convert array A to the identity array.

An identity array of size N is 1,2,3,..., N-1, N.

**Note:** For each query, you cannot perform actual operations on array A apart from setting A[X] to B.

## Input format

- The first line contains N denoting the number of elements in the array.
- The second line contains N space-separated integers.
- The next line contains Q denoting the number of queries.
- The next Q lines contain queries of type X B.

## Output format

Print Q integers in a separate line representing the answer to Q queries.

[link]: https://www.hackerearth.com/practice/algorithms/dynamic-programming/introduction-to-dynamic-programming-1/practice-problems/algorithm/shift-and-replace-d96fc236/
