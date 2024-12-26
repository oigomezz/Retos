# [Benny and Balls][link]

In this problem Benny is looking for your help as usual.

There are N baskets, which are numbered from 0 to N - 1.

In each moment of time exactly, starting with t = 1, one ball appears in xi-th basket, where xi = (a \* x(i-1) + b) % N.

The bottom of the i-th basket opens when there is not less than the p[i] balls in it, all the balls fall out of the basket, and then the bottom of the basket is closed again.

How many times baskets' bottoms will open to the T-th moment of time?

xi = (a \* xi-1 + b) % N;

## Input format

- The first line containts Q - the amount of test cases.
- Each test case consist of three lines:
  - First line contains N
  - Second line contains N numbers p[i]
  - Third line contains x1 , a, b, t

## Output format

Q lines - answers for each case

[link]: https://www.hackerearth.com/practice/basic-programming/implementation/basics-of-implementation/practice-problems/algorithm/benny-and-balls/
