# [Mishki Playing Games][link]

Mishki loves playing games, so she asked her friend Hacker to join her in the Game of Stones. In this game, they have N sets of stones, numbered from 1 to N. Each set consists of Ai stones, where 1 <= i <= N.
In each turn, player can select any of the set containing at least 1 stone, and have to reduce it to half of the present number of stones , i.e Ai/2 (Integer Division) from it, and in case of single stone, he/she has to empty the set by removing it.
As the game is really interesting, both will play this game on Q days. On each day, they will some select sets of stones numbered from l to r, where 1 <= l <= r <= N and being a lover of the games, everyday Mishki will be the first player to take the turn.
The one who won't be able to play his/her turn in the game (i.e no stones left in teh selected set of stones), will loose the game.
You need to tell the winner of the game on each day, if both the player will play optimally and take their turn alternatively.

**Note:**

1. Each day, before starting the game they will have the same number of stones in the set as given initially.
2. Use fast i/o for large test files.

## Input format

- The first line will consists of 2 integers N and Q denoting the number of sets of stones, and number of days respectively.
- Next line contains N space separated integers Ai, denoting the number of stones in each set.
- Each line of next Q lines contains 2 space separated inegers, l and r, denoting the range of sets used in the game on ith day.

## Output format

Print Q lines, each line containing the winner of the ith day.

[link]: https://www.hackerearth.com/practice/basic-programming/implementation/basics-of-implementation/practice-problems/algorithm/mishki-playing-games/
