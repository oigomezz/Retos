# [One Room to Another][link]

Yatin created an interesting problem for his college juniors. Can you solve it?

Given N rooms, where each room has a one-way door to a room denoted by room[i], where 1 <= i <= N. Find a positive integer K such that, if a person starts from room i, (1 <= i <= N), and continuously moves to the room it is connected to (i.e. room[i]), the person should end up in room i after K steps;

**Note:** The condition should hold for each room.If there are multiple possible values of K modulo (10⁹ + 7), find the smallest one.If there is no valid value of K, output -1.

## Input format

- The first line of the input contains an integer T, the number of testcases.
- For each Testcase:
  - The first line contains an integer N, the number of rooms.
  - The second line contains N spaced integers room[1], room[2], ..., room[N].

## Output format

- Output the smallest positive integer K modulo (10⁹ + 7), satisfying the above-mentioned conditions.
- If there is no such value, output -1.

[link]: https://www.hackerearth.com/practice/algorithms/graphs/graph-representation/practice-problems/algorithm/smallest-trip-length-c5309d9f/
