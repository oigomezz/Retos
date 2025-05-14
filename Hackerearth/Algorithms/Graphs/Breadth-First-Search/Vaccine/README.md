# [Vaccine][link]

There is a country with N villages and each village has a number associated with them and M roads, a road connects two different villages.

In this country, the Prime minister decided to test the hospitals to see if they can handle another wave of the coronavirus pandemic.

A village has the vaccine if the number associated with it is a prime number (villages numbered 2,3,5,7,11... will have a vaccine with them)

For each village find the minimum time required for the vaccine to arrive there if for each road between villages u and v it takes max(u,v) time to travel this road.

**Note:** The graph does not have self-loops or multi edges.

## Input format

- The first line will contain N and M, the number of villages and the number of roads respectively.
- The next M lines contain two integers u and v (meaning there is a road between villages u and v and it takes max(u,v) time to travel this road).

## Output format

Print N space-separated integers which is the minimum time for the vaccine to arrive at that village, if it's impossible for the vaccine to arrive at a particular village then print -1

[link]: https://www.hackerearth.com/practice/algorithms/graphs/breadth-first-search/practice-problems/algorithm/vaccine-2c845ac0/
