# [An interesting game][link]

You are given two arrays a1,a2,...,an and b1,b2,...,bn where n is an even number.

Alice and Bob are playing a game on these arrays. In each turn, Alice selects two unused numbers before numbers i and j such that 1 <= i,j <= n and i != j. Bob selects one of them and this number is denoted as x and adds bx to his score. Alice takes the remaining one, that is denoted as y, and adds ay to his scores.

Alice and Bob want to maximize their scores simultaneously. Your task is to determine the difference between their scores after the game. Totally, they have n/2 turns.

In other words, your task is to find the difference between Alice's and Bob's scores after all turns if both sides move optimally.

## Input format

- The first line contains one integer t denoting the number of test cases.
- The first line of each test case contains one integer n denoting the length of the array. It is guaranteed that n is even.
- The second line of each test case contains n distinct integers a1,a2,...,an denoting the elements of array a.
- The third line of each test case contains n distinct integers b1,b2,...,bn denoting the elements of the array b.

## Output format

For each test case, print a single integer denoting the difference between Alice's and Bob's scores after the game if both players move optimally.

[link]: https://www.hackerearth.com/practice/algorithms/greedy/basics-of-greedy-algorithms/practice-problems/algorithm/interesting-game-4-b6515135/
