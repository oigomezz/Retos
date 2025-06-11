# [Furthest vertex][link]

There are n vertices.

Your task is to perform q queries:

- 1 a b - add an undirected edge of the length 1 between vertices a and b
- 2 a - find the distance to the furthest vertex reachable from the vertex a

Guaranteed that graph will not contain loops and cycles during all the time.

## Input format

- First line of the input contains two integers n and q.
- Then follow q lines. The i-th of them contains integers: typei, ai and if typei = 1, bi.

## Output format

Print the distance which is needed for each query of the second type.

[link]: https://www.hackerearth.com/practice/algorithms/graphs/shortest-path-algorithms/practice-problems/algorithm/furthest-vertex/
