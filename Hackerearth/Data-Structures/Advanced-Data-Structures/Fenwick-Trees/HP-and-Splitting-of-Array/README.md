# HP and Splitting of Array

HP recently started learning about a property called inversion count. An inversion count of an array indicates how far from (or close to) being sorted the array is. If the array is already sorted, the inversion count is 0; if it's sorted in reverse order, the inversion count is maximal.

Formally speaking, two elements A[i] and A[j] form an inversion if A[i] > A[j] and i < j. The inversion count is the number of pairs of indices (i,j) such that A[i] and A[j] form an inversion.

You are given an array A with size N. Let's denote an i-rotation of this array as the array formed by removing the first i elements from the array and adding (appending) them to the end of the array in the same order.

HP wants to know the inversion counts of i-rotations of array A. Compute this inversion count for each i (1 <= i <= N).

## Input format

- The first line of the input contains a single integer T — the number of test cases. Each test case consists of two lines.
- The first line of each test case contains a single integer N denoting the size of the array.
- The second line contains N space-separated integers A1,A2,...,An.

## Output format

For each test case, print a single line containing N space-separated integers. The i-th of these integers should denote the inversion count of the i-rotation of A, for each 1 <= i <= N.
