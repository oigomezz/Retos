# [Lost in strings][link]

You have a list in which you store strings. The list is indexed from 1. Initially, the list contains only one string S.

There are three different types of tasks that you are asked to perform:

- 1 p n c: Create a new string of length p using the n-th string from the list such that all characters from 1 to p-1 in the new string are the same as in the old string and the p-th character is c. Append this string to the end of the list.
- 2 p n: Create a new string of length p using the n-th string from the list such that all the characters from 1 to p in the new string are the same as in the old string. Append this string to the end of the list.
- 3 l r s: Print yes if string s appears as the prefix of any string in the range [l,r] of the list, else print no.

## Input format

- First line: String S represents the only string that is initially in the list.
- Next line: Q represents the number of queries to be performed.
- Next Q lines: Each line describes one of the three types of tasks that can be performed. All the tasks are valid.

## Output format

For every task of type 3, print yes or no.

[link]: https://www.hackerearth.com/practice/algorithms/string-algorithm/string-searching/practice-problems/algorithm/lost-in-strings-11fa4a5d/
