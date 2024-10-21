# Optimal Moves

There are points placed on a number line at position 1,2,...,N.

Initially, you are at point 1 and want to find the minimum cost to reach each of the N points. You are allowed to move only towards +ve x-axis.

Let's say, after certain moves, you are at point i (i < N) and want to make the next move. You are allowed to make a move only of the following two types:

- type 1: by moving to the next point i.e point i+1 which cost Ai.
- type 2: by moving to point j if and only if i E [Lj,Rj] which cost Bi.

Find the minimum cost to reach each of the N points.

## Input format

- The first line contains T denoting the number of test cases. The description of T test cases is as follows:
- Each test case consists of multiple lines of input.
  - The first line of each test case contains one integer N — the number of points.
  - The second line consists of N-1 space-separated integers denoting the elements of array A.
  - The third line consists of N space-separated integers denoting the elements of array B.
  - The fourth line consists of N space-separated integers denoting the elements of array L.
  - The fifth line consists of N space-separated integers denoting the elements of array R.

## Output format

For each test case, output on a new line, the minimum cost to reach each of the N points.
