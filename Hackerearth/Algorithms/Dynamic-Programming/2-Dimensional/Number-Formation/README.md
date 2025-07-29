# [Number formation][link]

You are given an array A of N integers. Each integer is a single digit number in the range [0,9]. You are also given a number K. Now, you need to count how many subsequences of the array A exist such that they form a K digit valid number.

A subsequence of size K is called a valid number if there are no leading zeros in the number formed.

## Notes

- A subsequence of an array is not necessarily contiguous.
- Suppose the given array is 0 1 0 2, then if you choose subsequence to be 002, then it is not a valid 3 digit number. Also, it will not be considered as a single digit number. A valid 3 digit number in the array is 102. Please go through the sample I/O for better understanding.

## Input format

- The first line contains an integer N as input denoting the size of the array.
- Next line contains N space separated integers that denote elements of the array.
- Next line contains an integer K.

## Output format

In the output, you need to print the count of valid K digit numbers modulo 720720.

[link]: https://www.hackerearth.com/practice/algorithms/dynamic-programming/2-dimensional/practice-problems/algorithm/number-formation-1cae96c5/
