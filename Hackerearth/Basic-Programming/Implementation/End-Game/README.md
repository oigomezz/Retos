# [End Game][link]

Black and White are playing a game of chess on a chess board of n X n dimensions. The game is nearing its end. White has his King and a Pawn left. Black has only his King left. So, definitely Black cannot win the game. However, Black can drag the game towards a draw, and, he can do this only if he captures White's only left pawn. White knows exactly what he must do so that he wins the game. He is aware of the fact that if his Pawn reaches Row 'n' (topmost row as seen by White) , he is allowed to replace that Pawn by a Queen. Since White plays chess regularly, he knows how to beat the opponent in a situation in which the opponent has only a King left and he (White) has a King as well as a Queen left. The current scenario of the game will be given to you. You must tell whether this game will end with a Draw or will it end with White winning.

If Move = 0, it is currently White's move and if Move = 1, it is currently Black's move.

Black and White play alternately.

White's piece will be captured by Black if Black's King manages to reach the same square in which White's piece is currently in.

White's king is currently placed at the the point (1,n). White is in a hurry to convert his pawn into a queen, so , in every move of his, he only plays his pawn forward ( towards row n ), ignoring his king.

So, naturally, Black plays his King towards White's Pawn in order to capture it.

White's Pawn is currently located at the point (a,b).

Black's King is currently located at the point (c,d).

Pawn movement on a chess board : Pawn can move only one step forward, provided no piece is blocking it from doing so. ie. it can move only from (u,v) to (u+1,v), provided there is no piece (white or black) at (u+1,v)

King movement on a chess board : King can move one step in any direction. ie if it is at (u,v) currently, then it can move to (u+1,v) , (u-1,v) , (u,v+1) , (u,v-1) , (u+1,v+1) , (u+1, v-1) , (u-1,v+1) , (u-1,v-1), provided it remains inside the chess board

If at any moment the White Pawn is blocked by the black king from moving forward, white will be forced to play his king in such a case.

## Input format

First line consists of T, the number of test cases. Every test case comprises of a single line containing space separated integers n, a, b, c, d, Move.

## Output format

For every test case, print a single line, 'Draw' is the game ends as a draw or 'White Wins' if the game ends in white winning.

[link]: https://www.hackerearth.com/practice/basic-programming/implementation/basics-of-implementation/practice-problems/algorithm/end-game/
