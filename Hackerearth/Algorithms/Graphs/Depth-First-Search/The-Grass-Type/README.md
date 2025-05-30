# [The Grass Type][link]

Ash Catch'Em apparently loves only two things in his life: graph theory, and his grass type Poke'mons. And instead of using his grass type Poke'mons to be a better trainer, he just arranges them in a graph, and solve random questions.

Currently Ash is playing with his Bulbasaur. With its help, he has managed to create a tree of N vertices which are rooted at 1. Each of the vertices have labels namely A1, A2, ... , AN -1, AN.

Ash is trying to explain the concept of LCA, known as the Lowest Common Ancestor to his Poke'mons, so that they'll be able to understand how and what kind of evolution will they have to go through in future.

But we all know know that Ash is a little... slow at explaining things. So, he wants you to find the total number of unordered pairs (u,v) such that ALCA(u,v) == Au \* Av, where u != v . He thinks that this equation will help him figure out the logic behind the evolution of grass type Poke'mons. Can you help him find the total number of such pairs?

## Input format

- The first line consists of a single integer N denoting the total number of vertices in the tree created by Bulbasaur using Leech Seed.
- The next N-1 lines consist of two integers u and v denoting an edge.
- The next line will consist of N integers A1, A2, ... , AN -1, AN.

## Output format

Output the total number of pairs (u,v) such that ALCA(u,v) == Au \* Av and u!=v.

[link]: https://www.hackerearth.com/practice/algorithms/graphs/depth-first-search/practice-problems/algorithm/the-grass-type/
