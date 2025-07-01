# [Prefix and substring queries][link]

You are given Q queries and a string S of length N.

The queries are of the following three types:

- 1 c: Append character c to the end of the string S.
- 2 x y: Consider the suffixes of equal length ending at x and y, that is, consider the substrings S[a,x], S[b,y], and x - a + 1 = y - b + 1 = p. Determine the maximum value of p such that S[a,x] = S[b,y] = S[1,p]. Also, determine the longest prefix S[1,p] such that the suffixes of length p ending at x and y match.
- 3 p l r: Consider the prefix of the string S[1,p]. Consider all substrings S[x,y] such that L <= x <= y <= R . Then, count the number of substrings S[x,y] that match with S[1,p]. In other words, S[1,p] = S[x,y].

## Input format

- First line: Two space-separated integers N and Q.
- Second line: Single string S of length N.
- Next Q lines: Query of any of the three types provided.

## Output format

Print the answer for each query of type 2 and 3.

[link]: https://www.hackerearth.com/practice/algorithms/string-algorithm/string-searching/practice-problems/algorithm/prefix-and-substring-queries-87616b64/
