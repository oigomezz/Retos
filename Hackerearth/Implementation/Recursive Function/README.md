# Recursive Function

Implement the recursive function given by the following rules and print the last 3 digits:

F(x, y) = { y + 1 when x = 0, F(x - 1, 1) when x > 0 and y = 0, F(x - 1, F(x, y - 1)) when x > 0 and y > 0 }

## Input format

A single line containing two integers X,Y

## Output format

The last three digits.
