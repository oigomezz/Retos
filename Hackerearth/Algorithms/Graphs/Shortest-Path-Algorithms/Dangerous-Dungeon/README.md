# [Dangerous Dungeon][link]

David is playing a video game set in a dungeon. The dungeon has n interesting points and m one way tunnels connecting those points. The i-th tunnel starts at point ai and ends at point bi and takes ci units of time to traverse. Note that it may be possible that there are two tunnels connecting the same pair of points, and even more strangely, a tunnel that goes back to the same point.

David is currently at the point labeled 0, and wishes to travel to the point n-1 using the smallest amount of time.

David discovered that some points become dangerous at some moments of time. More specifically, for each point, David found an integer oi such that point i is dangerous at all times t satisfying t = oi modulo p. The integer p is the same for every single intersection.

David needs to always be in constant motion, and can't wait at a point. Additionally, he will always be safe in a tunnel, but cannot arrive at a point at the moment it becomes dangerous.

Help David determine the fastest time he can reach his destination.

## Input format

- The first line of input will contain three space separated integers n,m,p.
- The next line of input will contain n space separted integers oi.
- The next m lines of input will each contain 3 integers ai, bi, ci

## Output format

If it is impossible for David to reach point n-1, print -1. Otherwise, print the smallest amount of time it will take David to reach n-1.

[link]: https://www.hackerearth.com/practice/algorithms/graphs/shortest-path-algorithms/practice-problems/algorithm/dangerous-dungeon/
