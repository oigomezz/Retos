# [Shift String][link]

Given a string, s, of length, n, and a list of m strings, x1,x2,...,xm. All m strings in the list are distinct and have length n i.e ∀i |xi| = n, and none of the given strings is equal to s.

You can perform any number of operations s.

In an operation you are allowed to choose one position in the string, s, and change the character at the position to the next or previous character in the English alphabet cyclically ('a' -> 'b', 'b' -> 'c', 'c' -> 'd', ..., 'z' -> 'a', 'b' -> 'a', ...).

What is the minimum number of operations that you have to perform on, s, so for all the given m strings, s becomes xi at least once after one of the performed operations.

## Input format

- The first line of the input contains an integer, n, denoting the length of the string s.
- The second line of the input contains a string, s, denoting the string which you can perform operations on. Each character in s is a lowercase English alphabet ('a' - 'z').
- The next line of the input contains an integer, m, denoting the number of strings that will be in the list.
- The next m lines distinct strings, xi, denoting a string in the list. Each character in xi is a lowercase english alphabet ('a' - 'z')

## Output format

The output should contain one line denoting the minimum amount of operations that need to be performed on s, to reach each of the m strings at least once.

[link]: https://www.hackerearth.com/practice/algorithms/dynamic-programming/bit-masking/practice-problems/algorithm/shift-string-2-e1383bdd/
