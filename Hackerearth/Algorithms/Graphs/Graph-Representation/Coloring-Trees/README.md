# [Coloring trees][link]

There are N cities that are connected by N-1 roads. K cities have bus terminals and other N - K cities have bus stops. A bus terminus is a designated place where a bus starts or ends its scheduled route.

A bus should start from a terminal and must end its journey at another terminal visiting any city at most once. A city is crowded if there is a bus service in the city where one or more than one bus visits it along any route. You are required to simulate the routes for the buses so that the maximum number of cities is crowded. You can assume there is a number of buses ready for service from each terminus.

## Input format

- First line: Two space-separated integers N and K.
- Next N-1 lines: Two integers u and v that denote city u and city v is connected by a road.
- Next line: K integers denoting the cities that have a bus terminal.

## Output format

Print the number of cities that are crowded after all simulations.

[link]: https://www.hackerearth.com/practice/algorithms/graphs/graph-representation/practice-problems/algorithm/coloring-the-tree-7e8a557a/
