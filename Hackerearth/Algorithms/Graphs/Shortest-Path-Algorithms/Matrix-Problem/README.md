# [Matrix Problem][link]

Given an nxm board with a number between -1 and nxm in every entries. And an nxm matrix M is also given, where M(i,j) is the cost of selecting the (i,j) entry of the given board.

Your task is to find a connected block (which means these entries can reach each other by just go up, down, left and right without going out the block) in the board that contains at least K distinct positive numbers without any -1, and it must have minimum total cost for selecting these entries. Output the minimum total cost.

## Input format

- First line consists of three integers, n, m, K (1 <= n, m <= 15, 1 <= K <= 7). Then follows are two n\*m matrices, the first matrix denotes the numbers on the board and the second matrix denotes the cost of every entry.
- Namely, the first n lines contain m integers, where the jth number in ith line denotes the number on the entry (i,j) of the board. These integers are in [-1, n\*m].
- Next n lines contain m integers too. The jth number in ith line denotes the cost of selecting the entry (i,j) of the board. These integers are in [1, 100000].

## Output format

Print only one line containing the minimum cost to finish the task. If the task is impossible, output -1 please.

[link]: https://www.hackerearth.com/practice/algorithms/graphs/shortest-path-algorithms/practice-problems/algorithm/matrix-problem/
