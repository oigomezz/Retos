# [Components of Graph (Airbus)][link]

You are given a directed network of flights i.e. N cities and M one-directional flights. Each city has a particular air quality index value associated with it. Now, your task is to determine the maximum threshold value X such that if the flights incident to or from the cities with air quality index values less than X is canceled then there should exist a reachable component of cities in the network of size at least K. A subcomponent of a flight network is considered to be a reachable component if all the cities in that component are connected, this implies that all the flights are reachable from each other via direct or connecting flights.

**Note:** You can assume that the answer always exists.

## Input format

- First line: Three integers N, M, and K.
- Next line: N space-separated integers where i-th the integer denotes the value associated with the city number i.
- Next M lines: Two space-separated integers u and v that denote that there is a flight available from the city number u to v.

## Output format

Print the maximum threshold value as described in the problem statement.

[link]: https://www.hackerearth.com/practice/algorithms/graphs/strongly-connected-components/practice-problems/algorithm/components-of-graph-2b95e067/
