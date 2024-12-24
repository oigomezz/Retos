# [Coin Game][link]

Charlie and Alan have challenged each other to a game of logic with coins.

The game consists of N piles of coins with each pile consisting of Ai coins. The game progresses as follows: in each turn a player selects any of the piles with even number of coins and removes exactly the half the coins out of that pile. The game ends when a player can't make a move. The last move is a winning move.

Charlie makes the first move. Assuming both players play optimally, predict who wins the game.

## Input format

- The first line consists of the number of test cases T (1 <= T <= 100).
- Each test case consists of two lines.
  - The first line in each test case contains the single integer N ( 1 <= N <= 1000) — the number of piles of coins.
  - The second line contains N space separated integers Ai ( 1 <= Ai <= 10^9), specifying number of coins in piles.

## Output format

Output T lines. For each case, output "Charlie" (without quotes) if Charlie wins the game, and "Alan"(without quotes) if Alan wins the game.

[link]: https://www.hackerearth.com/practice/basic-programming/implementation/basics-of-implementation/practice-problems/algorithm/coin-game-3-1762eeeb/
