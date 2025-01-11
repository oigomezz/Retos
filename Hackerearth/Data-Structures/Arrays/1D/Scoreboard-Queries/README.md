# [Scoreboard queries][link]

In a tournament there are (N+1) players, N players have already played and their scores are denoted by an array A. Here, A1 is the score of the first player, A2 of the second, ..., of the Nth player.

Now, the organizers decide the ranks according to the following rules:

- The player x scored more than player y, player x gets a better rank.

In case of tie, the player with lower indices gets a better rank.

Now, it is the turn of the (N+1)th player to play. Before playing, he wants to know the number of ranks that he can secure so that he can decide his strategy.

Now, the jury has some scoreboard updates. Therefore, your task is to tell the jury after every update the number of distinct possible ranks that he can get.

## Input format

- The first line contains the number of test cases T.
- The first line of each test case contains two integers N and Q denoting the number of players who have already played and the number of updates by jury.
- The second line of each test case contains N space-separated integers of array A .
- Next Q lines of each test case contain two integers L and R denoting the score of the Lth player has changed to R.

## Output format

- For each test case:
  - Print Q lines denoting the number of possible ranks which (n+1)th player can get after every update.

[link]: https://www.hackerearth.com/practice/data-structures/arrays/1-d/practice-problems/algorithm/tournament-and-ranks-67cd4b7e/
