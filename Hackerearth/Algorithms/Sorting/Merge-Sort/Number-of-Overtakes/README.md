# [Number of overtakes][link]

A race is organized among N horses of a kingdom. Every horse has a velocity (in m/sec) that is denoted by an array Velocity[] where Velocity[i] represents the velocity of the i-th horse. The indexing of the array is 0-based.

All the horses are standing at different starting positions. The starting position of every horse is represented by an array pos[] where pos[i] denotes the starting position of the i-th horse. The indexing of the array is 0-based. The pos[] array is a permutation of integers 1 to N. A horse who is standing at i position is considered to be ahead of the horse who is standing at position j if and only if i > j.

The finish line of the race is 10^(10⁵) meters ahead. An overtake occurs when horse A, whose starting position is less than horse B, finishes the race earlier than horse B. Your task is to determine the number of overtakes that has occurred during the race.

## Input format

- First line: An integer N denoting the number of horses that are participating in the race.
- Next line: N space-separated integers denoting the velocity of the i-th horse.
- Next line: N space-separated integers denoting the starting position of i-th horse.

**Note:** Array is a permutation of integers 1 to N integers

## Output format

Print a single integer denoting the number of overtakes that has occurred during the race.

[link]: https://www.hackerearth.com/practice/algorithms/sorting/merge-sort/practice-problems/algorithm/overtakes-count-33746e3a/
