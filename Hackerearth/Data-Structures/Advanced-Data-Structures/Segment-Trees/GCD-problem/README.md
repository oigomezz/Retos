# GCD problem

You are given an array of N integers. A function is defined as follows:

F(i,j) = G.C.D(A[i], A[i+1], ..., A[J])

You are also given Q queries of the form L R. For every query, you must answer the value:

ΣΣ F(i,j)

## Input format

- First line: Two integers N and M denoting the number of elements in the array and queries.
- Next line: N integers,
- Next M lines: Query in the mentioned format

## Output format

For each query print an integer in a new line denoting the answer to that query.
