# [Probable winners][link]

There are N players competing in a tournament. Before the start of the tournament, there will be pre-tournament clashes in which all the players must play against each other, the winner in each of these games was noted, and this used to decide the winner of the original tournament.

Now, the tournament has started and all the players will be standing in a line sequentially such as 1,2,3,...,N. To decide the winner, the following operation will be performed for (N-1) times:

- Select any two adjacent players with equal probability. The player who won the pre-tournament game between these two will survive and the other player will be out of the tournament and will be removed from the line.

The player who remains at the end will be declared the winner. Your task is to find the number of players who have a non-zero probability of winning the tournament.

You will be given a two-dimensional matrix C of size N \* N. Element Cij is 1 if Playeri defeats Playerj in the pre-tournament clash and Element Cij is 0 if Playeri gets defeated in the pre-tournament clash. Cij will be 0 when i = j.

## Input format

- The first line contains an integer T denoting the number of test cases.
- The first line of each of the test case contains an integer N denoting the number of players.
- Each of the next N lines contains N integers denoting matrix C.

## Output format

For each test case, print a single line denoting the number of players having a non-zero probability of winning.

[link]: https://www.hackerearth.com/practice/algorithms/dynamic-programming/2-dimensional/practice-problems/algorithm/probable-winners-96715358/
