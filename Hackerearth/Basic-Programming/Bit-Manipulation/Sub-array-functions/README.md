# [Sub-array functions][link]

You are given an array A containing N integers. The following functions are defined for this array:

- f1(l,r) = XOR of the first M smallest elements in the subarray from l to r, l <= r and r-l+1 >= M.
- f2(l,r) = XOR of the first P largest elements in the subarray from l to r, l <= r and r-l+1 >= P.
- f3(l,r) = f1(l,r) & f2(l,r), l <= r.

Write a program to find l and r such that f3(l,r) is maximum. If there are several values of l and r for which f3(l,r) is maximum, return the one having the largest length. If multiple values still exist, return the one with the smallest l.

## Input format

- First line: T (number of test cases)
- First line in each test case: Three space-separated integers denoting N,M, and P respectively.
- Second line in each test case: N space-separated integers (denoting the array A)

## Output format

For each test case, print three space-separated integers denoting l, r, and f3(l,r).

[link]: https://www.hackerearth.com/practice/basic-programming/bit-manipulation/basics-of-bit-manipulation/practice-problems/algorithm/milly-and-sub-array-83aeedc8/
