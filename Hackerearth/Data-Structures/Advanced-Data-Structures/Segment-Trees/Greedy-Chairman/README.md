# [Greedy chairman][link]

One day, Madi, chairman of "Wal’s smart"company, decided to hire new employees.

His secretary, Dina J. Tramp, gave him a list of employees. At first glance, he thought that all candidates have different experience, skills, etc. However, they were same! The only thing that was unique to any candidate, is salary!(however, 2 or more employees can have same value). After that, Madi decided to test his company’s programmer’s skill.

At first, he numbered all candidates from 1 to n. After that, he wrote down all salaries(Candidate with number i wants salary ai). Then, he told him q questions. Every question had format l, r and k. The question was, in how many ways he can choose exaclty k candidates between l and r and hire them, such that Madi will spend miminum amount of money (since answer if very big, output it modulo 10⁹ + 7).His mighty programmist, Ralif tried to solve this problem. Unfortunately, he was unsuccesful. And he asked help from you.

## Input format

- The first line of input contains two integers n and m (1 <= n, m <= 2\*10⁵).
- The second line contains n integer a1,,a2,...an, (1 <= ai <= 10⁹ + 7) - the salary i'th candidate wants.
- Each of the following m lines contains three integer li, ri, ki, (1 <= li, <= ri, <= n, ki, <= ri, - li, +1).

## Output format

Output q lines, each line contains answer modulo (10⁹ + 7).

[link]: https://www.hackerearth.com/practice/data-structures/advanced-data-structures/segment-trees/practice-problems/algorithm/greedy-chairmanaugclash/
