# [Even Array][link]

An array is called good if every element of the array is an even integer.
You are given an array A of length N. In one move, you can do one of the following operations:

- Choose an index i and set Ai = Ai // 2
- Choose an index 1 <= i <= |A| and replace A[i],A[i+1] with one occurrence of A[i] ⊕ A[i+1]. Here |A| denotes the length of the array A and ⊕ denotes bitwise XOR operation.

Find the minimum number of moves needed to make array A good.

## Input format

- The first line contains T denoting the number of test cases. The description of T test cases is as follows:
- For each test case:
  - The first line contains N denoting the size of array A.
  - The second line contains N space-separated integers A1, A2, ..., An denoting the elements of A.

## Output format

For each test case, print the minimum number of moves needed to make array A good.

[link]: https://www.hackerearth.com/practice/algorithms/dynamic-programming/introduction-to-dynamic-programming-1/practice-problems/algorithm/even-array-2db9e3fc/
