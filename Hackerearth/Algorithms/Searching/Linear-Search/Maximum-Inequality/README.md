# [Maximum Inequality][link]

A function on a binary string T of length M is defined as follows:

    F(T) = number of indices i (1 <= i < M) such that T[i] != T[i+1]

You are given a binary string S of length N. You have to divide string S into two subsequences S1,S2 such that:

- Each character of string S belongs to one of S1 and S2.
- The characters of S1 and S2 .must occur in the order they appear in S.

Find the maximum possible value of F(S1) + F(S2)

**NOTE:** A binary string is a string that consists of characters `0` and `1`. One of the strings S1,S2 can be empty.

## Input format

- The first line contains T denoting the number of test cases. The description of T test cases is as follows:
- For each test case:
  - The first line contains N denoting the size of string S.
  - The second line contains the string S.

## Output format

For each test case, print the maximum possible value of F(S1) + F(S2) in a separate line.

[link]: https://www.hackerearth.com/practice/algorithms/searching/linear-search/practice-problems/algorithm/maximum-inequality-b002b193/
