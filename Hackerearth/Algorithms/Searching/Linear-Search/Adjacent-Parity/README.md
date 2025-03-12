# [Adjacent Parity][link]

You are given an array A containing N integers. Find if it is possible to rearrange the elements of the array such that the parity of the sum of each pair of adjacent elements is equal (formally, parity(A[i] + A[i+1]) = parity(A[j] + A[j+1]) for each 1 <= i < j <= N -1 ).

Here, parity refers to the remainder obtained when a number is divided by 2 (i.e. parity(x) = x mod 2).

## Input format

- The first line contains T denoting the number of test cases. The description of T test cases is as follows:
- For each test case:
  - The first line contains N denoting the size of array A.
  - The second line contains N space-separated integers A[1], A[2], ....., A[N] - denoting the elements of A.

## Output format

For each test case, print "YES"(without quotes) if it is possible to reorder the array elements to satisfy the given condition and "NO"(without quotes) otherwise.

[link]: https://www.hackerearth.com/practice/algorithms/searching/linear-search/practice-problems/algorithm/adjacent-parity-10c93d7a/
