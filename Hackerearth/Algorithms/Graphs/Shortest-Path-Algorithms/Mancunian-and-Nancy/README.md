# [Mancunian And Nancy Play A Game][link]

Mancunian is in a committed relationship with his girlfriend Nancy. His idea of a date is for them to have a romantic candlelight dinner and then play graph games. This time they are using a graph of N nodes and E edges. Mancunian is located at vertex M1 and wants to move to M2. Nancy wants to move from vertex N1 to N2. Anyone can move at any time, till both have reached their respective destinations. But there is a catch. Nancy can't bear to be too far away from her true love, Mancunian and hence the shortest distance between them at any point in time should never exceed a specified parameter K.

You are given several possible pairs of N1,N2, for Nancy. Count the number of such pairs which will make a valid game (where both Mancunian and Nancy can reach their respective destinations without violating the distance condition).

## Input format

- The first line contains three integers N, E and K denoting the number of vertices, number of edges in the graph and the maximum allowed distance between the two lovers respectively.
- The following E lines contain two integers A and B, denoting an undirected edge between those two vertices. There will be no self-loops or multiple edges in the graph.
- Next line contains two integers M1 and M2 denoting the source and destination for Mancunian.
- Next line contains a single integer Q denoting the number of games.
- Each of the next Q lines contains two integers N1 and N2 denoting the source and destination for Nancy, for that game.

## Output format

Print a single integer, denoting the number of valid games.

[link]: https://www.hackerearth.com/practice/algorithms/graphs/shortest-path-algorithms/practice-problems/algorithm/mancunian-and-nancy-play-a-game-1/
