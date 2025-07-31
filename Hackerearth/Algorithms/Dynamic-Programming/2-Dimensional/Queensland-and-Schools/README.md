# [Queensland and Schools][link]

You have been given 2 arrays A and B each of size N, and an integer X. Now, you need to pick a subset of k indices (maybe with repetitions) (i1,i2,i3,...,ik), such that:

1 <= k <= N

A[i1] + A[i2] + ... + A[ik] <= X

B[i1] + B[i2] + ... + B[ik] is maximized

You need to find and print the maximum possible value of B[i1] + B[i2] + ... + B[ik] such that A[i1] + A[i2] + ... + A[ik] <= X. Can you do it ?

Note that a single index can be picked multiple number of times to be part of the subset (i1,i2,i3,...,ik).

## Input format

- The first line contains a single integer X.
- The next line contains a single integer N.
- Each of the next N lines contains 2 space separated integers, where the integers on the i-th line denote A[i] and B[i].

## Output format

Print the required answer on a single line.

[link]: https://www.hackerearth.com/practice/algorithms/dynamic-programming/2-dimensional/practice-problems/algorithm/queensland-and-schools-1d351e31/
