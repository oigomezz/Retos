# Tri-State-Area

Given a weighted tree (T) and an integer MAXW, count the number of weighted graphs whose non-negative edges weight at most MAXW and T is an MST (minimum spanning tree) for that graph. Output the result modulo 987654319.

## Input format

- The first line of input contains two integers n and MAXW, the number of vertices of the aforementioned tree and the maximum allowed weight of an edge respectively.
- The next n-1 lines describes the tree. Each of which contain three integers, vi, ui and wi, meaning that there's and edge connecting vertices vi and ui with weight equal to wi.
- It's guaranteed that the given graph forms a tree.

## Output format

Print only one integer, the number of desired graphs modulo 987654319.
