# [Special Substring][link]

Given a string S of N length consisting of binary digits (0 and 1). We need to decompose S into K consecutive non empty substrings such that every digit is present in only one substring.

Say substrings are S[1], S[2], S[3], .... , S[K]. Choose a array B , which is a permutation of 1 to K i.e. it is of size K and include every element from 1 to K.

Now , form a new string V = S[B[1]] + S[B[2]] + ...... + S[B[k]].

For string V, a substring is said to be special if it includes equal number of ups and downs. Substrings having length 1 will not be special.

Aim is to maximize X, which is the count of special substrings in V.

## Input format

- First line contains two space-separated integers : N and K
- Second line contain a string S, of binary digits (0 and 1).

## Output format

- In the first K lines, print one integer denoting end index of i-th substring (indexes are 1 based).
- In next line print K space separated integers, denoting array B (permutation of 1 to K).
- End index of substrings should be in increasing order.

[link]: https://www.hackerearth.com/practice/algorithms/greedy/basics-of-greedy-algorithms/practice-problems/approximate/as-23d8d46d/
