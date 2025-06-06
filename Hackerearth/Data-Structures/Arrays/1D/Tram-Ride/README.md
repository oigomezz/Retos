# [Tram ride][link]

A city has N Tram stations numbered from 1 to N that are connected to one another and form a circle. You are given an array ticket_cost where ticket_cost[i] is the cost of a ticket between the stops number i and (i + 1) % N. The Tram can travel in both directions i.e. clockwise and anti-clockwise.

Return the minimum cost to travel between the given start and finish station.

You are given an integer N where N represents the total number of the tram stations, an integer start which represents the start station, and an integer finish which represents the finish station. You are given an array of positive integers ticket_cost where ticket_cost[i] represents the ticket cost between the station number i and (i + 1) % N.

**Task:** Determine the minimum cost to travel between the given start and finish station.

**Function description:** Complete the Solve() function provided in the editor below that takes the following arguments and finds the minimum cost to travel between the given start and finish station:

- N: Represents the total number of tram stations
- start: Represents the start station
- finish: Represents the finish station
- ticket_cost: Represents ticket_cost[i] denoting the ticket-cost between the station number i and (i + 1) %N

## Input format

- The first line contains an integer N denoting the total number of tram stations.
- The second line contains an integer start denoting the start station.
- The third line contains an integer finish denoting the finish station.
- The fourth line contains an N space-separated integer array ticket_cost, ticket_cost[i] represents the ticket-cost between the station number i and (i + 1) %N.

## Output format

Return the minimum cost to travel between the given start and finish station.

[link]: https://www.hackerearth.com/practice/data-structures/arrays/1-d/practice-problems/algorithm/tram-ride-d7ff3a92/
