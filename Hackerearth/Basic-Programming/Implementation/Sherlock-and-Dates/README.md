# [Sherlock and Dates][link]

Watson was observing in calendar dates of form DD:MM:YYYY. He considers a date to be lucky if

DD + 1 = MM and
MM + 1 = YYYY % 100, where a % b denotes the remainder when a is divided by b.
For example, date 02:03:2004 is lucky because 02 + 1 = 03 and 03 + 1 = 2004 % 100.

Now comes Sherlock and Watson gives him two dates, say D1 and D2, and asks him how many lucky dates lie between D1 and D2(both inclusive).

## Input format

- First line contains T, the number of test cases.
- Each test case consists of two valid dates D1 and D2(in form DD:MM:YYYY) separated by a space. D2 occurs on or after D1.

## Output format

For each test case, print the required answer in one line.

[link]: https://www.hackerearth.com/practice/basic-programming/implementation/basics-of-implementation/practice-problems/algorithm/sherlock-and-dates/
