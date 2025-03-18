# [Minimum radius][link]

You are given two arrays X and Y of N elements denoting N points on the 2D plane. You are given another array A of N elements denoting the values associated with each point.

You have to find the minimum integer value radius r of a circle with the center (0,0) such that the sum of all the values of nodes within the circle or on the circle is greater than or equal to an integer p.

If any such r does not exist, print -1.

**Notes:** Assume 1-based indexing. For a circle with radius 0, the center is said to lie inside that circle.

## Input format

- The first line contains an integer T denoting the number of test cases.
- For each test case:
  - The first line contains two space-separated integers N, p.
  - The second line contains N space-separated integers denoting the array X.
  - The third line contains N space-separated integers denoting the array Y.
  - The fourth line contains N space-separated integers denoting the array A.

## Output format

For each test case in a new line, print the minimum integer value radius r of the required circle.

[link]: https://www.hackerearth.com/practice/algorithms/searching/binary-search/practice-problems/algorithm/minimum-radius-2-29df5cb3/
