# [Operations on an array][link]

You are given an array of n elements and an integer x. You must perform the following types of operations on the array:

1. Find the index of the K-th occurrence of x in the range l to r (both inclusive). If there are no indexes that satisfy the condition, then print -1.
2. Update the value that is present at the given index.

For each query of type 1, print the index of the K-th occurrence of x.

## Input format

- The first line contains two integers n and x denoting the number of elements and an integer whose index is required respectively.
- The second line contains n integers a[i] denoting the elements of the array.
- The third line contains an integer q denoting the number of queries.
- Next q lines contain the following type of queries:
  - If type is equal to 1, then l, r, and k (refer to the first point of the problem statement).
  - If type is equal to 2, then index and value (refer to the second point of the problem statement)

## Output format

Print q integers as the answer to type 1 queries. If there are no indexes that satisfy the condition, then print -1.

[link]: https://www.hackerearth.com/practice/data-structures/advanced-data-structures/fenwick-binary-indexed-trees/practice-problems/algorithm/kth-element-2-7d970b44/
