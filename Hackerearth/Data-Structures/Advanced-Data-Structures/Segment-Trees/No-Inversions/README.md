# No-Inversions

You're given a string S of length N consisting of lowercase English letters. You are asked Q queries of the type L R. For each query, you are asked to find the no of good substrings between L to R(inclusive).

A substring will be called good if it has no inversions. If there exists any pair of indices (i,j) in the substring a where, i < j for which aj < ai (according to the alphabetical order of the letters) then this pair is counted as an inversion.

A substring of a string is a continuous segment of letters from the string. For example, "acker" is a substring of "hackerearth" and "ckar" is not. The length of the substring is the number of letters in it.

## Input format

- First line of input contains an integer T (the no of test cases). Each test case consists of the followings:
  - First line contains an integer N (the length of the string).
  - Second line contains a string S consisting of N english lowercase letters.
  - Third line contains an integer Q (the no of queries).
  - Next Q lines contain three space-separated integers L R denoting the query.

## Output format

For each test case, for each ith query, print a single integer denoting the answer to the ith query.
