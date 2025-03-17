# [Horse Race][link]

You own a race course where N different races are played on a day and the performance of the winner is recorded in an array A. The winner of the i-th race is Ai horse. Being the owner, you are only interested in the performance of all the horses numbered from 1 to M. Let's denote the number of races won by the horses numbered from 1 to M by array B, where Bj denotes the number of races won by horse j (1 <= j <= M).

Let K denote the minimum value among all the elements of the array B. You are allowed to perform the following operations at most X times (maybe 0).

- Choose index i (1 <= i <= N) change the value Ai of i.e. the winner of race i.

You are given an integer X denoting the maximum number of operations you can perform. Find the maximum possible value of K after performing atmost X operations.

**Note:** There can be horses greater than M (M<= N) participating in the race, but we only care about the horses numbered from 1 to M.

## Input format

- The first line contains an integer T, which denotes the number of test cases.
- The first line of each test case contains three integers, denoting the value of N, M, and X respectively.
- The second line of each test case contains N space-separated integers, denoting the elements of array A.

## Output format

For each test case, print the maximum possible value of K.

[link]: https://www.hackerearth.com/practice/algorithms/searching/binary-search/practice-problems/algorithm/horse-race-122f4ccc/
