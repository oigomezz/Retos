# Movement in arrays

Consider an array A of size N. You start from the index 0 and your goal is to reach index N-1 in exactly M moves.

At any index, you can move forward or backward by a number of steps that is equal to a prime divisor of the value which exists at that index. You cannot go beyond the array while going forward or backward.

Write a program to determine whether it is possible to reach index N-1 in M moves.

## Input format

- First line: T (number of test cases)
- First line in each test case: N
- Second line in each test case: N space-separated integers (denoting the array A)
- Third line in each test case: M

## Output format

For each test case, print YES or NO depending upon the result.