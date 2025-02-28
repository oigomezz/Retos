# Monk and Operations

Monk is fond of matrices. Today, he created a matrix A of size N x M. He defines four types of operations on the matrix as follows:

1. Add v1 to all elements of a row.
2. Update the value of all elements of a row to v2, i.e., all elements of that row become equal to v2.
3. Add v3 to all elements of a column.
4. Update the value of all elements of a column to v4, i.e., all elements of that column become equal to v4.

He defines a function F(x) as

    F(x)= ΣΣ abs(A[i][j])

where A[i] [j] refers to the j-th cell in the i-th row of matrix A, and abs(x) refers to absolute value of any integer x.

Now, he has defined some restrictions:

1. On any cell of the matrix, at most one operation can be performed. This operation can be of any type.

2. Any type of operation can be used any number of times.

You need to maximize the value of F(x) following these restrictions.

## Input format

- The first line consists of two integers N and M, denoting the number of rows and number of columns in matrix A respectively.
- Each of the following N lines consist of M space-separated integers, where the j-th integer in the i-th line denotes A[i] [j].
- The last line of input consists of four space-separated integers denoting the values of v1, v2, v3 and v4 respectively.

## Output format

The only line of output should consist of the maximum value of F(x).
