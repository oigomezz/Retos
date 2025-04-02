# [Missing Soldiers][link]

An infinite army of ants is marching on an infinite 2-D plane. Since ants are disciplined, here's how they march: each ant chooses exactly one x coordinate and moves along it in positive y direction, starting from (x, 0). There exists exactly one ant for each x coordinate on that plane and hence there are infinite ants!

There are N horizontal barriers lying on this plane. The ith barrier is defined by (xi, yi) and di, which means that the barrier is blocking all ants which want to pass through points lying on line segment connecting (xi, yi) and (xi + di, yi). Once an ant encounters a barrier, it stops moving.

Given all the barriers, your task is to find the total number of ants, that will be ever blocked at some point in their march.

## Input format

- The first line contains an integer N which denotes the number of barriers.
- Next N lines follow, each contains 3 space separated integers, "xi yi di" as explained in problem statement above.

**Note:** The barriers in the input may overlap.

## Output format

Output a single integer, the number of ants that will be ever blocked at some point in their march.

[link]: https://www.hackerearth.com/practice/algorithms/sorting/merge-sort/practice-problems/algorithm/missing-soldiers-december-easy-easy/
