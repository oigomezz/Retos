# [Prefix Number <Liv.ai>][link]

Given a very large number N, you need to count the total ways such that if we divide the number into two parts a and b then number a can be obtained by integral division of number b by some power p of 10 and p >= 0.

For example: Let 220 be a number then, if you divide the number into two parts 2 and 20 then, if 20 is divided by 10¹ gives the number 2.

Important Notes:

1. You cannot perform any irregular division of the number i.e the original number should be formed after concatenation of the two parts a and b. Example of irregular division is 289 divided as 29 and 8.
2. Both the numbers a and b should not contain any leading zeros.
3. Integral division of any two numbers a, b is F(a/b) where F is the floor function

## Input format

- A line that contains a very large number N(string of digits 0-9).

## Output format

Total number of ways to divide the string such that it follows the above constraints.

[link]: https://www.hackerearth.com/practice/algorithms/string-algorithm/z-algorithm/practice-problems/algorithm/prefix-number-f5c76976/
