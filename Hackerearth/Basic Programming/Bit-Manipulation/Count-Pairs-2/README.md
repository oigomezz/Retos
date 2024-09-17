# Count pairs

You are given the following:

- An integer N
- An integer X
- An integer Y
- An array A of N elements
- An array B of N elements

Find the number of pairs of (i,j) such that:

- (A[i] ^ B[j])&X = (A[i] ^ B[j])&Y, where ^ represents bitwise XOR operator and & represents bitwise AND operator.
- 1 <= i,j <= N

## Input format

- The first line contains a single integer T that denotes the number of test cases.
- For each test case:
  - The first line contains an integer N.
  - The second line contains an integer X.
  - The third line contains an integer Y.
  - The next line contains N space-separated integers denoting array A.
  - The next line contains N space-separated integers denoting array B.

## Output format

For each test case, print the number of pairs (i,j) that satisfy the conditions in a new line.
