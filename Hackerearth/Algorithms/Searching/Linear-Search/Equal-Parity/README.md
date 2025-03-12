# [Equal Parity][link]

You are given an array A containing 2N integers. You want to obtain exactly N even integers in the array. Is it possible to achieve the goal using the following operation any number of times(possibly zero) ?

- Choose two distinct indices i,j (1 <= i,j <= N, i != j) such that A[i] is an even integer, then set A[i] = A[i] / 2, A[j] = A[j] \* 2

## Input format

- The first line contains T denoting the number of test cases. The description of T test cases is as follows:
- For each test case:
  - The first line contains an integer N where 2N denotes size of array A.
  - The second line contains 2N space-separated integers A[1], A[2], ..., A[2N]- denoting the elements of A.

## Output format

For each test case, print "YES" (without quotes) if it is possible to achieve the goal and "NO" (without quotes) otherwise.

[link]: https://www.hackerearth.com/practice/algorithms/searching/linear-search/practice-problems/algorithm/equal-parity-ccc0c1dd/
