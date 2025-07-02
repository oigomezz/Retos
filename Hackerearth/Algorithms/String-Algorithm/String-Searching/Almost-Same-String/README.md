# [Almost Same String][link]

## Assumption

1. You have to consider the character set of lowercase characters, which is cyclically connected, i.e after a comes b, after b comes c and so on... and after z comes a.
2. The distance between any two characters in the character set is the minimum number of steps you need to convert one character to another.
3. In one step, either you can increase the character by 1 or decrease the character by one.
4. Lets say, if you increase a by 1, it will become b, and if you decrease a by 1, it will become z. Similarly if you increase z by 1, it will become a.

## Problem Statement

You are given two strings A and B of equal length, and an integer K. Both the strings consists of lowercase characters only.

These two strings are said to be almost same strings if we take any two characters say ch1 and ch2 from any of the two strings (either both characters from the same string or from the different strings), then: distance between ch1 and ch2 in the character set <= K.

Your task is to change the strings to almost same strings in minimum number of steps. To recall, in one step you can either increase any character of any string by 1 or decrease it by 1.

## Input format

- First line consists of an integer T denoting number of test cases.
- In each test case:
  - First line consists of string A.
  - Second line consists of string B.
  - Third line consists of an integer K.

## Output format

Print the minimum number of steps required to change the strings to almost same strings. Answer for each test case should come in a new line.

[link]: https://www.hackerearth.com/practice/algorithms/string-algorithm/string-searching/practice-problems/algorithm/forming-almost-similar-string-d551fc3d/
