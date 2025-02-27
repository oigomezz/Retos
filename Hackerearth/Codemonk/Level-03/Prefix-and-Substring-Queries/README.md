# Prefix and Substring Queries

You are given a string S of length N and Q queries.

The queries are of 3 types:

- 1 c : Append the character c to the end of the string S
- 2 x y : Consider the suffixes of equal length ending at x and y. i.e. consider substrings S[a, x] and S[b, y] and x - a + 1 = y - b + 1 = p. Find the maximum value of p such that S[a, x] = S[b, y] = S[1, p]. More formally, this can be stated as to find the longest prefix S[1, p] such that the suffixes of length p ending at x and y match.
- 3 p l r : Consider the prefix of the string S[1, p]. Now consider all substrings S[x, y] such that L <= x <= y <= R. Count the number of substrings S[x, y] which match with S[1, p].(i.e. S[1, p] = S[x, y]).

## Input format

- First Line : Two space separated integers N and Q .
- Second Line : A single string S of length N.
- Q lines follow with each each line containing a query of any of the 3 above mentioned types.

## Output format

Print the answer for each query of type 2 and 3.
