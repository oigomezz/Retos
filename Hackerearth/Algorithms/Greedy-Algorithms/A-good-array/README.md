# [A good array][link]

You are given an array A which consists of N elements. Each element of array is either zero or one. Your task is to convert the given array into a good array with a minimum cost.

Good array: In a good array, select any subarray of even length M and the sum of elements in the subarray will be M/2.

In order to transform an array to good array, you can perform the following two operations as many times as you want:

1. Choose any index i (1 <= i <= N) and if it is currently 0, then convert it to 1 for X coins.
2. Choose any index i (1 <= i <= N) and if it is currently 1, then convert it to 0 for Y coins.

Your task is to minimize the cost of transformation of an array to good array.

## Input format

- The first line contains T, denoting the number of test cases.
- The first line of each test case contains three space-separated integers N, X, and Y.
- The second line of each test case consists of N space-separated integers of array A.

## Output format

For each test case, print one line denoting the minimum cost to transform array A into a good array.

[link]: https://www.hackerearth.com/practice/algorithms/greedy/basics-of-greedy-algorithms/practice-problems/algorithm/savage-array-94706055/
