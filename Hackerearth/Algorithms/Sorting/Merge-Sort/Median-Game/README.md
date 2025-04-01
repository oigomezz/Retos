# [Median Game][link]

You are given an array A of N integers. You perform this operation N-2 times: For each contiguous subarray of odd size greater than 2, you find the median of each subarray(Say medians obtained in a move are M1,M2,...,Mk). In each move, you remove the first occurrence of value min(M1,M2,...,Mk) from the original array. After removing the element the array size reduces by 1 and no void spaces are left. For example, if we remove element 2 from the array {1,2,3,4}, the new array will be {1,3,4}.

Print a single integer denoting the sum of numbers that are left in the array after performing the operations. You need to do this for T test cases.

## Input format

- The first line contains T denoting the number of test cases.
- The first line of each test case contains N denoting the number of integers in the array initially.
- The next line contains N space seperated integers denoting A[1], A[2], ..., A[N].

## Output format

Output a single integer denoting the sum of numbers left in the array after performing the operations for each test case on a new line.

[link]: https://www.hackerearth.com/practice/algorithms/sorting/merge-sort/practice-problems/algorithm/median-game-june-easy-19-3722be60/
