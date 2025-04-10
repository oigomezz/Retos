# [Team division][link]

There are N (where N is always even) players standing in a line where the coordinates of players are given as (X1,0), (X2,0)... (XN,0). You are required to divide the min to two teams such that there is an equal number of players on either side. For this, you can select a coordinate (P, 0) if and only if the number of players on the left-hand side is equal to the number of players on the right-hand side. For the players on (P,0), you are independent to choose their side.

Find the number of such possible coordinates where teams can be divided.

**Note:** Non-integral coordinates do not exist.

## Input format

- The first line contains an integer T denoting the number of test cases.
- For each test case:
  - The first line contains an integer N denoting the number of players.
  - The second line contains an array of space-separated integers denoting array X.

## Output format

Print a single line for each test case, denoting the number of coordinates (P.0) from where the teams can be divided.

[link]: https://www.hackerearth.com/practice/algorithms/greedy/basics-of-greedy-algorithms/practice-problems/algorithm/team-division-3f28e964/
