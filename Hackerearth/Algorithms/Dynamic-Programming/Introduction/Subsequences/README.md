# [Subsequences][link]

Your task is to find a range L to R(inclusive) such that the number of integers in this range that satisfies the following property is equal to K:

- Property: Sum of all the subsequences of digits of that number must be odd

For example, 1257 has 1 + 2 + 5 + 7 + 12 + 15 + 17 + 25 + 27 + 57 + 125 + 127 + 257 + 1257 = 1934 as the sum of all subsequences.

Find such a range that is of the minimum length. If more than one such range exists, print the range with the smallest value of L.

## Input format

- The first line contains an integer Q denoting the number of queries.
- The next Q lines contain an integer K.

## Output format

For each query, print two integers denoting L,R in a separate line. If no such range exists, then print -1.

[link]: https://www.hackerearth.com/practice/algorithms/dynamic-programming/introduction-to-dynamic-programming-1/practice-problems/algorithm/subsequence-again-19245c50/
