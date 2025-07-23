# [An interesting game][link]

Bob and James are about to play with an array A of N elements with Bob starting the game. In each turn :

- A player selects a non-zero number of elements from A with the same value and removes them from A.

The player whose turn makes array A becomes empty wins the game.

James is very intelligent and he modifies the game a bit. He selects some distinct elements (among those present in A) and removes all other elements which are not selected from A. The game is then played using this modified array.

Find the number of possible subsets of elements that James can select to modify A such that James is bound to win if both the players play optimally.

Consider an empty subset as a valid answer.

Since the number of possible subsets can be large enough, print the answer modulo 10⁹ + 7.

## Input format

- The first line contains an integer T denoting the number of test cases.
- The second line contains an integer N.
- The next line contains N space-separated integers, denoting elements of A.

## Output format

For each test case, print the number of possible subsets satisfying the criteria modulo 10⁹ + 7 in a new line.

[link]: https://www.hackerearth.com/practice/algorithms/dynamic-programming/2-dimensional/practice-problems/algorithm/interesting-game-hard-93f267d9/
