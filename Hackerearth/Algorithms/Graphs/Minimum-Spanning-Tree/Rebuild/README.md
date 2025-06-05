# [Rebuild][link]

All roads of Byteland have been destroyed by a recent epic fight between good and evil. Unfortunately, the citizens need to get back to work and need to rebuild their road network.

There are n interesting points in the city, and there are m proposals for roads to build between the points. The i-th proposal is to build an undirected road between the ai-th point and the bi-th point with a cost of ci.

The city would like to build a set of roads such that it's possible to go from any one interesting point to any other interesting point through some series of built roads. They know that at least one such set of roads exists. If there are multiple sets of roads that satisfy the condition, they would like to find a set that minimizes the total cost of roads built. If there are multiple sets with minimum total cost, they will break ties in a process described in the next paragraph.

In the process of rebuilding, the city would also like to lower congestion in some points. More specifically, if there are multiple sets of roads with the same minimum cost, they would like to choose a set that minimizes the number of roads incident to the first interesting point (while keeping the cost minimum). If there are still ties, they would like to minimize the number of roads incident to the second interesting point (while keeping the cost and the number of roads incident to the first interesting point to be small). This continues on until the last interesting point.

More formally, we can say the degree sequence of a set of roads is the sequence {deg(1),deg(2),...,deg(n)}, where deg(i) is the number of roads incident to the i-th interesting point. Given two sets of roads R1,R2 that each connect all the points, we can say the city prefers R1 to R2 if R1's cost is strictly smaller than R2's cost, or R1 and R2 costs are equal and the degree sequence of R1 is lexicographically smaller than the degree sequence of R2.

Given n and the description of the m proposals of roads, print the minimum cost of a set of roads that connects the points and the degree sequence of that set of roads.

## Input format

- The first line of the input will contain an integer T, denoting the number of test cases.
- Each test case will be formatted as follows:
  - The first line of the test case will contain 2 integers, n, m.
  - Then m lines will follow, each with 3 integers ai, bi, ci.

## Output format

Print two lines for each test case.

- The first line contains the minimum cost of a set of roads that connects all the points.
- The second line contains n space separated integers, the degree sequence of the set of roads chosen. The i-th number on this line represents the number of roads incident to the i-th interesting point.

[link]: https://www.hackerearth.com/practice/algorithms/graphs/minimum-spanning-tree/practice-problems/algorithm/rebuild/
