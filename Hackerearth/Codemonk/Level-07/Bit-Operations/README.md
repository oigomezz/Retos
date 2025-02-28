# Bit operations

You are given an array of size n. Initially, all the elements of the array are zero. You are given q queries, where each query is of the following type:

- 1 L R X: For each element in the range [L,R] like y, set y = y | X.
- 2 L R X: For each element in the range [L,R] like y, set y = y & X.
- 3 L R X: For each element in the range [L,R] like y, set y = y ⊕ X.
- 4 L R: Print the sum of the elements in the range [L,R].
- 5 L R: Print the result after performing the XOR operation of the elements in the range [L,R].

## Input format

- First line: n, q denoting the size of the array and the number of queries
- Next q lines: A query

## Output format

For each query of type 4 or 5, print the answer.
