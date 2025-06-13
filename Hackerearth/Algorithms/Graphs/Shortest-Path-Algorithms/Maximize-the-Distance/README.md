# [Maximize the distance in graph][link]

Given an undirected complete graph G with n vertices. The weight of the edge between (i,j) is equal to Cij. Let D(i,j) be the shortest distance between vertices i,j and W(G) be the sum of all shortest distances between any two vertices. You can remove at most k edges from graph G in order to obtain a graph G'. You have to maximize the ratio of the sum of all shortest distances between any two vertices in new graph G' (after removing the edges) and sum of all shortest distances between any two vertices in old graph G (before reomoving the edges): W(G') / W(G). G must remain connected.

## Input format

- The first line contains two space separated integers n and k denoting the number of vertices and at most how many edges you can remove.
- Next n lines contains n space separated integers. i-th line denotes the elements of Ci.

## Output format

- The first line contains a number q, the number of edges deleted.
- Next q lines contains two space separated integers each, xi,yi denoting that edge (xi,yi) will be deleted.

[link]: https://www.hackerearth.com/practice/algorithms/graphs/shortest-path-algorithms/practice-problems/approximate/maximize-the-distance-in-graph-2e8503e7/
