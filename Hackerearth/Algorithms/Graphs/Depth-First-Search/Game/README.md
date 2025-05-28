# [Game][link]

You are playing a game in which you have a rectangular grid of n\*n cells. Each cell is either empty or has a firework. Empty cells are marked with ".", cells with firework are marked with "\*" . Two cells are said to be adjacent if they share a side.

If firework in any cell explodes it destroys itself and the empty cells connected to it. Two cells are connected if there is a path of empty adjacent cells between them.

You have to find the number of cells that will be destroyed if the fireworks are triggered independently.

## Input format

- The first line contains an integer n denoting the dimensions of the grid.
- Each of the next n lines contains symbols: "." for empty cells, "\*" for cells containing a firework.

**Note:** All rows have n number of symbols.

## Output format

Print the sum of the number of cells destroyed if each bomb is triggered independently.

[link]: https://www.hackerearth.com/practice/algorithms/graphs/depth-first-search/practice-problems/algorithm/bomb-game-13ebde2d/
