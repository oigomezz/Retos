# [String Queries][link]

Given a 1-indexed String S of length N, consisting of lowercase English alphabets, you need to answer queries based on the properties of this string.

You shall be given Q queries to answer. In each query you shall be given 2 integers L and R. Now , you need to report the minimum number of String elements you need to delete in the substring of String S ranging from L to R inclusive, so that each distinct character occurring in the range occurs equal number of times.

For example, consider the String "abcdab". Here, the characters occurring in this String are a. b, c and d. On deleting one occurrence of a as well as b one of the possible Strings is abcd. Each character occuring in the range now occurs equal number of times. So, the minimum number of deletions is two.

Note that we need to equalize the count of only characters that occur in the range, and not of characters that do not. It is allowed to delete all occurences of a character, so that it no longer occurs in the range at all

Can you do it ?

## Input format

- The first line contains 2 space separated integers N and Q.
- The next line contains the String S.
- Each of the next Q lines contains 2 space separated integers L and R, denoting the parameters of the i-th query.

## Output format

Print the answer to each query on a new line.

[link]: https://www.hackerearth.com/practice/algorithms/string-algorithm/basics-of-string-manipulation/practice-problems/algorithm/string-queries-1/
