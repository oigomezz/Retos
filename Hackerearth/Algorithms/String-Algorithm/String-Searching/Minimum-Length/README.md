# [Minimum length][link]

You are given an integer N. We call a string S good if it satisfies the following conditions:

1. S[i] = a or S[i] = b ∀ 1 <= i <= len(S)
2. S[i] <= S[i+1] ∀ 1 <= i <= len(S)-1. Recall that a < b according to the numbering of ASCII table.

Here len(S) denotes the length of string S.

Your task is to find the minimum length of a good string which has atleast N distinct substrings.

Notes

- A substring of a string is a contiguous subsequence of that string. For example, "hacker" is subtring of "hackerearth", but "hackr" is not.
- Two substrings X and Y are different if:
  - They are of different length.
  - If they are of the same length, then there is an index i such that X[i] != Y[i].

## Input format

- The first line contains a single integer T denoting the number of test cases.
- For each test case, the only line of input contains a single integer N.

## Output format

For each test case (in a separate line), output the minimum length of a good string which has at least N distinct substrings.

[link]: https://www.hackerearth.com/practice/algorithms/string-algorithm/string-searching/practice-problems/algorithm/minimum-length-2-d2b8af58/
