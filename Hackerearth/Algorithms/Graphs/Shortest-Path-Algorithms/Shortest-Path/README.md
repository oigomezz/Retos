# [Shortest path][link]

In a country, there are N cities numbered from 1 to N.

There are M trains in the country which are used by people to move from one city to another. Each train starts from city Li and ends at city Ri and the cost of taking the train is Wi. One can travel between any two cities (from smaller index to larger one) that lie between Li and Ri ( both inclusive) with the cost of Wi.

More formally people can travel from city u to v (Li <= u < v <= Ri) at the cost of Wi (1 <= i <= M).

**Task** Determine the minimum cost required to travel from city 1 to city N. If the city N is not reachable from city 1 then print -1.

## Notes

- Assume 1-based indexing
- Trains are given in form of array A of size M\*3, denoting the starting city, ending city, and the cost

## Function description

Complete the function solve provided in the editor. This function takes the following 3 parameters and returns the minimum cost required to travel from city 1 to city N:

- N: Represents the number of cities
- M: Represents the number of trains
- A: Represents array in which A[i][0], A[i][1], and A[i][2] represent the city at which ith train starts, the city at which ith train ends, and the cost of taking the train respectively

## Input format

- The first line contains T denoting the number of test cases. T also specifies the number of times you have to run the solve function on a different set of inputs.
- For each test case:
  - The first line contains 2 integer N and M represents the number of cities and the number of trains.
  - The Next M line contains 3 space-separated integers that represent the city at which ith train starts, the city at which ith train ends, and the cost of taking the train respectively.

## Output format

For each test case in a new line, print the minimum cost required to travel from city 1 to city N. If the city N is not reachable from city 1 then print -1.

[link]: https://www.hackerearth.com/practice/algorithms/graphs/shortest-path-algorithms/practice-problems/algorithm/shortest-path-7-f25d82a1/
