# [A plane journey][link]

A flight company has to schedule a journey of N groups of people from the same source to the same destination. Here, A[1], A[2], ..., A[N] represents the number of people in each group. All groups are present at the source. The flight company has M planes where B[1], B[2], ..., B[M] represents the capacity of each plane.

You are required to send all groups to destination with the following conditions:

1. Each plane can travel from the Source to Destination with only one group at a time such that capacity of a plane is enough to accommodate all people in that group.
2. All people belonging to the same group travel together.
3. Every plane can make multiple journeys between source and destination.
4. It costs 1 unit of time to travel between source to destination and vice versa.

**Note:** Multiple planes can fly together and also it is not necessary for planes to end their journey at the source.

Determine the minimum time required to send all groups from the source to the destination.

## Input format

- The first line contains two integers N and M.
- The next line contains N space-separated integers A[1], A[2], ..., A[N].
- The next line contains M space-separated integers B[1], B[2], ..., B[M].

## Output format

Print a single integer denoting minimum time required to send all groups to the destination. If it is not possible to perform this operation, then print -1.

[link]: https://www.hackerearth.com/practice/algorithms/searching/binary-search/practice-problems/algorithm/people-carrying-6dd467ed/
