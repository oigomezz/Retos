# [Alternative moves][link]

You are given three integers N, A, and B. You have another integer X = 0. You can apply the following move (1-indexed) any number of times:

- During the odd-numbered moves(1, 3, 5,....), you have to set X = X + A.
- During the even-numbered moves(2, 4, 6,....), you have to set X = X - B.

Find the minimum number of moves required so that the value of X becomes greater than or equal to N or print -1 if it is impossible to do so.

## Input format

- The first line contains T denoting the number of test cases. The description of T test cases is as follows:
- Each test case consists of a single line containing three integers N, A, and B.

## Output format

For each test case, print the minimum number of moves required so that the value of X becomes greater than or equal to N or print -1 otherwise.

[link]: https://www.hackerearth.com/practice/algorithms/greedy/basics-of-greedy-algorithms/practice-problems/algorithm/alternative-moves-f12ee40a/
