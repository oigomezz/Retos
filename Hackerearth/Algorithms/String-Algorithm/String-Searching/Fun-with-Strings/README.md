# [Fun with strings][link]

You are given a string S = S[0]S[1]S[2]...S[n-1] of length n.

Find the sum of length of LCP(Longest Common Prefix) over all the (n²(n+1)²)/4 ordered pairs of its substrings.

Formally, say the substring of S starting at index i and ending at index j is represented by Sij, and let L(A,B) represent the length of LCP of strings A and B.

Then compute the value of : ΣΣΣΣ L(Sij,Skl)

As this value may be very large, print it modulo 10⁹ + 7.

## Input format

- The first line contains T, the number of test cases. It is followed by lines, describing the strings in the testcases 2T.
- Each string is described by two lines:
  - The first line contains n, length of the string S.
  - Second line contains the string S consisting of lowercase english alphabets only.

## Output format

Print T lines containing the sum of lengths of lcp over all ordered pairs of substrings of S modulo 10⁹ + 7 for the T testcases, each on a new line.

[link]: https://www.hackerearth.com/practice/algorithms/string-algorithm/string-searching/practice-problems/algorithm/fun-with-strings-1/
