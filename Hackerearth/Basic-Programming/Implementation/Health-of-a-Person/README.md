# [Health of a Person][link]

There N people in your city. The jth person contains Aj health point. You are trying to make these people walk in your locality. You walk for M days. On the ith day, every walk decreases Bi health points of the person you are walking with. Also, on the ith day, you can only walk with the jth person if the person is still healthy and j is a multiple of i. You can walk with as many people as you can but you can walk with a specific person only once in a day.

A person becomes unhealthy if their health point becomes less than or equal to 0. At the end of each day, their health points are restored to their original level if they are not unhealthy already.

Your task is to determine the day in which the ith person becomes unhealthy or will remain healthy.

## Input format

- First line: T denoting the number of test cases
- For each test case:
  - First line: Contains two integers N and M denoting the number of people and days on which you walk respectively
  - Next line: N integers where Ai denotes the health points of the ith person
  - Next line: M integers where Bi denotes the reduction of the health of the ith day's walk

## Output format

Print N lines where the ith of these​​​​​ lines contain a single integer, denoting the day when the ith person becomes unhealthy. Otherwise, print -1 if the ith person never becomes unhealthy.

[link]: https://www.hackerearth.com/practice/basic-programming/implementation/basics-of-implementation/practice-problems/algorithm/attack-of-the-mind-flayer-3-119b5d47/
