# [Queries problem][link]

You are given an array A of N integers. Now, you are required to process queries of the following two types.

1. pos val: Multiply val to A[pos] i.e. A[pos] = A[pos] \* val.
2. Print an integer X such that the absolute difference between the following two values (A[1] \* A[2] \* ... A[X]) and (A[X+1] \* A[X+2] \* ... A[N]) is minimized. If there are multiple such values of X, then print the smallest one.

## Input format

- First line: N that denotes the number of elements in the array and M that denotes the number of queries.
- Next line: N integers denoting the array.
- Next M lines: Queries of the two types.

## Output format

For each query of the second type, print the answer corresponding to the query.

[link]: https://www.hackerearth.com/practice/algorithms/searching/binary-search/practice-problems/algorithm/an-interesting-partition-problem-june-circuits-18f83691/
