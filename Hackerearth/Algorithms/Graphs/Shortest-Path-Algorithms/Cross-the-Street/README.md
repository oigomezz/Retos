# [Cross the street][link]

ABC Company is involved in the logistics business.

The company has many outlets and stockyards in a city. The city is like an N\*M grid. We consider a single cell of the given grid to be a single block in the city. The stockyard is at the upper-left corner and the outlet is located in the lower right corner. Everyday, one of the employees has to travel from the upper left to the lower right corner for supplies. Each block in the city has a height, where the height of the block located at position (i,j) in the grid is equal to Aij. The company wants to change the heights of some of the blocks, so that the employee can enjoy a high-speed drive from the stockyard to the outlet. But this change comes at a certain cost.

Specifically, if they change a block height from x to y, then they must pay exactly |x-y| dollars. Please help them find the minimum cost, such that by spending that specific amount, they can get a path from stockyard to the outlet with all blocks along the path having the same height.

In a single move, the employee can move from a block to any of its adjacent blocks. Note that during this journey, the employee is allowed to move in all four directions, fulfilling the condition that he never goes out of the grid at any point in time.

## Input format

- First line contains two positive integers N and M - number of rows and columns in the city.
- Then, N lines follow, each containing M integers, where the integer on the i-th line denotes Aij.

## Output format

The first and only line of output should contain minimum cost.

[link]: https://www.hackerearth.com/practice/algorithms/graphs/shortest-path-algorithms/practice-problems/algorithm/cross-the-street-72/
