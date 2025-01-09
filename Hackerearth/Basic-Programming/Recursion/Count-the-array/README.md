# [Count the array][link]

You are given an integer P.

Also, you are given Q queries of the following type:

- N: Determine the count of distinct arrays of size <= N and >= 1 such that:
  - Each array element is a prime number.
  - Product of the value of all the array elements is <= P.
  - Array formed is palindromic.

**Note:**

- Two arrays are said to be distinct if there exists at least one index where the value of element present in both the arrays is different.
- An array is said to be palindromic if it reads same from the left to right and right to left direction.
- Since the count can be very large, print the output in modulo 10⁹ + 7.
- Assume 1 based indexing.

## Input format

- The first line contains an integer P.
- The second line contains an integer Q.
- The next line contains Q space-separated integers that denotes the value of N for each query.

## Output format

Print Q space-separated integers denoting the result for Q queries.

[link]: https://www.hackerearth.com/practice/basic-programming/recursion/recursion-and-backtracking/practice-problems/algorithm/count-array-b31ab1e9/
