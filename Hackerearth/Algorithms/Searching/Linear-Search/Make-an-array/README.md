# [Make an array][link]

You are given an array A of length N. You take an array B of length N such that B[i] = 0 for each 1 <= i <= N. You can apply the following operation on B any number of times:

- Choose (N - 1) distinct indices and add 1 to each of those indices.

## Task

Find the number of operations required to convert array B into array A by applying the given operation. Print -1 if it is impossible to do so.

## Function description

Complete the function solve() provided in the editor. This function takes the following two parameters and returns the required answer:

- N: Represents the length of array A.
- A: Represents the array A.

## Input format

**Note:** This is the input format that you must use to provide custom input (available above the Compile and Test button).

- The first line contains T, denoting the number of test cases. T also specifies the number of times you have to run the solve function on a different set of inputs.
- For each test case:
  - The first line contains N, denoting the size of array A.
  - The second line contains N space-separated integers A[1], A[2], ....., A[N], denoting the elements of array A.

## Output format

For each test case, print the number of operations required to convert array B into array A by applying the given operation or -1 if it is impossible to do so.

[link]: https://www.hackerearth.com/practice/algorithms/searching/linear-search/practice-problems/algorithm/make-an-array-85abd7ad/
