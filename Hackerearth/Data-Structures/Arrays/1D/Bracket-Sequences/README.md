# [Bracket sequences][link]

A bracket sequence is a string that contains only characters '(' and ')'.

A correct bracket sequence is a bracket sequence that can be transformed into a correct arithmetic expression by inserting characters '1' and '+' between the original characters of the sequence. For example, bracket sequences '()()' and '(())' are correct. The resulting expressions of these sequences are: '(1)+(1)' and '((1+1)+1)'. However, '(', ')(', and '(' are incorrect bracket sequences.

You are given a bracket sequence s(s1s2...sn), where si denotes the type of i's bracket (open or close). It is not mandatory that s is necessarily correct. Your task is to determine the number of i's such that sisi+1...sns1s2...si-1 is a correct bracket sequence.

## Input format

The single line contains sequence s.

## Output format

Print the number of shifts denoting the correct bracket sequence.

[link]: https://www.hackerearth.com/practice/data-structures/arrays/1-d/practice-problems/algorithm/bracket-sequence-1-40eab940/
