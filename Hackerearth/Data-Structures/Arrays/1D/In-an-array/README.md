# [In an array][link]

You are given an array A of size N, where the ith integer of the array is A[i] and its value ranges between 1 and 1000 inclusive. You are required to complete the following task:

Assume that you are provided with 3 additional numbers K, X, and Y. Your task is to report the number of unordered pairs of elements (i,j) from this array, such that (1 <= i < j <= N), (A[i] + A[j]) % K = X, and (A[i] x A[j]) % K = Y.

## Input format

- First line: Four space-separated integers N, K, X, and Y
- Next line: N space-separated integers where the ith integer denotes A[i].

## Output format

Print the required number of ordered pairs of array elements in a single line. As the answer could be rather large, be careful of integer overflows.

[link]: https://www.hackerearth.com/practice/data-structures/arrays/1-d/practice-problems/algorithm/in-an-array-9fbe4c12/
