# [Game of Deletion][link]

Two players are playing the game of deletion. Player1 plays with array A and Player2 plays with array B. The length of both the arrays are N.

The game is like this - both of them want to delete their respective arrays. A player can delete the array in multiple steps.

During one step, he chooses some numbers from the array and takes the bitwise OR of these numbers and remove these numbers from the array.

This bitwise OR is the cost incurred in deleting the selected numbers. This way he deletes his whole array. The reward of deleting the entire array will be the sum of all numbers in the array minus the sum of the cost of all the steps.
The player with the maximum reward will win.

You have to print the winner along with the margin of reward he wins with. Let's say Player1 scored reward1 and Player2 scored reward2 and Player1 wins , then the margin will be reward1 - reward2.

## Input format

- First line contains a number N . N is the length of the array.
- Second line contains the N integers corresponding to elements of the array with Player1.
- Third line contains the N integers corresponding to elements of the array with Player2.

## Output format

- If Player1 wins, print 1 followed by a space and then the reward margin he wins with.
- If Player2 wins, print 2 followed by a space and then the reward margin he wins with.
- Print 1, if the game draws.

[link]: https://www.hackerearth.com/practice/basic-programming/bit-manipulation/basics-of-bit-manipulation/practice-problems/algorithm/game-of-destruction-f96cd509/
