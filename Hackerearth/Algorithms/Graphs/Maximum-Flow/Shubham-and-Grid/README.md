# [Shubham and Grid][link]

You are given a grid of n rows and m columns consisting of lowercase English letters a, b, c, and d.

We say 4 cells form a "nice-quadruple" if and only if

1. The letters on these cells form a permutation of the set {a,b,c,d}.
2. The cell marked b is directly reachable from cell marked a.
3. The cell marked c is directly reachable from the cell marked b.
4. The cell marked d is directly reachable from the cell marked c.

A cell (x2,y2) is said to be directly reachable from cell (x1,y1) if and only if (x2,y2) is one of these 4 cells { (x1 - 1, y1), (x1 + 1 , y1), (x1, y1 - 1) and (x1, y1 + 1)}.

Given the constraint that each cell can be part of at most 1 "nice-quadruple", what's the maximum number of "nice-quadruples" you can select?

## Input format

- First line: Two space-separated integers n and m.
- Next n lines: Each contains m space separated lowercase letters from the set {a,b,c,d} denoting the grid cells.

## Output format

Output the maximum number of "nice-quadruple" you can select.

[link]: https://www.hackerearth.com/practice/algorithms/graphs/maximum-flow/practice-problems/algorithm/shubham-and-grid-806c2c66/
