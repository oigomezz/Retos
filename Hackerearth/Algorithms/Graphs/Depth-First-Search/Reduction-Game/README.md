# [Reduction Game][link]

You are given an array A consisting of N distinct integers. If the size of the array is greater than one, then you can perform the following operations any number of times:

- Select two integers Ai and Aj such that CountOnes(Ai ⊕ Aj) = 1 and delete either Ai or Aj from the array. This operation costs C1.

- Select two integers Ai and Aj such that CountOnes(Ai ⊕ Aj) > 1 and delete either Ai or Aj from the array. This operation costs C2.

Here, CountOnes(X) returns the number of 1s available in the binary representation of integer X. Determine the minimum cost to reduce the size of the array to 1.

## Input format

- First line: T denoting the number of test cases.
- For each test case:
  - First line: N.
  - Second line: Two space-separated integers C1 and C2.
  - Third line: N space-separated integers denoting the array A.

## Output format

For each test case, print a single integer in a separate line as described in the problem statement.

[link]: https://www.hackerearth.com/practice/algorithms/graphs/depth-first-search/practice-problems/algorithm/reduction-game-56c3c092/
