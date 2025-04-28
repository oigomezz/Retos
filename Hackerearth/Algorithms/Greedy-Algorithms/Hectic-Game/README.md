# [Hectic Game][link]

Alice and Bob are playing a hectic game in which there are a total of N tasks each consisting of a start time Si and end time Ei.

Both players take alternate turns, Alice plays first. In each turn, a player chooses the maximum number of tasks that are non-overlapping as both Alice and Bob can perform only one task at a time. In the next turn, the other player will choose the maximum number of tasks that are non-overlapping from the remaining tasks and so on.

Now, both the players will take XOR (Exclusive - OR) of the total tasks count value obtained in each of their turns. Let the value be A for Alice and B for Bob. Now, If A > B, Alice wins. If B > A , Bob wins. If A = B, it's a tie. Find out the winner?

## Input format

- The first line of the input will be T, the total number of test cases.
- The first line of each test case will be N, the total number of tasks.
- Then N lines follow each consisting of two space-separated integers Si and Ei the start time and the end time.

## Output format

For each test case print the respective result Alice, Bob or Tie.

[link]: https://www.hackerearth.com/practice/algorithms/greedy/basics-of-greedy-algorithms/practice-problems/algorithm/hectic-game-2e74ada4/
