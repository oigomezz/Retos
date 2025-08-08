# [Filler Game][link]

You are playing a game called filler game with your friend. In the game you are given an N x M grid, i.e., a grid with N rows and M columns. The players make alternate moves. Each cell in the grid can be empty or filled. In one move, a player can fill a cell, if and only if this cell is empty and there is an empty cell sharing an edge with this cell. The player who can't make the last move, loses the game. Assume that both you and your friend play optimally.

You are given Q queries. In each query, you are given an N x M grid. You have to tell who will win if it is your turn to move on the given grid. If the winner is your friend, print 1, else print 0 if you will win the game.

**Note:** It is advised to use fast input methods, as the input is large.

## Input format

- First line of input contains three space-separated integers N, M and Q, denoting the number of rows in the grid, the number of columns in the grid and the number of queries, respectively.
- Now for each of the Q queries, you will be given N lines containing string of M length, denoting the N x M grid. The strings contain only 0's and 1's. If the cell of the grid is empty, the string will have a 0 at that place, and if that cell is filled, it will have a 1.

## Output format

Output contains Q lines. Each line contains the answer(either 0 or 1) to the game for each query.

[link]: https://www.hackerearth.com/practice/algorithms/dynamic-programming/bit-masking/practice-problems/algorithm/filler-game-2/
