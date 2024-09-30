# Good Indices

Given an array of integers A of size N. You can perform the following operation on the array:

- Choose an index i and remove the ith element from A.

For each, i (from 1 to N), output the minimum number of operations such that the integer i becomes greater than BOTH of its neighbours i.e. (A[i] > A[i-1] && A[i] > A[i+1]).

If it is not possible to satisfy the mentioned condition output -1 for that index.

## Input format

- The first line contains T, the number of test cases.
- The first line of all test cases contains N, the number of elements in the array.
- The second line contains N space-separated integers.

## Output format

For every test case, output N integers, where the ith integer represents the minimum number of moves to make the ith index good.
