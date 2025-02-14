# [Rotations and Inversions][link]

Rahul has recently learnt about array inversions. An array a has N integers, indexed from 0 to N - 1. Formally, the number of inversions is the number of pairs (i, j) such that 0 <= i < j < N and a[i] > a[j].

Now, he wants to find the lexicographically smallest left rotation of the array such that number of inversions are maximized. The index of rotation is defined as the number of elements from the front that need to left rotated. For example, given the array with elements a[0], a[1], a[2], ..., a[N - 1], the rotation with index 1 will be a[1], a[2], ..., a[N - 1], a[0]; the rotation with index k will be a[k], a[k + 1], ..., a[N - 1], a[0], ..., a[k - 1].

Note that in case, multiple lexicographically equal rotations are found to have the largest number of inversions, you should print the smallest index of rotation.

An array a of integers is lexicographically smaller than another array b if a[i] = b[i] for all indices 0 ≤ i < k and a[k] < b[k].

## Input format

- The first line shall contain a single integer T, denoting the number of test cases to follow.
- Each of the test cases contain 2 lines each.
  - The first line has an integer N, the size of array and the next line has N integers separated by a single space.

## Output format

You should output exactly T lines, each containing 2 numbers, the selected index for rotation and the maximum number of inversions found, separated by a single space.

[link]: https://www.hackerearth.com/practice/data-structures/advanced-data-structures/fenwick-binary-indexed-trees/practice-problems/algorithm/rotations-and-inversions/
