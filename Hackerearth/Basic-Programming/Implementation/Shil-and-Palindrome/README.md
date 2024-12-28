# [Shil and Palindrome][link]

Shil is your new boss and he likes palindromes very much. Palindrome is a string that can be read the same way in either direction, from the left to the right and from the right to the left. (ex. madam , aabaa, racecar)

Given a string S , beautiful Palindrome is a lexicographical minimum palindrome that can be formed by rearranging all the characters of string S. In order to please your boss, find a beautiful Palindrome that can be formed with help of string S.

String x is lexicographically less than string y, if either x is a prefix of y (and x ≠ y), or there exists such i (1 ≤ i ≤ min(|x|, |y|)), that xi < yi, and for any j (1 ≤ j < i) xj = yj. Here |a| denotes the length of the string a. The lexicographic comparison of strings is implemented by operator < in modern programming languages​​.

## Input format

Only line of input contains string S. All the letters of this string will be in lower letters('a' - 'z').

## Output format

Output lexicographical minimum Palindrome that can be formed by rearranging all the letters of string S. If no such Palindrome exist for given input, print -1.

[link]: https://www.hackerearth.com/practice/basic-programming/implementation/basics-of-implementation/practice-problems/algorithm/shil-and-palindrome/
