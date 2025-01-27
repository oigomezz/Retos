# [Avoid Maxima-Minima][link]

You are given an array A consisting of N integers.

An index of the array i (1 < i < N )is called :

- local maximum if the element on the ith index is strictly greater than the two adjacent elements (that is, Ai > Ai-1, Ai > Ai+1)
- local minimum if the element on the ith index is strictly less than the two adjacent elements (that is, Ai < Ai-1, Ai < Ai+1).

You want to obtain an array such that it does not contain any local maximums and local minimums. To do that, you can do the following operation any number of times:

- Choose an index i (1 <= i <= |A|) and delete the element A[i] from the array. Here |A| denotes the current length of array A. After each operation, the length of the array decreases by one.

Find the maximum length of the final array A which does not contain any local maximums and local minimums.

## Input format

- The first line contains T denoting the number of test cases. The description of T test cases is as follows:
- For each test case:
  - The first line contains N denoting the size of array A.
  - The second line contains N space-separated integers A[1], A[2], ....., A[N] - denoting the elements of A.

## Output format

For each test case, print the maximum length of the final array A which does not contain any local maximums and local minimums.

[link]: https://www.hackerearth.com/practice/data-structures/advanced-data-structures/segment-trees/practice-problems/algorithm/avoid-maxima-minima-8221ea6c/
