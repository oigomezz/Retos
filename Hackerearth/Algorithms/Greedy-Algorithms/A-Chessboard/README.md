# [A chessboard][link]

In this version of chess, only two kings pieces are placed on the chessboard. Initially, the coordinates of the first king piece are generated (X1, Y1), it is placed on the chessboard at the generated position. Now, the coordinates of the second king piece are generated (X2, Y2), it is placed on the chessboard at the generated position.

These pieces can be moved in a sequential manner, that is, one by one, starting from the first piece. Both the kings want to win if they can not, at least draw.

## Rules

1. The chessboard is a standard 8 x 8 board.
2. The kings can move from one cell to another if they have an edge or corner in common.
3. If the generated coordinates of the second king are exactly equal to the first, then the second king wins.
4. Both players play optimally.
5. The game is considered to be won by the first king piece if after it moves, then it can have the same coordinates as the second. The second king piece becomes the winner if after this piece is moved, then both kings have the same coordinates. The game is drawn if there is no possible ways for anyone to win if both the pieces are played optimally.

## Input format

- The first line contains T denoting the number of test cases.
- The first line of each test case contains two space-separated integers denoting the row and column of the first king (X1, Y1).
- The second line of each test case contains two space-separated integers denoting the row and column of the second king (X2, Y2).

## Output format

Print T lines. For each test case:

- In a single line, print 'FIRST' if the first king piece wins, print 'SECOND' if the second king piece wins, and print 'DRAW' if none of them wins.

[link]: https://www.hackerearth.com/practice/algorithms/greedy/basics-of-greedy-algorithms/practice-problems/algorithm/chessboard-2-8f06e380/
