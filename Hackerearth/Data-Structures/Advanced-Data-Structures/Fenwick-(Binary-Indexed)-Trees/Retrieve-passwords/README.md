# Retrieve passwords

A password is a number that is exactly divisible by 9. It is the largest number that can be formed by rearranging all the available digits in a provided range (L,R) inclusive and adding another number of your own choice to this sequence at any position. The password is missing a digit that must be added. You are also given an encrypted number. You are also provided q queries. The queries could be of two types.

1. Update a digit at a position.
2. Determine the largest number that is divisible by 9 in the provided range with the mentioned conditions. In the provided mentioned number, print its x-th digit.

You must retrieve the password.

## Input format

- First line: A string s.
- Second line: A number q indicating the number of questions that must be asked.
- Third line:
  - For each q:
    - A number t indicating the type of query 1 to update and 2 for the query.
    - For a query of type 1, two numbers follow x and y. Update the value at position x (1-based indexing) to y.
    - For a query of type 2, three numbers follow l, r, x. Determine the x-th digit between l to r inclusive (1-based indexing) for the retrieved password.

## Output format

For each query of type 2, print the x-th digit of the formed password.
