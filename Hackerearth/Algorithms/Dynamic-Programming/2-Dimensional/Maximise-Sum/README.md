# [Maximise Sum][link]

Given an array A of N numbers, and an initially empty array P, you can do operations of 4 types on it:

1. Take the last number of array A, remove it and add it to P.
2. Take the last two numbers of array A (if size of array is greater than 1), remove them and add their product to P.
3. Reverse array A, take the last number of array A, remove it and add it to P.
4. Reverse array A, take the last two numbers of array A (if size of array is greater than 1), remove them and add their product to P.

Note that after each operation, array A becomes smaller and maybe reversed. You need to continue adding elements to array P until the array A has 0 elements. You need to maximise the sum of all the values in array P.

## Input format

- First line contains a single integer N.
- Next line contains N space separated integers denoting the array A.

## Output format

Output the maximum sum of all elements of array P that can be obtained by doing the 4 operations as described above on the array A.

[link]: https://www.hackerearth.com/practice/algorithms/dynamic-programming/2-dimensional/practice-problems/algorithm/maximise-xor-f240c1e1/
