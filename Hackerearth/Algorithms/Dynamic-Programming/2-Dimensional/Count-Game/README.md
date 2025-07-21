# [Count Game][link]

Bob and Alice plays a game. Given are N piles with heights represented by an array A. Both players play alternatively. .

Each player will reduce the height of any pile ( with a non zero height ) by at least 1 on his turn. (A player can reduce height of any pile minimum to zero). Player which is unable to reduce height of any pile loses the game.

Alice plays first, can you tell the number of subsets of A with which if the game is played, then it is sure that Bob will win if both the players play optimally.

As number of subsets can be large, output answer modulo 10⁹ + 7. Empty Set should be considered in answer

## Input format

- First line contain an integer N, denoting number of elements in A.
- Second line contain N space separated integers.

## Output format

Print number of subsets of A modulo 10⁹ + 7, with which Bob will win surely.

[link]: https://www.hackerearth.com/practice/algorithms/dynamic-programming/2-dimensional/practice-problems/algorithm/weighted-tree-function-d4f02544/
