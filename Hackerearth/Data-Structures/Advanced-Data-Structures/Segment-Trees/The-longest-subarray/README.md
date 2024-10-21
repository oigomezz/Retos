# The longest subarray

You are given an array of N positive integers and Q queries. In each query, you are given two integers L and R.

For each query, find the length of the longest subarray such that the bitwise AND of the subarray is 2^k where L <= k <= R and if no subarray exists, then the answer will be 0.

## Input format

- The first line contains T denoting the number of test cases. The description of each test case is as follows.
  - The first line contains an integer N denoting the number of array elements.
  - The next line contains N space-separated integers.
  - The next line contains an integer Q denoting the number of queries that are required to be performed.
  - Each of the next Q lines contains two integers L and R.

## Output format

For each test case, Q lines must be printed and the ith line should contain the output for the ith query.
