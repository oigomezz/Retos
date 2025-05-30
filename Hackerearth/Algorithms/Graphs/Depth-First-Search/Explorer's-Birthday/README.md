# [Explorer's Birthday][link]

Today is Explorer's birthday, and two of his best friends Raful and Jambo gave him a tree with N vertices and N-1 edges. After playing with it for a while, Explorer got bored, so Raful and Jambo gave him a task:

Find the answer: A modulo 10⁹ + 7 - sum of all functions for all f(u,v) unordered pairs of vertices (u,v) such that u != v. The function f(u,v) is the product of the weights of the edges on the shortest path between u and v. Note that pairs (u,v) and (v,u) are considered the same, so must only be counted once.

He easily solved it. Can you (the best programmer in Lalalandia) do it too?

## Input format

- The first line contains one integer N - the number of vertices.
- The next N-1 lines describe the edges: each contains three integers u, v and c. This means that there is the edge with weight c between vertices u and v.

## Output format

The first line should contain the single integer A modulo 10⁹ + 7 - sum of all functions f(u,v).

[link]: https://www.hackerearth.com/practice/algorithms/graphs/depth-first-search/practice-problems/algorithm/explorers-birthday/
