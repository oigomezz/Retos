# [Visiting friends][link]

M friendships exist between N people. They are divided into groups such that all the friends will remain in same group and the people from each group visit each other according to the following conditions:

1. Each people can host only one other people from their group.
2. Each people can visit only one other people from their group.
3. Friendship is transitive in nature, which means, if A is a friend of B and B is a friend of C then A is also a friend of C.

Write a program to find the number of ways in which the people from each group can visit each other. Two ways are considered different if at least one people visits two different friends.

## Input format

- First line: T (number of test cases)
- For each test case:
  - First line: Two space-separated integers N and M
  - Next M lines: Two space-separated integers U and V denoting a friendship between U and V

## Output format

For each test case, first print the number of groups and in next line, print the number of ways in which the people from each group can visit each other, in decreasing order of number of ways.

[link]: https://www.hackerearth.com/practice/algorithms/graphs/depth-first-search/practice-problems/algorithm/visiting-friends-9f10e4c8/
