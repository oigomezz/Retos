# [Pebbles Game][link]

Given 2N pebbles of N different colors, where there exists exactly 2 pebbles of each color, you need to arrange these pebbles in some order on a table. You may consider the table as an infinite 2D plane.

The pebbles need to be placed under some restrictions :

1. You can place a pebble of color X, at a coordinate (X,Y) such that Y is not equal to X, and there exist 2 pebbles of color Y.

In short consider you place a pebble of color i at co-ordinate (X,Y). Here, it is necessary that (i=X),(i!=Y) there exist some other pebbles of color equal to Y.

Now, you need to enclose this arrangement within a boundary , made by a ribbon. Considering that each unit of the ribbon costs M, you need to find the minimum cost in order to make a boundary which encloses any possible arrangement of the pebbles. The ribbon is sold only in units (not in further fractions).

## Input format

- First line consists of an integer T denoting the number of test cases.
- The First line of each test case consists of two space separated integers denoting N and M.
- The next line consists of N space separated integers, where the i-th integer is A[i], and denotes that we have been given exactly 2 pebbles of color equal to A[i]. It is guaranteed that A[i] != A[j], if i != j.

## Output format

Print the minimum cost as asked in the problem in a separate line for each test case.

[link]: https://www.hackerearth.com/practice/algorithms/sorting/merge-sort/practice-problems/algorithm/pebbles-game-1/
