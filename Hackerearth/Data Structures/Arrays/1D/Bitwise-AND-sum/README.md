# Bitwise AND sum

You are given an array A consisting of N positive integers. Here, f(i,j) is defined as the bitwise AND of all elements of the array A after replacing all elements of A in range [i,j] (both inclusive) with (2²⁵ - 1).

Note that after calculating the value f(i,j) for some (i,j), the array is restored back to its original form. Therefore, calculating f(i,j) for each (i,j) pair is independent.

## Input format

- The first line contains a single integer T denoting number of test cases.
- For each test case:
  - The first line contains a single integer N denoting the length of the array.
  - The second line contains N space-separated integers denoting the integer array A.

## Output format

For each test case, print the required sum in a separate line.
