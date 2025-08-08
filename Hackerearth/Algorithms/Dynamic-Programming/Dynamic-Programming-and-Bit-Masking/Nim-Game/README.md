# [Nim game][link]

Alice and Bob are playing the classic Nim game. In this version of the game, there are N heaps of stones. The i-th heap consists of i stones. In a single move, a player can select any non-empty heap and remove a positive number of stones from it. Alice starts the game, and both players move alternately. The player who cannot make a move in his or her turn loses the game.

Bob and Alice believe that the game is highly unfair to the second player. They both decide to give Bob an advantage. Before the game begins, Bob must select 2 distinct heaps i,j and combine them to form a single heap (the total number of heaps now will be N - 1 and the combined heap will contain i + j stones). The game, then begins as usual, with Alice making the first move. Both the players play optimally in the game.

Your task is to determine the number of ways in which Bob can select two distinct heaps such that after combining them, Bob has a winning strategy. Since the answer may be large, you have to calculate the answer modulo 10⁹ + 7.

**Note:** If in two ways, one of the selected heaps is different, then these two ways are considered different.

## Input format

- First line: A single integer T denoting the number of test cases.
- For each test case:
  - First line: A single integer N denoting the number of heaps.

## Output format

For each test case, print a single integer, on a new line, that represents the number of ways of winning for Bob modulo 10⁹ + 7.

[link]: https://www.hackerearth.com/practice/algorithms/dynamic-programming/bit-masking/practice-problems/algorithm/unfair-nim-afea7c42/
