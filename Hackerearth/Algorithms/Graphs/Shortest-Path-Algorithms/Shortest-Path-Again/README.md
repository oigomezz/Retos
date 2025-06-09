# [Shortest Path Again][link]

There are N cities and Demon is in city 1. Now, there are M pair of roads between some cities and each of the roads have cost to travel by it. The cost to travel from city c1 to ck is 1\*w1 + 2\*w2 + 3\*w3+......+(k-1)\*wk-1 where wi is the cost to travel from city pi to city pi+1. Demon is lazy and so he wants you to find the minimum cost to travel from city 1 to every other city from 1 to N. If there exists no path to travel from city 1 to city i, print -1.

**Note:** There can be self-loop roads or multiple edge roads. All the roads are bidirectional.

## Input format

- The first line contains two space-separated integers n and m - the number of nodes and edges respectively.
- The next m lines contain three space-separated integers x, y, and w - representing an edge between x and y with cost w.

## Output format

Output n lines. In the ith line, output the minimum distance from city 1 to the ith city. If there exists no such path, output -1.

[link]: https://www.hackerearth.com/practice/algorithms/graphs/shortest-path-algorithms/practice-problems/algorithm/shortest-path-again-f5d97dad/
