# [Substring Queries][link]

A substring of a string S is another string S^d that occurs "in" S. For example, "thebestof" is a substring of "Itwasthebestoftimes". This is not to be confused with subsequence, which is a generalization of substring. For example, "Itwastimes" is a subsequence of "Itwasthebestoftimes", but not a substring.

You are given a string S and Q queries on it. In each query, you will be given two integers L and R. For each query, you need to find the lexicographic rank of the substring between indices L and R among all the substrings of this string.

String x is lexicographically less than string y, if either x is a prefix of y (and x != y), or there exists such i (1 <= i <= min(|x|, |y|)), that xi < yi, and for any j (1 <= j < i). Here a denotes the length of the string a.

There might be some queried substrings which occur more than once in the given string. You should consider the queried substring a as the lexicographically largest among all substrings of S which are equal to a.

## Input format

- First line of input contains the string S.
- Next line contains an integer Q, denoting the number of queries.
- Each of the next Q lines contain 2 integers L and R, the end points of the substring in the corresponding query.

## Output format

For each query, output the answer in a new line.

[link]: https://www.hackerearth.com/practice/algorithms/string-algorithm/string-searching/practice-problems/algorithm/septembereasy-substring-queries-f75c15fc/
