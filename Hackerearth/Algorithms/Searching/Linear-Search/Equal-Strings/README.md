# [Equal Strings][link]

You are given two binary strings (where each character is either 0 or 1) S and T, each of length N and an integer X. You can apply the following two types of operations to the string S:

- Choose two distinct indices i,j and flip both S[i], S[j]. The cost of this operation is X.
- Choose an index i (1 <= i < N) and flip both S[i], S[i+1]. The cost of this operation is 1.

You may perform this operation any number of times. Find the minimum cost to make the strings S and T equal or report that it is impossible.

## Input format

- The first line of input contains an integer T denoting the number of test cases. The description of each test case is as follows:
- The first line of each test case contains two integers N denoting the length of the string S and T and integer X.
- The second line of each test case contains the string S.
- The third line of each test case contains the string T.

## Output format

For each test case, print -1 if it is impossible to equalize the strings. Otherwise print the minimum cost to make the strings S and T equal in a separate line.

[link]: https://www.hackerearth.com/practice/algorithms/searching/linear-search/practice-problems/algorithm/equal-strings-79789662-4dbd707c/
