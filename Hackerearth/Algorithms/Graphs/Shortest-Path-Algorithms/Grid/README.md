# [Grid][link]

You are given a grid A of size N\*M, two integers (Si, Sj) and Q tasks. Each task contains two integers, (Di,Dj). Each cell in the grid is either empty cells denoted by O (Capital English character 'o') or occupied cells denoted by \*. Initially, you are at (Si,Sj). Find the minimum number of steps in which you have to take to reach (Di,Dj) from (Si,Sj) without traversing the occupied cells.

In a single step, you can move from any cell (i,j) to the 4 neighboring cells i.e. (i-1,j), (i+1,j), (i,j-1) and (i,j+1) provided these cells are inside the grid A.

## Input format

- The first line of input contains 3 space separated integers N, M and Q where N and M denotes the dimensions of the grid A and Q denotes the number of tasks.
- Each of the next N lines contain a string of length M, j-th character in the i-th line of which is either O or \* denoting that the cell (i,j) is empty or occupied.
- The next line contains 2 space separated integers Si and Sj denoting the source cell of the grid.
- This is followed by Q lines each containing 2 space separated integers Di and Dj.

## Output format

Print the answer to each query on a new line. If there is no path between (Si,Sj) and (Di,Dj), print -1.

[link]: https://www.hackerearth.com/practice/algorithms/graphs/shortest-path-algorithms/practice-problems/algorithm/robot-in-grid-b7d391f7/
