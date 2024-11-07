# Mancunian and Twin Permutations

You are given two arrays A and B of the same length N. Each is a permutation of the integers from 1 to N. You are allowed to perform operations on the first array. Each operation consists of swapping the values at any two indices in the first array.

There will be Q queries. Each query is specified by a quadruplet (L1,R1,L2,R2) which asks for the minimum number of swaps you need to perform in the first array so that the subarray [L1,R1] in the first array is a permutation of the subarray [L2,R2] in the second array.

## Input format

- The first line contains a single integer N denoting the number of elements in the arrays A and B.
- The second line contains N integers denoting the elements of the array A.
- The third line contains N integers denoting the elements of the array B.
- The fourth line contains a single integer Q denoting the number of queries.
- Each of the next Q lines contains the quadruplet L1 R1 L2 R2 for the i-th query.

## Output format

For each query, output the answer in a new line.
