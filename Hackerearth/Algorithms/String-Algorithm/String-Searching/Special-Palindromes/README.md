# [Special palindromes][link]

You are given a string S consisting of lowercase Latin letters. You have to select a substring say S2 and prefix say S2 from S of equal length.

Your task is to concatenate them such that one of them is appended in reverse order and form a string P that is either:

- P = S1 + reverse(S2) or S2 + reverse(S1), here + operator denotes concatenation.

If string P is a palindrome, then it is said to be a special palindrome.

Find the number of strings S1 such that there exists a prefix S2 using which a special palindrome string can be formed.

## Input format

- The first line contains an integer T denoting the number of test cases.
- The first line of each test case contains an integer N denoting the length of string S.
- The second line of each test case contains string S.

## Output format

For each test case, print the number of distinct special palindrome strings possible in a new line.

[link]: https://www.hackerearth.com/practice/algorithms/string-algorithm/string-searching/practice-problems/algorithm/special-palindrome-11f52457/
