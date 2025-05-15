# [Gears in a machine][link]

Alice and Bob are working on a new contraption to make the most of their extended summer vacations. However, they ran into some trouble with the mechanics of their machine, specifically, in the gear trains. The complicated meshing of gears has confused them and they require your help to make it functional.

A gear train is a network of gears that are engaged with each other. Mechanically, two gears are said to be engaged or connected if some segment of their teeth interlocks, so that rotating gear forces the rotation of the other gear. This mechanism forces all gears that are engaged with the latter gear to rotate and this motion propagates throughout the train. This type of network can be described in terms of a graph where each vertex represents a gear and an edge denotes that two gears are engaged.

There are two types of gears, internal and external. The types of gears depend on which region their teeth are present. Note that all gears are fixed to their position.

You are given a network of N gears and M connections. Determine whether rotating two given gears in given directions results in a functional rotation. You must answer Q queries.

## Input format

- The first line contains 3 integers N,M,Q denoting the number of gears, the number of connections and the number of queries respectively.
- The second line contains N integers the i-th of which is 1 if the gear is external or -1 if it is internal.
- The next M lines contain two integers u and v denoting that gears u and v are engaged.
- The next Q lines contain 4 integers gp, gf, dirp, dirf denoting the gears held by Alice and Bob and the directions in which they are rotated.

## Output format

For each query, print a single line containing 'YES' if the rotation is functional or 'NO' if it is not.

[link]: https://www.hackerearth.com/practice/algorithms/graphs/breadth-first-search/practice-problems/algorithm/gear-up-fa635535/
