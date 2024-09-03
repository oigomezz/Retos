# Robotic Moves

A robot's initial position is (0,0) and it can only move along X-axis. It has N moves to make and in each move, it will select one of the following options:

- Go to (X-1,0) from (X,0)
- Go to (X+1,0) from (X,0)
- Remain at its current position

Your task is to calculate Σ (abs(X) + abs(Y)) for all reachable (X,Y).

**Note:** Here, abs denotes the absolute value.

See the sample explanation for better understanding.

## Input format

- The first line specifies a number T denoting the number of test cases.
- The first line of each test case containing an integer N denoting the number of moves.

## Output format

Print T lines. For each test case, print a single integer as described in the problem statement.
