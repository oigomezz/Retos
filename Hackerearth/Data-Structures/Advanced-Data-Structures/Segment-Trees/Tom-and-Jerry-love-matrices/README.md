# Tom and Jerry love matrices

Tom and Jerry are playing with matrices. Jerry gifts Tom with a matrix of size M x N. The matrix element have a unique property that each cell of the matrix has value Aij = X + i + j. Since Tom loves challenges, Jerry will give Tom Q queries. Each of these queries can be of any of the following three types:

1. R C1 C2: Delete the cells in the Row R starting from column C1 and ending at column C2 (1 <= C1 <= C2 <= N, 1 <= R <= M).
2. C R1 R2: Delete the cells in column C starting from row R1 and ending at row R2 (1 <= R1 <= R2 <= M, 1 <= C <= N).
3. K: Take all the remaining elements in the array and sort the elements by their values. Now, return the K-th smallest element. If K is greater than the number of elements remaining, then print -1 (1 <= K <= 10⁹).

You are required to print the output only in case of the queries of type 3. You must help Tom to solve the tasks and answer the queries given by Jerry.

## Input format

- The first line of input contains four integers, M, N, X, and Q. Here, Q is the number of queries and M and N are the dimensions of the matrix.
- The next Q lines contain queries of the type mentioned in the question.
  - 1 A B C for queries of type 1.
  - 2 A B C for queries of type 2.
  - 3 A for queries of type 3.

No two deleted sub rows or subcolumns will intersect, that is the segments queried to be deleted are disjoint.

## Output format

For queries of type 3, print a single integer on a new line corresponding to the answer of that query as mentioned in the question.
