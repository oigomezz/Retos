# [Arrange Brackets][link]

Given a string S of length N consisting of two characters (open bracket) "(" and (close bracket) ")". We need to decompose S into K consecutive non-empty substrings such that every character is present in only one substring.

Say substrings are S[1],S[2], ..., S[K]. Choose an array B and an array C, which is a permutation of 1 to K i.e. it is of size K and include every element from 1 to K. Also please note there should be atleast K/2 (rounded down) indices where B[i] != C[i].

Now, form a new string V = S[B[1]] + S[B[2]] + ... + S[B[K]] and V' = S[C[1]] + S[C[2]] + ... + S[C[K]]. A matching pair of brackets is not balanced if the set of brackets it encloses are not matched.

A string is said to be balanced if

- Empty string is a balanced string.
- If s is a balanced string, then (s) is also a balanced string.
- If s and t are balanced strings, then st (concatenation of s and t) is also a balanced string.

Suppose the number of balanced substrings in V is X and V' is X' (of length greater than 1).

Aim is to maximize Z = X + X'.

## Input format

- First line contains two space-separated integers N K.
- Next line contains a string S of length N.

## Output format

- In the first line print K integers, which denotes the end index of i-th substring (indexes are 1 based).
- In next line print K space separated integers, denoting array B (permutation of 1 to K).
- In next line print K space separated integers, denoting array C (permutation of 1 to K).

**Note:** End index of substrings should be in increasing order.

[link]: https://www.hackerearth.com/practice/algorithms/string-algorithm/string-searching/practice-problems/approximate/balance-brackets-again-6bd70495/
