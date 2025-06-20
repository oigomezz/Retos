# [Covering Chessboard][link]

You have an n by m grid. Each grid square has a certain value associated with it. This is given by the numbers vi,j.

You can capture grid squares in two different ways.

1. You can directly capture a grid square. This costs ci,j.
2. You can indirectly capture a grid square. You can only do this if we have already captured all of this squares neighbors. This costs bi,j ≤ ci,j.

Two squares are neighbors if they share an edge.

Your score is the sum of values you have captured minus the cost it took to capture those squares. Return the maximum possible score you can achieve.

## Input format

- The first line of input will contain two integers n, m.
- The next n lines of input will contain m space separated integers each. The j-th number on the i-th line denotes vi,j.
- The next n lines of input will contain m space separated integers each. The j-th number on the i-th line denotes bi,j.
- The next n lines of input will contain m space separated integers each. The j-th number on the i-th line denotes ci,j.

## Output format

Print a single integer, the answer to the problem.

[link]: https://www.hackerearth.com/practice/algorithms/graphs/min-cut/practice-problems/algorithm/covering-chessboard/
