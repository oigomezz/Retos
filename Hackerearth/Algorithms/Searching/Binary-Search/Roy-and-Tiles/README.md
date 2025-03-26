# [Roy and Tiles][link]

Roy is playing Tiles game. It consists of a Source node and Destination node and a tiles grid of size NxN.

Grid lies in between Source and Destination (See the image below).

All of them have some value associated with them denoted by S (Source value), D (Destination value) and grid[i][j] (tile value) where 1≤i≤N, and 1≤j≤N.

Roy is at the Source node and he has to reach Destination node to finish the game. Rules of the game are:

- We can move from Source to any tile of row1, if the value of that tile is 1 greater than Source. In other words, we can move from source to grid[1][j] , if grid[1][j] = 1+S where 1≤j≤N.

- We can move from rowi to any tile of rowi+1, if the value of the tile at rowi+1 is 1 greater than the current tile's value. In other words, we can move from grid[i][j1] to grid[i+1][j2], if grid[i+1][j2] = 1+grid[i][j1] where 1≤j1, j2≤N.

- We can move from last row to Destination node, if the value of the Destination node is 1 greater than the current tile's value. In other words, we can move from grid[N][j] to Destination node, if D = 1+grid[N][j] where 1≤j≤N.

Your task is to find the number of ways Roy can move from Source to Destination node. Since the answer can be very large, output it modulo 1000000007. Note that there are several queries with separate values of S and D on the same grid.

## Input format

- First line contains T - number of test cases.
- First line of each test case contains size of grid N.
- Next N lines each contains N space separated integers.
- Followed by integer Q, number of queries.
- Each of the next Q lines contains two space separated integers, S and D.

## Output format

For each query of each test case, print in a new line number of ways Roy can go from S to D.

[link]: https://www.hackerearth.com/practice/algorithms/searching/binary-search/practice-problems/algorithm/roy-and-tiles-1/
