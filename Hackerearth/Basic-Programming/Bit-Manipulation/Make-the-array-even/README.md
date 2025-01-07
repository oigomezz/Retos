# [Make the array even][link]

You are given an array A of N integers. If you make the array whole using the following operation, then what is the minimum number of operations required to make the entire array even?

**Note:** It can be proved that this is always possible.

Select an index 1 <= i < N and perform operation:

- P=Ai+Ai+1;
- Q=Ai-Ai+1;
- Ai=P;
- Ai+1=Q;

## Input format

- The first line contains an integer T denoting the number of the test cases.
- In each test case:
  - The first line contains an integer N denoting the number of elements in the array.
  - The second line contains N space-separated integers of array A.

## Output format

For each test case print a single line denoting the minimum number of operations required to make the whole array even.

[link]: https://www.hackerearth.com/practice/basic-programming/bit-manipulation/basics-of-bit-manipulation/practice-problems/algorithm/make-even-8ced0d4b/
