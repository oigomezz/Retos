# [Alice and messages][link]

Alice has K strings, each consisting only of lowercase letters that she wanted to send to her friend. To avoid anyone else from being able to see them, she encodes every string using the following rule:

- For every letter x, if it is the i-th letter of the alphabet starting from the left, replace it with the i-th letter starting from the right. For example, the string 'abcd' would be encoded to 'zyxw'.

However, due to a bug, a certain number of messages (possibly none) were not encoded. You are given a list of N distinct strings containing all the original messages as well as the encoded messages. You do not know how many messages Alice originally started with.

**Task:** Determine the minimum possible value of K denoting the the number of messages Alice initially started with.

## Input format

- The first line contains an integer N, denoting the number of strings present in the final array.
- The second line contains N space-separated strings consisting of lowercase letters only.

## Output format

Print a single line containing a single integer representing the minimum possible number of strings Alice could have had initially.

[link]: https://www.hackerearth.com/practice/algorithms/string-algorithm/basics-of-string-manipulation/practice-problems/algorithm/testing-40-d469eb00/
