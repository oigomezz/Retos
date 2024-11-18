# One mismatch

Given a string s and a set of n strings Pi.

For each i find the number of occurrences of Pi in s with at most one k-length gap.

The string s occurs in string t at position p with at most one k-length gap if strings s and t[p]t[p+1]...t[p+|s|-1] are equal with at most one k-length gap.

Strings s and r are equal with at most one k-length gap if:

1. |s| = |r|;
2. or all i and j such that s[i] != r[i] and s[j] != r[j], it holds |i-j| < k.

## Input format

- First line of input contains single integer k.
- Second line of input contains string s.
- Third line contains an integer n.
- Then follow n lines. The i-th of them contains string Pi.

## Output format

Print n lines. The i-th of them should contain the number of occurrences Pi in s with at most one k-length gap.
