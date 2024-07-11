# Tic-Tac-Toe

A game of tic-tac-toe is played on a 3X3 square grid. Each cell is either empty (denoted by '.') or occupied by one of the two players ('X' and 'O'). X goes first and then they take turns alternatively. If X is written three times in a straight line, then X wins and the game ends. The same goes for O. If there is no empty cell left, then the game ends as a draw.

You are given the description of a game of tic-tac-toe. You have to determine the state of the game.

The states of the game are as follows:

- If the game is invalid, that is, if there is no possibility of it happening, output "Wait, what?".
- If X has won, then print "X won." else if O has won print "O won.".
- If it is a draw, then print "It is a draw.".
- Otherwise, print whose turn it is, "X's turn." or "O's turn." accordingly.
