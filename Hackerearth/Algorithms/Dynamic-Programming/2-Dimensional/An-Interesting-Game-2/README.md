# [An interesting game][link]

Bob and Alice are playing with an array A of n elements with Bob starting the game. In each turn:

1. A player picks a non-zero number of elements from A with the same value and remove it from A.
2. The player whose turn makes array A empty wins the game.

Alice modifies the game a bit. She selects some distinct elements that are present in A and removes all other elements that are not selected from A. Now, the game is played using this modified array.

Find the number of possible subsets of elements that Alice can select to modify A such that Alice must win if both the players play optimally.

## Input format

- The first line contains N.
- The next line contains N space-separated integers denoting the elements of A.

## Output format

Print the number of possible subsets of elements that Alice can select to modify A such that Alice must win if both the players play optimally modulo 10⁹ + 7.

[link]: https://www.hackerearth.com/practice/algorithms/dynamic-programming/2-dimensional/practice-problems/algorithm/interesting-game-3-4d4095c9/
