# [Puzzled Grid][link]

Today, you need to solve a problem on a Puzzled Grid game. "In a grid of NxN size, where each cell has a positive integer, two players compete in several rounds.

Each round starts by both players putting a rock in a random location of the grid. Then, the two players must connect the two rocks with a line that passes through the grid cells (e.g: from a grid cell the line can can expand either horizontally or vertically and never out the grid). Since there may be a lot of ways to connect the two stones, we are only interested in those lines that minimizes the highest cell in their path (e.g: the cell with the highest number should be as small as possible).

You need to find and print this minimized maximum. Can you do it?

## Input format

- First line contains two integers n and Q, where n is the grid size and Q is the number of rounds of the game.
- Next n lines contain each n integer denoting the grid cell numbers.
- Then, next Q lines contain each 4 integers x1,y1,x2,y2 denoting the first and second stone locations -- the indexes are 0 based and the origin is the top leftmost cell.

## Output format

Print Q lines, each denoting the answer for each round.

[link]: https://www.hackerearth.com/practice/algorithms/searching/ternary-search/practice-problems/algorithm/puzzled-grid-1/
