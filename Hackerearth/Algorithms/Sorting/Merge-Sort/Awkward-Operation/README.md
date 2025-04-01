# [Awkward operation][link]

You are given two sequences a and b consisting of n integers. You may choose any index i (1 < i < n) and simultanously apply the following changes :

- a[i-1] := a[i-1] + a[i]
- a[i] := -a[i]
- a[i+1] := a[i+1] + a[i]

Determine whether you can make array a equal to array b after applying this operation any number of times (possibly zero).

## Input format

- The first line contains one integer t, the number of test cases.
- The first line of each test case contains a single integer n, the number of integers in each sequence.
- The second line of each test case contains n integers A[1], A[2], ..., A[N].
- The third line of each test case contains n integers B[1], B[2], ..., B[N].

## Output format

For each test case, output "Yes" (without quotes) if b can be obtained by applying the aforementioned operation on a any number of times, and "No" (without quotes) otherwise.

[link]: https://www.hackerearth.com/practice/algorithms/sorting/merge-sort/practice-problems/algorithm/awkward-operations-a70ed200/
