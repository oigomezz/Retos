# [Summer Vacation][link]

Alex is planning to do some projects during his summer vacation. There are N number of projects divided into 3 groups. Each project has two parameters - t[i], meaning the number of days required to complete that project, and g[i], meaning the group to which that project belongs. Now the summer vacation will last for D days, and Alex has to choose the projects so that the sum of the number of days required to complete the projects is exactly D. But there are two additional conditions:

1. He will do each project only once.
2. He will not do projects from the same group successively, i.e., no two adjacent projects can belong to the same group.

Now, Alex is thinking about the number of ways in which he can select the projects(their order matters) such that the sum of the time required to complete the projects is exactly D, and there are no two adjacent projects from the same group and each project is chosen at most once. Alex is busy preparing for the projects, can you help him to find the number of possible ways. Since, the answer can be very large, output it modulo 10⁹ + 7.

## Input format

- The first line will contain a single integer T denoting the number of test cases. Then the test cases follows.
- The first line of each test case will contain two space-separated integers N and D, denoting the total number of available projects and the number of days in the vacation.
- The following N lines of each test case will contain two space-separated integers t[i] and g[i] denoting the number of days required to complete that project and the group to which the project belongs.

## Output format

Print a single integer denoting the total number of ways of choosing the projects satisfying the given conditions modulo 10⁹ + 7.

[link]: https://www.hackerearth.com/practice/algorithms/dynamic-programming/bit-masking/practice-problems/algorithm/summer-vacation-b0a74639/
