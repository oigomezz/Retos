# Maximizing Expressions

You are given three arrays A, B, and C. All the three arrays consist of N integers.

You must perform the following operation on each index exactly one time:

Convert(i): Select a positive value D such that Ci & D = D, and update Bi = Bi ⊕ D.

Here, ⊕ and & denotes the bitwise XOR operation and bitwise AND operation.

## Input format

- First line: A single integer N denoting the number of elements of the array.
- Next line: N integers of array A.
- Next line: N integers of array B.
- Next line: N integers of array C.

## Output format

Print a single integer that denotes the maximum value of S.
