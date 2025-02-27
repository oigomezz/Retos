# Too many numbers

You are given two numbers N and M , you are asked to print an array A such that:

- A[i] is in the range [L:R]
- A is sorted in increasing order
- A[i]%M = N%M
- A[i] != M

But the array may be very large so if the array size is strictly more than K, you will skip the task and print -1

## Input format

- In the first line: n m
- Second line: l r
- Third line: k

## Output format

On the first line print the length of the required array. On the second line print n integers (the required array A) , or print -1 if the required array length is more than K
