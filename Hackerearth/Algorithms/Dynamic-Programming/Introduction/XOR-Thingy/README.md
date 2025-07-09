# [Xor Thingy <July Circuits '19>][link]

There are n players playing a game. Every player has a skill value denoted by Si. Before the game starts, each player can change their skill value to any non-negative integer smaller than their current skill value or leave it untouched. The coolness of the game is then defined as the bitwise-xor of the players skill values. We'd like to know for every number X from 0 to m the number of ways that the coolness of the game equals X. Since these numbers may be extremely large, output them modulo 10⁹ + 7.

## Input format

- The first line of input contains two integers n and m, the number of the players and the parameter from the problem statement.
- The second line of input contains n space-separated integers, describing the skill values of the players.

## Output format

Output m+1 integers, the i-th of which is the number of ways that the coolness of the game equals i-1 modulo 10⁹ + 7.

[link]: https://www.hackerearth.com/practice/algorithms/dynamic-programming/introduction-to-dynamic-programming-1/practice-problems/algorithm/xor-thingy-2d7dbe08/
