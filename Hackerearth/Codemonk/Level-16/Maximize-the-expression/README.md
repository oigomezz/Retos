# Maximize the expression

You are given three arrays A,B and C. All three arrays consist of N integers.

You can perform the following operation on each index for at most one time:

- Convert(i): Select a positive value D such that C[i] & D = D and update B[i] = B[i] ⊕ D. Here, ⊕ and & denotes the bitwise XOR operation and bitwise AND operation.

You are required to maximize the following expression:

S = Σ A[i] ⊕ B[i]

## Input format

- First line: A single integer N denoting the number of elements of the array.
- Next line: N integers of array A.
- Next line: N integers of array B.
- Next line: N integers of array C.

## Output format

Print a single integer that denotes the maximum value of S.
