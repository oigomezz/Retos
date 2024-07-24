# Game of Sequence

Two players P and Q are playing a game of sequence on an array A of size n. In each move a player will choose two distinct numbers X and Y , both numbers should be present in the array. Now the player will pick all the positions where the number X is present , and will replace the value there with the number Y.
The game stops if the array has only one distinct value. The player who is unable to make a move in his turn loses.You have to decide who will lose the game. First move is played by the player P.

## Input format

- First line contains a number t that denotes total number of test cases.
- Second line contains a number n as input denoting total size of the array.
- Third line contains n space separated integers denoting the elements in the array A.

## Output format

Output P if the player P loses , Q otherwise.
