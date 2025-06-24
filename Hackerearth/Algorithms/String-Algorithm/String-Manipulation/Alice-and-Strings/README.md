# [Alice and Strings][link]

Two strings A and B comprising of lower case English letters are compatible if they are equal or can be made equal by following this step any number of times:

Select a prefix from the string A (possibly empty), and increase the alphabetical value of all the characters in the prefix by the same valid amount. For example if the string is xyz and we select the prefix xy then we can convert it to yz by increasing the alphabetical value by 1. But if we select the prefix xyz then we cannot increase the alphabetical value.

Your task is to determine if given strings A and B are compatible.

## Input format

- First line: String A.
- Next line: String B

## Output format

For each test case, print YES if string A can be converted to string B, otherwise print NO.

[link]: https://www.hackerearth.com/practice/algorithms/string-algorithm/basics-of-string-manipulation/practice-problems/algorithm/aliceandstrings-9da62aa7/
