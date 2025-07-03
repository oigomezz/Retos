# [Longest Palindrome][link]

Given a string S of N length consisting of lowercase latin characters (a - z). We need to decompose S into K consecutive non empty substrings such that every character is present in only one substring.

Say substrings are S[1], S[2], S[3], .... , S[K]. Choose a array B , which is a permutation of 1 to K i.e. it is of size K and include every element from 1 to K.

Now , form a new string V = S[B[1]] + S[B[2]] + ...... + S[B[k]].

Suppose, X is the length of the longest palindromic substring present in string V.

Aim is to maximize X.

## Input format

- First line contains two space-separated integers : N and K.
- Second line contain a string S, of lowercase latin characters.

## Output format

- In the first K lines, print one integer denoting end index of i-th substring (indexes are 1 based).
- In next line print K space separated integers, denoting array B (permutation of 1 to K)
- End index of substrings should be in increasing order.

[link]: https://www.hackerearth.com/practice/algorithms/string-algorithm/manachars-algorithm/practice-problems/approximate/longest-palindrome-3daadc21/
