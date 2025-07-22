# [Maximize Array Function][link]

For array A of N integers we call a function f(A) = Σ i\*Ai

Given array of N integers and in one move you can select a position and delete the array element. Then all elements to the right are shifted to the left by 1 position. For example, given array is [5, 9, 15, 25, 15, 9], if you delete A2 then the array will be [5, 15, 25, 15, 9] and then if you delete A2 the array will be [5, 25,15, 9].

Find the maximum value of f(A) of modified array by performing the above move any number of times (possibly 0).

## Input format

- The first line contains T denoting the number of test cases. The description of each test case is as follows.
  - The first line contains an integer N denoting the number of array elements.
  - The next line contains N space-separated integers.

## Output format

For each test case, print the answer in a new line.

[link]: https://www.hackerearth.com/practice/algorithms/dynamic-programming/2-dimensional/practice-problems/algorithm/maximize-array-function-662cdd83/
