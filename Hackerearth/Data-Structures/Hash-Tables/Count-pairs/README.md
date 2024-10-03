# Count pairs

You are given an array A consisting of N non-negative integers. You are also given 2 integers p (a prime number) and k. You are required to count number of pairs (i,j) where, 1 <= i < j <= N and satisying:

    (A²i + A²j + Ai \* Aj) mod p = k

where a mod p = b means that b is the remainder when a is divided by p. In particular, 0 <= b < p.

## Input format

- The first line contains a single integer T denoting the number of test cases.
- For each test case:
  - The first line contains three space-separated integers N, k, and p denoting the length of the array, the required remainder/modulo, and the prime number respectively.
  - The second line contains N space-separated integers denoting the integer array A.

## Output format

For each test case, print the number of pairs satisfying the equation in a separate line.
