# [Update the Array][link]

Given an array A of N integers and an integer K. You can perform the following operation any number of times on the given array:

- Choose an integer x such that 1 <= x <= K.
- Choose any index i such that 1 <= i <= N.
- Update A[i] = x

In different operations, different value of x and i can be chosen.

Your **task** is to count minimum number of operations required such that following conditions are met:

- All elements in array A becomes pairwise distinct.
- Count of array elements with odd value is equal to count of array elements with even value.

If the above conditions cannot be met after any number of operations, return -1.

**Note:**

- Assume 1 Based Indexing is followed.
- Array A is said to have pairwise distinct elements if and only if the value of all the elements in array A is distinct.

## Input format

- The first line contains a single integer T, which denotes the number of test cases. T also specifies the number of times you have to run the minUpdates function on a different set of inputs.
- For each test case:
  - First line contains an integer N.
  - Next line contains N space-separated integers denoting the elements of array A.
  - Next line contains an integer K.

## Output format

For each test case in a new line, print an integer denoting the minimum number of operations required or print -1, if the conditions cannot be met.

[link]: https://www.hackerearth.com/practice/basic-programming/implementation/basics-of-implementation/practice-problems/algorithm/update-the-array-3fcbf307/
