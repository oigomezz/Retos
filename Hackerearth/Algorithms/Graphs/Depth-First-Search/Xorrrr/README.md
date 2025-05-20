# [Xorrrr][link]

Bob lives in a country called HackerLand and in this country, there are N cities numbered 1 to N and they form a tree. That is, there are N-1 undirected roads between these N cities and every two cities can reach each other through these roads. The length of the road between city i and city j is (i+j) (meaning if there is a road between city i and city j then the length will be i + j).

So a great scientist in HackerLand invented the new car in which Bob can travel from one city to another city in f(i,j) time where f(i,j) indicates bitwise xor of length of the roads in the simple path between city and . So Bob was curious to find the bitwise xor of all f(i,j) such that 1 <= i,j <= N. Help Bob to find.

## Input format

- The first line contains N, the number of cities in the country.
- Then N-1 lines contains two integers u and v, means that there is a undirected road between city u and city v. It is guaranteed that the given roads form a tree.

## Output format

Print a single integer denoting our answer.

[link]: https://www.hackerearth.com/practice/algorithms/graphs/depth-first-search/practice-problems/algorithm/xorrrr-40caac1a/
