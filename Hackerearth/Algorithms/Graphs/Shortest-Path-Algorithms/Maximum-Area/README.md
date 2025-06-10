# [Maximum Area][link]

While walking around Hackerland, Marichka found a large square grid of size N\*N consisting of unit squares of size 1\*1. Now Marichka wants to explore it as much as possible.

In one move Marichka can move to the cell which shares an edge with cell, where Marichka currently is. It will take her Aij (1 <= Aij <= 10⁶) minutes, where (i,j) is the coordinates of the cell where Marichka moved. Marichka defines her exploration level as the maximum row number for all cells she visited multiplied by maximum column number for all cells she visited. Marichka always starts her exploration in the cell with coordinates (1,1). Your task is to help Marichka maximize this score. Marichka is limited in time, so she can't spend more than T minutes exploring the grid.

## Input format

- The first line contains two integers N, T size of the grid.
- Each line i of the N subsequent lines contains N integers describing i-th row of the grid --- ai1, ai2, ..., ain.

## Output format

Output maximum Marichka's exploration level.

[link]: https://www.hackerearth.com/practice/algorithms/graphs/shortest-path-algorithms/practice-problems/algorithm/maximum-area-fd641ce2/
