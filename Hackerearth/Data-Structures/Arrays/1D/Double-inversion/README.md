# Double inversion

Consider a certain permutation of integers from 1 to n as A = {a1,a2,...,an} and reverse of array A as R, that is, R = {an,an-1,...,a1}. You are given the inversions at each position of array A and R as {IA1,IA2,...IAn} and {IR1,IR2,...IRn} respectively.

Find the original array A. If, there are multiple solutions, print any of them. If there is no solution, then print -1.

**Note:** The inversion of array arr for position i is defined as the count of j positions satisfying the following condition arrj > arri and 1 <= j < i.

## Input format

- The first line contains T denoting the number of test cases.
- For each test case:
  - The first line contains n denoting the number of elements.
  - The second line contains the elements {IA1,IA2,...IAn}.
  - The third line contains the elements {IR1,IR2,...IRn}.

## Output format

For each test case, print the array A in the space-separated format or -1 if no solution exists. Each test case should be answered in a new line.
