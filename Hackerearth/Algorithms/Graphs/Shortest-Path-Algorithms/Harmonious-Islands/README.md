# [Harmonious Islands][link]

Imagine a planet with two beautiful islands. Each island is decorated with several cities, and they are connected by a network of bidirectional roads. The cost of traveling through each road is provided. Both the islands have equal number of cities and roads.

You are given two arrays,A and B, where A represents the beauty index associated with the cities on Island 1, and B represents the beauty index associated with the cities on Island 2.

To journey from a city i on Island 1 to a city j on Island 2, there exists special unidirectional flights. However, specific conditions must be met:

- j must be a multiple of i, indicating a compatible connection between the cities. (i.e. a unidirectional flight exists between city i to city j if and only if j is a multiple of i).
- The cost of the flight is determined by multiplying the beauty indexes of i-th city and j-th city (i.e. Ai \* Bj), ensuring a harmonious transition between the islands.

Your task is to calculate the minimum cost required to travel from city x on Island 1 to city y on Island 2. If it is not possible to travel from city x to city y based on the given conditions, you should output -1, indicating an incompatible connection.

## Input format

- First line contains an integer T, the number of test cases.
- The first line of each test case contains 2 integers N, M seperated by a space representing the number of cities and roads respectively.
- The next line contains N integers space-seperated by a space representing the array A.
- The next line contains N integers space-seperated by a space representing the array B.
- The next M lines of each test case contains 3 space-seperated integers X, Y, Z representing a bidirectional road from city X of 1st island to city Y of 1st island and it requires a cost Z to travel through that road.
- The next M lines of each test case contains 3 space-seperated integers X, Y, Z representing a bidirectional road from city X of 2nd island to city Y of 2nd island and it requires a cost Z to travel through that road.
- The next line of each test case contains 2 space-seperated integers x,y, which are described in the problem statement.
- It is guaranteed that there are no self loops or multiple edges in the graphs.

## Output format

For each testcase, output an integer, the minimum cost required to travel from city x in 1st island to city y in 2nd island. Or print -1 if it's an incompatible connection in a new line.

[link]: https://www.hackerearth.com/practice/algorithms/graphs/shortest-path-algorithms/practice-problems/algorithm/harmonious-islands-4c2c8172/
