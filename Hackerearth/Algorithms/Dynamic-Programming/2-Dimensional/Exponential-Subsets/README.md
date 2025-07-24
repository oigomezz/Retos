# [Exponential subsets][link]

You are given an integer array A consisting of N elements. Your task is to determine for every element if any of its powers can be expressed as the sum of any subset of array A.

Let S be any subset of A.

Σ Si = A[i]^K where K >= 2.

If it is possible to do for any element, print 1. Otherwise, print 0.

## Input format

- The first line contains T denoting the number of test cases.
- The first line of each test case contains an integer N denoting the number of elements in array A.
- The second line of each test case contains N space-separated integers of array A.

## Output format

For each test case, print a single line of N space-separated integers (0/1). Print 0 if there is no subset such that the sum of that subset is equal to any power greater than 1 of the element at this index. Otherwise, print 1.

[link]: https://www.hackerearth.com/practice/algorithms/dynamic-programming/2-dimensional/practice-problems/algorithm/exponential-subset-f78d066f/
