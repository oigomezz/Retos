# [Book-Cricket][link]

The rules of a cricket game are as follows:

- The game is played for N overs.
- Each over consists of 6 balls.
- The batting team has P number of players.
- At the start of the game, the first 2 players come out to play. The first player is called the striker (the one facing the current ball) and the second player is called the non-striker.
- The striker continues being the striker until he either gets OUT (he will be replaced by the next player who is yet to play) or his strike gets ROTATED (the striker becomes the non-striker and the non-striker becomes the striker).
- Each ball consists of one of the following events:
  - 0 : This adds no score to the striker.
  - 1 : Adds one run to the striker and the strike gets ROTATED.
  - 2 : Adds two runs to the striker.
  - 4 : Adds four runs to the striker.
  - 6 : Adds six runs to the striker.
  - W : The striker is OUT and will be replaced by next player.
  - At the end of every over, the strike will be ROTATED again.

Write a program to implement the scoreboard of a cricket game.

## Input format

- First line: T (number of test cases)
- First line in each test case: Two space-separated integers N and P
- Second line in each test case: Details of N overs (As a string)

## Output format

For each test case, print the first line as "Case X:" (where X refers to the test case number). In the next P lines, print "Player Y: " followed by the score of the Yth player.

**Note**:

If the player is currently not out, output a '\*' after the score.
If the player has not yet come out to play, output 'DNB' (Did not bat) instead of the score.
It is guaranteed that at the end of the match at least 2 players are still not out.
It is guaranteed that the last ball of the match is not a "W".

[link]: https://www.hackerearth.com/practice/basic-programming/implementation/basics-of-implementation/practice-problems/algorithm/bookcricket-bd707e2d/
