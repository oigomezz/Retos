# [The new traveling salesman problem][link]

Alice entered a country that contains n cities and she wants to see all of the cities by incurring the the minimum cost possible. There are m two-way roads in the country. A road connects two cities and it has a cost. The i-th road connects cities vi,ui and costs ci. The difference between this problem and the classic TSP problem is that switching from a road to another road has a cost.

The viscosity for each road is defined as the i-th road has viscosity gi. Switching from a road with viscosity x to a road with viscosity y adds √(x² + y²) cost.

Find the minimum cost needed to see all of the cities.

## Note

- Alice is comfortable with seeing a city or a road several times.
- This problem is an approximation problem and you will get a higher score if you print a path with a lower cost.

## Input format

- The first line contains two integers n, m.
- The next m lines contain the description of roads where the i-th line contains vi, ui, ci, and gi.

## Output format

Print the order in which Alice will see the cities. In the first line, print k that denotes the number of roads in her path. In the next line, print the numbers of the roads she will pass in order.

[link]: https://www.hackerearth.com/practice/algorithms/graphs/graph-representation/practice-problems/approximate/tzp-5a83020f/
