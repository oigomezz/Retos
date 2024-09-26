# Find the String

You are given a matrix of characters. The matrix has N rows and M columns. Given a string s, you have to tell if it is possible to generate that string from given matrix.
Rules for generating string from matrix are:

1. You have to pick first character of string from row 1, second character from row 2 and so on. The (N + 1)th character of string is to be picked from row 1, that is, you can traverse the rows in a cyclic manner (row 1 comes after row N).
2. If an occurrence of a character is picked from a row, you cannot pick the same occurrence again from that row.

You have to print Yes if given string can be generated from matrix using the given rules, else print No.

## Input format

- First line consists of T, denoting the number of test cases.
- Each test case consists of:
  - First line consists of two integers N and M, denoting the matrix dimensions.
  - Following N lines consist of M characters each.
  - Last line consists of a string s.

## Output format

For each test case, print "Yes" if string can be generated else print "No". Answer for each test case should come in a new line.
