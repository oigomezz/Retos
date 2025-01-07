# [The minimum cost][link]

You are given a binary array (array consists of 0's and 1's) A that contains N elements. You can perform the following operation as many time as you like:

1. Choose any index 1 <= i <= N and if it is currently 0, then convert it to 1 for C01 coins.
2. Choose any index 1 <= i <= N and if it is currently 1, then convert it to 0 for C10 coins.

Your task is to transform the given array into a special array that for every index 1 <= i < N, Ai ^ Ai+1 = 1.

Here, ^ denotes XOR.

## Input format

- The first line contains T the number of test cases.
- The first line of each test case contains three space-separated integers N, C01 and C10.
- The second line consists of N space-separated integers of array A.

## Output format

For each test case, print one line denoting the minimum cost to transform array A into a special array.

[link]: https://www.hackerearth.com/practice/basic-programming/bit-manipulation/basics-of-bit-manipulation/practice-problems/algorithm/min-cost-2-fe2d3308/
