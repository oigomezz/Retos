# [Empty Game][link]

You are given an array A of length N. In one move, select an integer X and do one of the following operations:

1. Choose one index i (1 <= i <= N) such that |A[i] - X| <= 1 and remove A[i].
2. Choose two indices i and j (1 <= i,j <= N, i != j) such that |A[i] - X| <= 1 and |A[j] - X| <= 1 and remove A[i] and A[j] from the array.

Find the minimum number of moves required to make the array empty.

## Input format

- The first line contains an integer T denoting the number of test cases.
- The first line of each test case contains an integer N denoting the length of the array.
- The second line of each test case contains N space-separated elements of the array A.

## Output format

For each test case, print the minimum moves needed to make the array empty.

[link]: https://www.hackerearth.com/practice/algorithms/greedy/basics-of-greedy-algorithms/practice-problems/algorithm/empty-game-d49730e1/
