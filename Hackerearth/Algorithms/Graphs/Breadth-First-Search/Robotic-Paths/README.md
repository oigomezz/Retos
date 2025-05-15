# [Robotic paths][link]

You have built a new robot and placed it in a maze. The maze contains N rows and each row contains M cells. Each cell of the maze is either an empty cell or an obstacle. An empty cell is denoted by a (.) dot and an obstacle is denoted by a (#) hash. The robot is operated by your computer with some keyboard commands. Currently, there are 4 character commands:

- L: Moves the robot from the current cell to its left cell.
- R: Moves the robot from the current cell to its right cell.
- U: Moves the robot from the current cell to its upper cell.
- D: Moves the robot from the current cell to its lower cell.

The robot can go to some cell only if it is empty and inside the maze. Therefore, you cannot give a command that takes the robot to an obstacle or out of the maze.

The robot is currently at (Sx,Sy) cell. You want to take it to (Fx, Fy) cell. Therefore, you are required to build a string of character commands that takes the robot to the destination. There may exist several strings that can perform the same task but you must use the string of the minimum length. If there exist several strings of the minimum length, you must select the lexicographically smallest string of them.

Refer to the sample explanation section for better understanding.

## Input format

- First line: Two integers N and M.
- Next N lines: Strings of M lengths that represent the maze.
- Next line: An integer Q denoting the number of queries.
- Each of the next Q lines: Four integers Sx, Sy, Fx, and Fy.

**Note:** It is guaranteed that (Sx,Sy) and (Fx,Fy) will be empty cells and (Sx,Sy) != (Fx,Fy)

## Output format

If it is possible to reach the destination, then print the string command as mentioned. Otherwise, print Impossible.

[link]: https://www.hackerearth.com/practice/algorithms/graphs/breadth-first-search/practice-problems/algorithm/robo-path-78511fb1/
