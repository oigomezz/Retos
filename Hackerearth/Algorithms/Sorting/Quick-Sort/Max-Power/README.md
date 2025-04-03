# [Max Power][link]

Given an array A having N distinct integers.

The power of the array is defined as:

- max(A[i] - A[j]) where 2 <= i <=N.
- for each i, j is the largest index less than i such that A[j] < A[i].

Let's say the array is {1,2,5}, then the power of the array is max((2-1), (5-2)), which simplifies to max(1,3) which is equal to 3.

**Operation Allowed:** If you are allowed to choose any two indices x and y and swap A[x] and A[y], find out the maximum power that can be achieved.

**Note:** You are allowed to perform the above operation at most once.

## Input format

- First line consists of a single integer, T, denoting the number of test cases.
- First line of each test case consists of a single integer, denoting N.
- Second line of each test case consists of N space separated integers denoting the array A.

## Output format

For each test case, print the maximum achievable power on a new line.

[link]: https://www.hackerearth.com/practice/algorithms/sorting/quick-sort/practice-problems/algorithm/increasing-subsequence-fbb63e3c/
