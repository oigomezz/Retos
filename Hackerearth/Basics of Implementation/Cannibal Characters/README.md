# Cannibal Characters

You are given an integer n and a string s of size n composed of lower case english letters.

- In one operation, you have to choose any character in the string s, then delete the first character to the left of the chosen character that is equal to the chosen character (if there exists) and delete the first character to the right of the chosen character that is equal to the chosen character (if there exists).

- Note that in one operation, the length of the string s is reduced by a maximum of two characters

You want to minimize the length of the string s.

## Input format

The first line contains a single integer T, which denotes the number of test cases. T also specifies the number of times you have to run the Minimum_Operations function on a different set of inputs.

For each test case:

- First line contains an integer n.
- Second line contains a string s.

## Output format

For each test case in a new line, print the minimum number of operations required to minimize the length of string s.
