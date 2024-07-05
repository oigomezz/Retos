# The Largest Subnumber

You are given a string S of length N which consists of digits from 0 to 9. You need to find an index i such that the sub number formed by S[i..N]
is divisible by K and the xor of all the digits in the sub number formed by S[1..(i-1)] is maximum. If there are multiple i's such that S[i..N]
is divisible by K and for all such values of i, S[1..(i-1)] is maximum, then print the largest sub number.

The sub number S[i..N] should not contain any leading zeros and the value of S[i..N] should not be 0. Both the sub numbers S[1..(i-1)] and S[i..N] should contain at least one digit. If no answer exists, print -1.

## Input format

- First line: T denoting the number of test cases.
- For each test case:
  - First line: Two space-separated integers N and K
  - Second line: String S

## Output format

If an answer exists, then print the sub number S[i..N]. Otherwise, print -1.

For each test case, print the answer in a new line.
