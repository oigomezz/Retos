# [Non-decreasing arrays][link]

You are given an array A consisting of N positive integers. Your task is to find an array B of length N satisfying the following conditions:

- Bi > 0 for all 1 <= i <= N
- Bi <= Bi+1, for all 1 <= i < N
- Bi is divisible by Ai for all 1 <= i <= N
- Σ Bi is minimum

## Input format

- The first line contains a single integer T denoting the number of test cases.
- The first line of each test case contains a single integer N denoting the length of the array.
- The second line of each test case contains N space-separated integers denoting the integer array .

## Output format

For each test case (in a separate line), print N space-separated integers denoting B1,B2,...,Bn. If there are multiple answers, you can print any of them. It is guaranteed that under the given constraints at least 1 B exists.

[link]: https://www.hackerearth.com/practice/data-structures/arrays/1-d/practice-problems/algorithm/make-it-non-decreasing-7d3391fd/
