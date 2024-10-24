# Bit operations

You are given an array of size N. Initially, all the elements are zero. You are provided with Q queries and each query is one of the following types:

- 1 L R X : For each element in the range [L,R] such as y, set y = y | X.
- 2 L R X : For each element in the range [L,R] like y, set y = y & X.
- 3 L R X : For each element in the range [L,R] like y, set y = y ⊕ X.
- 4 L R : Print the sum of the elements in range [L,R].
- 5 L R: Print the XOR of the elements in range [L,R].

## Input format

- First line: N and Q
- Each of the next N lines: A query

## Output format

For each query of type 4 or 5, print the answer.
