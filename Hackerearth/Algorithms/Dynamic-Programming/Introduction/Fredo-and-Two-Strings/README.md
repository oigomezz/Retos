# [Fredo and Two Strings][link]

Fredo has got two strings s and t. Playing around with them, he came up with the following question:

Will string t be a subsequence of string s if he removes substring [S[i], S[i+1], ..., S[j-1], S[j]] from string s ?

Given q queries, each query consists of indices i and j, you have to answer "Yes" if string t is a subsequence of remaining string s else answer "No".

**Note:** Each query is independent of each other.

## Input format

- First line of input consists of string s.
- Next line consists of string t.
- Next line consists of two integers q 2 (q denoting number of queries and second integer always having value 2).
- Each of following q lines consists of two integers i and j, denoting starting and ending indices of substring to be deleted from string s.

## Output format

For each query , output "Yes" if t is a subsequence of remaining string s, else output "No". Answer for each query should come in a new line.

[link]: https://www.hackerearth.com/practice/algorithms/dynamic-programming/introduction-to-dynamic-programming-1/practice-problems/algorithm/fredo-and-two-strings-247e6c24/
