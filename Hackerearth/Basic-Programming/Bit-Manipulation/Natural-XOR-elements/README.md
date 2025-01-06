# [Natural XOR elements][link]

You are given an integer N. To solve the problem, you must find the minimum number of elements that must be removed from the set S = {1,2,...,N} such that the bitwise XOR of the remaining elements is 0.

## Input format

- The first line contains an integer t representing the number of test cases.
- The first and only line of each test case contains an integer N representing the number presented to you.

## Output format

For each test case, print a single line.

The first integer k represents the minimum number of elements and you must remove from S. Then, k space-separated integers a1,a2,...,ak follows representing the elements that you have to remove from S.

If there are multiple possible solutions, output the lexicographically largest one. A solution a1,a2,...,ak is lexicographically larger than solution b1,b1,...,bn, if ai > bi where i is the smallest index where ai != bi.

[link]: https://www.hackerearth.com/practice/basic-programming/bit-manipulation/basics-of-bit-manipulation/practice-problems/algorithm/natural-xor-25d22168/
