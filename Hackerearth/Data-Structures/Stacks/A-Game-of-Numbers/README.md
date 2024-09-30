# A Game of Numbers

You are given an array A of N integers. Now, two functions F(X) and G(X) are defined:

- F(X): This is the smallest number Z such that X < Z <= N and A[X] < Z[X]
- G(X): This is the smallest number Z such that X < Z <= N and A[X] > Z[X]

Now, you need to find for each index i of this array G(F(i)), where 1 <= i <= N. If such a number does not exist, for a particular index i, output 1 as its answer. If such a number does exist, output A[G (F(i))].

## Input format

The first line contains a single integer N denoting the size of array A. Each of the next N lines contains a single integer, where the integer on the ith line denotes A[i].

## Output format

Print N space separated integers on a single line, where the ith integer denotes A[G (F(i))] or 1, G(F(i)) if does not exist.
