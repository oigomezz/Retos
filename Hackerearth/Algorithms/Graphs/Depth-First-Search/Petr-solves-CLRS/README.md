# [Petr solves CLRS][link]

Petr was learning flows. He encountered a problem in the “Introduction To Algorithms by CLRS book”.Petr was not able to solve the problem. And also in the book solutions of problems having odd problem-number were given, and unfortunately, the problem was even-numbered.

So Petr went to Tourist for help. Since Tourist was busy giving his internship interviews, could you help Petr solve the problem?

In a town, there are n people living. And each person has a set of friends. In this town, friendship is symmetric (ie. if A is a friend of B implies B is a friend of A), but not transitive(ie. if A and B are friends & B and C are friends does NOT imply that A and C are also friends). There is a festival in the town consisting of Q days. Each of the Q days one of the n people get a reward in the morning. Initially, all the n people are empty-handed (having 0 reward). A person in the town becomes happy if the total reward of his friends become k. Your task is to find out for each person the day when he becomes happy.

## Input format

- n, m, k
- m lines follow:
  - a, b (a-b are friends)
- q
- q lines:
  - p, x (person p gets reward x)

## Output format

Print n lines for each person tell the day when he becomes happy. or print -1 if he never becomes happy.

[link]: https://www.hackerearth.com/practice/algorithms/graphs/depth-first-search/practice-problems/algorithm/petr-solves-clrs-01096d2d/
