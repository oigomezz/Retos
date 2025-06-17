# [Lonely Island][link]

There are many islands that are connected by one-way bridges, that is, if a bridge connects islands a and b, then you can only use the bridge to go from a to b but you cannot travel back by using the same. If you are on island a, then you select (uniformly and randomly) one of the islands that are directly reachable from a through the one-way bridge and move to that island. You are stuck on an island if you cannot move any further. It is guaranteed that after leaving any island it is not possible to come back to that island.

Find the island that you are most likely to get stuck on. Two islands are considered equally likely if the absolute difference of the probabilities of ending up on them is <= 10^(-9).

## Input format

- First line: Three integers n (the number of islands), m (the number of one-way bridges), and r (the index of the island you are initially on).
- Next m lines: Two integers ui and vi representing a one-way bridge from island ui to vi.

## Output format

Print the index of the island that you are most likely to get stuck on. If there are multiple islands,then print them in the increasing order of indices (space separated values in a single line).

[link]: https://www.hackerearth.com/practice/algorithms/graphs/topological-sort/practice-problems/algorithm/lonelyisland-49054110/
