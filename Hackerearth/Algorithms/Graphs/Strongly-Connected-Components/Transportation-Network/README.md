# [Transportation network][link]

The country of Byteland consists of n cities. Between any 2 cities it is possible to have a railway track and a road.

Railway tracks are bidirectional, meaning if there exists a railway track between u and v then you can take a train from u to v as well as from v to u. Similarly, roads are bidirectional, meaning if there exists a route between u and v then you can drive from u to v as well as from v to u.

2 cities, u and v are called railway-connected if it is possible to travel between u and v using railway tracks.

2 cities, u and v are called road-connected if it is possible to travel between u and v using roads.

The transportation network is called balanced if for all pairs of cities u, v:

u,v are railway-connected if and only if u,v are road-connected.

Initially, there are n cities and no roads or railways in Byteland. You will be given q instructions asking you to build either a railway track or a road between some 2 cities. After each instruction, you must report whether the transportation network is balanced.

## Input format

- The first line of input will contain 2 integers, n and q. q lines will follow. Each line will contain 3 space-separated integers in one of the following formats:
  - 1 u v : build a railway track between u and v.
  - 2 u v : build a road between u and v.

## Output format

You must print q lines. The ith line contains an answer to the question whether the transport network is balanced after the ith instruction. If it is balanced print "YES" (without quotes) otherwise print "NO" (without quotes).

[link]: https://www.hackerearth.com/practice/algorithms/graphs/strongly-connected-components/practice-problems/algorithm/transportation-network-a3bc571b/
