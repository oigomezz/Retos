# [A strongest string][link]

You are given a string S that consists of N lowercase letters of the Latin alphabet.

In one step, you can remove any letter in the string. You are required to determine the maximum lexicographic sentence of words you can leave so that all letters are different.

The lexicographical order on the set of all these finite words orders the words in the following manner:

1. You are given two different words of the same length, for example, a = a1,a2,...,ak and b = b1,b2,...,bk. The order of these two words depends on the alphabetic order of the symbols on the first place where the two words are different (counting from the beginning of the words), a < b if and only if ai < bi in the underlying order of alphabet A.
2. If two words have different lengths, then the usual lexicographical order pads the shorter one with 'blanks' (a special symbol that is treated as smaller than every element of A) until the words are made of the same length. Now, the words are compared as in the previous case.

## Input format

- The first line contains T denoting the number of test cases.
- The first line of each test case contains N denoting the length of string S.
- The second line of each test case contains string S.

## Output format

For each test case, print the answer.

[link]: https://www.hackerearth.com/practice/algorithms/string-algorithm/string-searching/practice-problems/algorithm/strongest-string-4103a929/
