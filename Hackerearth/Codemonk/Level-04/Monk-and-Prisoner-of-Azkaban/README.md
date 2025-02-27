# Monk and Prisoner of Azkaban

Monk's wizard friend Harry Potter is excited to see his Dad fight Dementors and rescue him and his Godfather Sirius Black. Meanwhile their friend Hermoine is stuck on some silly arrays problem. Harry does not have time for all this, so he asked Monk to solve that problem for Hermoine, so that they can go.

The problem is given an array A having N integers, for each i (1 <= i <= N), find x + y, where x is the largest number less than i such that A[x] > A[i] and y is the smallest number greater than i such that A[y] > A[i]. If there is no x < i such that A[x] > A[i], then take x = -1. Similarly, if there is no y > i such that A[y] > A[i], then take y = -1.

## Input format

- First line consists of a single integer denoting N.
- Second line consists of N space separated integers denoting the array A.

## Output format

Print N space separated integers, denoting x + y for each i (1 <= i <= N)
