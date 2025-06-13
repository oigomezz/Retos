# [Nick and JosephLand][link]

Nick is the mayor of JosephLand. He wants to make a reform of the roads in JosephLand. In JosephLand, there are n cities, numbered 1 through n. There are also m weighted, directed roads represented by three numbers:

- ui,vi,wi: there is a road from ui to vi and the fine taken on this road is wi. That means, if you pass a road from vi to ui, i.e violating the traffic law you have to pay wi coins, otherwise you don't have to pay anything.

Nick is going to have a travel. Travel consists of q journeys. Each journey is represented by two numbers: ai,bi. That means, he starts his journey in ai and ends in bi. Every time he will choose a journey with minimum cost. Cost of a journey is equal to the sum of fines he paid during the journey.

Consumption of a travel is Σ costj. As Nick is the mayor of JosephLand, before the travel he can change directions of any roads as many times as he wants. So now Nick wants to change directions of some roads in such a way, that consumption is minimal. Note that no changes can be made.

## Input format

- The first line contains two integers n, m — the number of cities and the number of roads, respectively.
- Next m lines contain three integers each, ui,vi and wi denoting there is a road from ui to vi and the fine is wi. Note that between a pair of cities can exist more than one road.
- Next line contains a single integer q — the number of journeys.
- Next q lines contain two integers each, ai and bi — the start and the end of the journey, respectively. Note that the start and the end can be the same city.

It is guaranteed that the JosephLand is connected.

**Note:** there can be a problem with stack size.

## Output format

Print the minimum consumption that Nick can achieve.

[link]: https://www.hackerearth.com/practice/algorithms/graphs/articulation-points-and-bridges/practice-problems/algorithm/nick-and-josephlandaugclash/
