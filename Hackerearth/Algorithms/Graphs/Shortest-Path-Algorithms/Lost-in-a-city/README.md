# [Lost in a city][link]

A country consists of n cities and m one-way roads. There is a central city with number s. Each city sells a particular sweet (city i sells sweets of value vi).

You are required to go to city d. If you are currently in city x, then you can randomly select and move to one of the cities that is directly reachable from x through a single road. You can perform this technique until you reach city d. You must stop once you reach the destination city.

You can buy sweets only once on your way. Determine the highest value p such that you can take home a sweet whose value is at least p independent of the path that you take. Print the value of p for each destination city d from 1 to n.

## Input format

- First line: An integer t denoting the number of test cases.
- For each test case:
  - First line: Three integers n,m, and s.
  - Next line: n integers denoting the value of a sweet that is sold in each city.
  - Next m lines: Two integers u and v denoting a directed road from city u to v.

## Output format

For each test case, print n space-separated integers denoting the answer to each destination city.

[link]: https://www.hackerearth.com/practice/algorithms/graphs/shortest-path-algorithms/practice-problems/algorithm/lost-in-city-f6e7f540/
