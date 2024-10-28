# Flipping Brackets

A regular bracket sequence is a sequence of '(' and ')' characters defined as follows:

- The empty string (without any characters) is a regular bracket sequence.
- If A is a regular bracket sequence, then (A) is also considered a regular sequence.
- If A and B are regular bracket sequences, then AB is also considered as a regular bracket sequence.

For a string S that consists of only '(' and ')' characters, consider a sequence of M operations that are of one of the following types:

- C i: If the character S[i] is an opening bracket '(' , then it is replaced by a closing bracket ')'. Similarly, the ')' character is replaced by the '(' character.
- Q i: Determine the maximum length K of the regular bracket sequence starting at index i of the string. Formally, the string S[i] S[i+1]...S[i+K-1] should be a regular bracket sequence, where K is maximized. If there is no regular bracket sequence starting at index i, then print 0.

## Input format

- First line: String S
- Next line: M representing the number of queries
- Next M lines: A query of the following types:
  - C i: Replace the character at index i with the opposite bracket.
  - Q i: Find the maximum length of a regular bracket sequence starting at index i.

## Output format

For the query of the type Q, print the length of the longest regular bracket sequence starting at index i.
