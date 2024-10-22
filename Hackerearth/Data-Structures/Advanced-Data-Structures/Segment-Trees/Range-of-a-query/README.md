# Range of a query

You are given an array A of N integers. You are required to answer Q queries of the following types:

- 1 L R: Choose any two indices i,j such that L <= i <= j <= R and find the maximum possible value of function F(i, j).
- 2 X V: Update the value of the element at index X with V that is set A[X] = V.

Function F(i,j) is defined as follows:

- F(i,j) = 0, if all the elements in the subarray A[i..j] are not equal. Otherwise, F(i,j) = A[i] + max(0, A[i+1]-1) + max(0, A[i+2]-2)+...+max(0, A[j]-j+i)

**Note:** Assume 1-based indexing.

## Input format

- The first line contains two space-separated integers N and Q denoting the number of elements in array A and the number of queries respectively.
- The second line contains N space-separated integers denoting the elements of array A.
- Next Q lines contain three space-separated integers denoting the queries.

## Output format

For every query of type 1 in space-separated format, print the maximum possible value of function F.
