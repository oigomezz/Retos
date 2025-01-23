# [Beautiful Substrings][link]

A string S is a substring of string T if it is possible to choose several consecutive letters in T in such a way that they form S.

A string is called beautiful if it can be split into substrings, such that for every substring the first and last characters are 'b' and all other characters are 'a'.

For instance, strings "bab", "bb", "baab", "baaabbabbbbaab" are beautiful strings, but strings "baa", "bbb", "b", "baabab" are not beautiful.

Given N strings consisting of letters 'a' and 'b'.

Emil decided to write down all possible prefixes of the given strings (he will write each prefix only once which mean he'll write distinct prefix only). After that he will count the number of beautiful substrings in every prefix and sum them up (a beautiful substring will be counted as many times as it is contained in each prefix).

Output the sum Emil will get.

As the answer can be pretty large output it modulo 10⁹ + 7.

## Input format

- The first line contains N denoting the number of strings.
- The ith of the next N lines contains the string Si.

## Output format

The sum Emil gets modulo 10⁹ + 7.

[link]: https://www.hackerearth.com/practice/data-structures/advanced-data-structures/trie-keyword-tree/practice-problems/algorithm/beautiful-substrings-008a53a4/
