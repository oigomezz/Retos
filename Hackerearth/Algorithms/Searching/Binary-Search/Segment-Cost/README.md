# [Segment Cost][link]

You are given an array of integers A of size N. Cost of a segment (L,R) is defined as (A[L] ⊕ A[L+1] ⊕ ... ⊕ A[R-1] ⊕ A[R]) - (where ⊕ denotes the Bitwise XOR operator).

Given a range (x,y), find the smallest subsegment (x',y') such that x <= x'<= y' <= y and its cost is maximum among all the subsegments of (x,y).

If there exists more than answer, print the subsegment with smallest x'.

## Input format

- First line contains an integer N.
- Second line contains N space-separated integers denoting the array A.
- Next line contains two space separated integer x y.

## Output format

Print two space separated integers x' y' denoting the subsegment.

[link]: https://www.hackerearth.com/practice/algorithms/searching/binary-search/practice-problems/algorithm/segment-cost-af31ef0c/
