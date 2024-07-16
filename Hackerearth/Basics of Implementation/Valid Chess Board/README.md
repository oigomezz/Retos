# Valid Chess Board

You are given a tiled chart paper of N rows and M columns. There are a total of N x M tiles in it. Each tile is colored either black or white. Now, you need to count how many ways are there to cut valid chessboards of size 8 x 8 out of this chart paper.

Notes

1. One chessboard is different from another if either of them contains at least one tile which is different from another chessboard.
2. The chess board formation should have distinct colors of adjacent cells i.e. Black/White alternative (regular chessboard rules apply).

## Input format

- The first line contains two space-separated integers N and M as input.
- In the next N lines, you are given a string of M characters. Each character is either 0 or 1. If it is 0 then the tile color is white, if it is 1 then the tile color is black.

## Output format

In the output, you need to print an integer that denotes the required count as stated in the problem statement.
