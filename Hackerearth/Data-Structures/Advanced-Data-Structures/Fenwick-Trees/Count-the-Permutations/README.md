# [Count the permutations][link]

You are given two sequences A and B of length N. Determine the number of different ways to permute the sequence A such that it is lexicographically smaller than the sequence B.

A sequence (X1,X2,...,Xk) is strictly lexicographically smaller than a sequence (Y1,Y2,...,Yk), if there exists an index t (1 <= t <= K)such that:

1. Xt < Yt.
2. Xr = Yr for all 1 <= r < t

A permutation X of A is considered different from another permutation Y of A, if there exists an index i (1 <= i <= N) such that Xi != Yi. For example:

- If A = (1,1,1), then there is only one different permutation of A.
- If A = (1,1,2,2), then there are 6 different permutations of A.

## Input format

- First line: Integer N
- Second line: N integers - A1,A2,...,An
- Third line: N integers - B1,B2,...,Bn

## Output format

Print the remainder of the final answer when divided by 10⁹ + 7.

[link]: https://www.hackerearth.com/practice/data-structures/advanced-data-structures/fenwick-binary-indexed-trees/practice-problems/algorithm/count-the-permutations-06ecd021/
