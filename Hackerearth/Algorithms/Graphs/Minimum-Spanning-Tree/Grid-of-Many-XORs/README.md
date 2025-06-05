# [Grid of Many Xors][link]

Consider a grid with N rows and M columns, where each cell has some integer value written in it. Every cell is connected to every side adjacent cell via an undirected edge. The cost of an edge e connecting any two cells with value a and b is Ce = a ⊕ b (Here ⊕ denotes bitwise xor of two the integers a and b)

We define a good trip between two cells (r1,c1) and (r2,c2) as a trip starting at cell (r1,c1) and ending at cell (r2,c2) while visiting every cell of the grid at least once.

There is a cost associated with every good trip. Let's say, for a given edge e, you travel that edge Te
times. Then the cost of the trip is:

Σ(Ce \* (Te / 2))

Here, (Te / 2) is the ceiling of the result of division of Te by 2.

For the given starting cell (r1,c1) and ending cell (r2,c2), you have to find the minimum cost of a good trip.

## Input format

- The first line will consist of the integer T denoting the number of test cases.
- For each of the T test cases, the first line will consist of two integers N and M, denoting the number of rows and columns of the grid respectively.
- The second line will consist of four integers, r1 c1 r2 c2, denoting the coordinates (r1,c1) of the starting cell and (r2,c2) of the ending cell.
- Then, N lines will follow, each containing M integers, denoting the values in the grid, such that the j-th value in the i-th row will denote the number in the cell (i,j) of the grid.

## Output format

For each of the T test cases, output a single integer, denoting the minimum cost of a good trip.

[link]: https://www.hackerearth.com/practice/algorithms/graphs/minimum-spanning-tree/practice-problems/algorithm/grid-of-many-xors-de84b766/
