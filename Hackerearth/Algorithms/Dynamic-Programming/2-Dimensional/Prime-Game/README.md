# [( Problem B ) Prime Game][link]

Alice and Bob have an integer x consisting only of digits 2,3,5,7. They are playing a game with this number.

The rules of the game are as follows:

- Alice starts the game and then both of them take alternating turns.
- In each turn, the player removes one digit either from the front or back of the integer x in the decimal notation.
- The player who reduces the given integer to a prime number loses the game.

Note that when the number is reduced to one digit, it will always become a prime number, as it will be equal to one of 2,3,5 or 7.

Determine who wins the game if both play optimally.

## Input format

- First line: t (number of test cases)
- Next t lines: Contains the description of t test cases. Each test case is described in a single line with an integer x.

## Output format

For each test case:

- If Alice wins, then print 'Alice' (without quotes) in a single line.
- If Bob wins, then print 'Bob' (without quotes) in a single line

[link]: https://www.hackerearth.com/practice/algorithms/dynamic-programming/2-dimensional/practice-problems/algorithm/prime-game-1-2604365b/
