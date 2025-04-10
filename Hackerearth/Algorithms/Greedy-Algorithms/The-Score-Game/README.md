# [The score game][link]

You are given an array A of N elements where each element is a pair represented by (X[i], Y[i]).

Bob and Alice play a game where both of them have to pick some elements from the array A. Suppose, Bob picked the elements at index i1,i2,...,iK where K <= N.

- Score(Bob) = Σ (X[j] + Y[j]), where j belongs to i1,i2,...,iK.
- Score(Alice) = Σ X[j], where j belongs to 1,2,...,N excluding i1,i2,...,iK .

Find the minimum number of elements Bob must pick such that the score of Bob is greater than Alice.

**Note:** 1-based indexing is used.

## Input format

- The first line contains an integer T denoting the number of test cases.
- For each test case:
  - The first line contains an integer N.
  - The second line contains N space-separated integers denoting the first element of the pair.
  - The third line contains N space-separated integers denoting the second element of the pair.

## Output format

For each test case, print the minimum number of elements Bob needs to pick to score greater than Alice.

[link]: https://www.hackerearth.com/practice/algorithms/greedy/basics-of-greedy-algorithms/practice-problems/algorithm/score-game-fbf0cd0c/
