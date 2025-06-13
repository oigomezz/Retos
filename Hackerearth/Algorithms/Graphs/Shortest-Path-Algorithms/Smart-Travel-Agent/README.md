# [Smart travel agent][link]

Our smart travel agent, Mr. X's current assignment is to show a group of tourists a distant city. As in all countries, certain pairs of cities are connected by two-way roads. Each pair of neighboring cities has a bus service that runs only between those two cities and uses the road that directly connects them. Each bus service has a particular limit on the maximum number of passengers it can carry. Mr. X has a map showing the cities and the roads connecting them, as well as the service limit for each bus service.

It is not always possible for him to take all tourists to the destination city in a single trip. For example, consider the following road map of seven cities, where the edges represent roads and the number written on each edge indicates the passenger limit of the associated bus service.

In the diagram below, It will take at least five trips for Mr. X. to take 99 tourists from city 1 to city 7, since he has to ride the bus with each group. The best route to take is 1 - 2 - 4 - 7.

**Problem:** What is the best way for Mr. X to take all tourists to the destination city in the minimum number of trips?

## Input format

- The first line will contain two integers: N (N ≤ 100) and R, representing the number of cities and the number of road segments, respectively.
- Each of the next R lines will contain three integers (C1, C2, and P) where C1 and C2 are the city numbers and P (P > 1) is the maximum number of passengers that can be carried by the bus service between the two cities. City numbers are positive integers ranging from 1 to N.
- The (R+1)th line will contain three integers (S, D, and T) representing, respectively, the starting city, the destination city, and the number of tourists to be guided.

## Output format

The output should contain 2 lines - the first line giving the route taken and the second line giving the minimum number of trips.

**Note:** If multiple solutions exist . Print lexicographically-smallest path. Agent is also travelling in the same path so he has to be counted while travelling in that path for each trip.

[link]: https://www.hackerearth.com/practice/algorithms/graphs/shortest-path-algorithms/practice-problems/algorithm/smart-travel-agent/
