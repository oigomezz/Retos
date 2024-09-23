# Special series

Consider a series F that is defined as follows:

- F(1) = 1
- F(2) = 1
- F(3) = 2
- For n >= 3, F(n)² - F(n+1)xF(n-1) = (-1)^n

Given two integers n and m. We need to make the nth term and mth term of the series co-prime. Find the largest positive number by which we must divide the nth term and mth term of the series such both terms become co-prime. Since, this number can be very large, print it modulo 10⁹ + 7.

**Note:** Two numbers are said to be co-prime if there does not exist any number greater than 1, which divides both the numbers.

## Input format

- The first line contains an integer T denoting the number of test cases.
- For each test case:
  - The first line contains a string denoting the integer n.
  - The second line contains an integer m.

## Output format

For each test case in a new line, find the required largest positive number modulo 10⁹ + 7.
