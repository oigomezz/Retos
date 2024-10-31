# Akash and GCD

Akash is interested in a new function F such that,

F(x) = GCD(1, x) + GCD(2, x) + ... + GCD(x, x)

where GCD is the Greatest Common Divisor.

Now, the problem is quite simple. Given an array A of size N, there are 2 types of queries:

1. C X Y : Compute the value of F( A[X] ) + F( A[X + 1] ) + F( A[X + 2] ) + .... + F( A[Y] ) (mod 10⁹ + 7)
2. U X Y: Update the element of array A[X] = Y

## Input format

- First line of input contain integer N, size of the array.
- Next line contain N space separated integers the elements of A.
- Next line contain integer Q, number of queries.
- Next Q lines contain one of the two queries.

## Output format

For each of the first type of query, output the required sum (mod 10⁹ + 7).
