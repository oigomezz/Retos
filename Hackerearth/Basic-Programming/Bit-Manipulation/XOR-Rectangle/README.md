# [XOR Rectangle][link]

You have an array of N integers S1, S2, ...,Sn. Consider a N x N matrix such that Aij = Si ⊕ Sj.

Here ⊕ indicates bitwise xor operator.

You have been given Q queries. Each query consists of four integers x1,y1,x2,y2 which denotes a submatrix with (x1,y1) as their top-left corner and (x2,y2) as their bottom-right corner such that x1 <= x2 and y1 <= y2. For each of the query, you have to print summation of all integers lying in queried submatrix.

## Input format

- First line of input consists of integer N.
- Next line consist of N space separated integers denoting array S1,S2,...,Sn.
- Next line consists of integer Q denoting total number of queries.
- Next Q lines consist of four integers x1,y1,x2,y2 denoting the queried submatrix.

## Output format

For each of the query, print a single number in a separate line which denotes summation of all the numbers lying in queried submatrix.

[link]: https://www.hackerearth.com/practice/basic-programming/bit-manipulation/basics-of-bit-manipulation/practice-problems/algorithm/xor-rectangle/
