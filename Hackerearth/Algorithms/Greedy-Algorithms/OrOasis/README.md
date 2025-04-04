# [OrOasis][link]

Consider an array A with N elements. The task is to identify the shortest possible contiguous subarray where the Bitwise OR of the elements within the subarray equals the Bitwise OR of the elements outside the subarray. Additionally, determine the count of all such minimal-length subarrays that meet this condition.

## Notes

- The subarray of A is a contiguous part of the array A, i. e. the array A[i], A[i+1], ..., A[j] for some 1 <= i <= j <= N.
- If in the given array there exists no such subarray for which the Bitwise OR of the elements within the subarray equals the Bitwise OR of the elements, print a single integer -1.

## Input format

- The first line contains a single integer T, which denotes the number of test cases.
- For each test case:
  - The first line contains N denoting the size of array A.
  - The second line contains N space-separated integers, denoting the elements of A.

## Output format

For each test case, If the answer exists, print 2 integers, where the first one is the shortest possible contiguous subarray where the Bitwise OR of the elements within the subarray equals the Bitwise OR of the elements outside the subarray, & the second one is the count of all such minimal-length subarrays, in a new line, Otherwise If in the given array there exists no such subarray for which the Bitwise OR of the elements within the subarray equals the Bitwise OR of the elements, print a single integer -1, in a new line.

[link]: https://www.hackerearth.com/practice/algorithms/greedy/basics-of-greedy-algorithms/practice-problems/algorithm/oroasis-7e736f17/
