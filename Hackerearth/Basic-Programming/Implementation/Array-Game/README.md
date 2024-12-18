# [Array Game][link]

Ashish and Jeel are playing a game. They are given a multiset of arrays (initially only one array is present).
A player has to make the following move in their turn:

- Select one of the arrays of size greater than 1.
- Divide the array into two non-empty parts such that every element of the left array is smaller than every element of the right array.

Formally, if we split an array A of size N into arrays L and R, then the following conditions must hold:

- L must be a non-empty prefix and R must be the remaining non-empty suffix of the array A respectively.
- For every element Pi of L and every element Qj of R, the inequality Pi < Qj must hold.

A player loses if he cannot make a move. Both the players play the game optimally. If Jeel plays first, then determine who wins the game.

## Input format

- First line: An integer T denoting the number of test cases.
- Each test case:
  - First line: An integer N denoting the size of the array.
  - Second line: N space separated integers, the ith integer being Ai.

## Output format

For each test case, print the winner of the game "Jeel" or "Ashish" (without quotes).
Answer for each test case should come in a new line.

[link]: https://www.hackerearth.com/practice/basic-programming/implementation/basics-of-implementation/practice-problems/algorithm/array-game-1-3bdd5d12/
