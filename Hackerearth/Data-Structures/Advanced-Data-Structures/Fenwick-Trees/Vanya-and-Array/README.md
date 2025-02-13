# [Vanya and Array][link]

Let's define 2 functions a function F(i) and Val(i,j) for an Array A of size N as follows:

F(i) = Σ Val(i,j)

Val(i,j) = 1 ,if A[i] < A[j], else, Val(i,j) = 0.

Now, Vanya has been given one such array A of size N and an integer K. She needs to find the number of Distinct Unordered Pairs of elements (a,b) in array A such that F(a) + F(b) >= K.

## Input format

- The first line contains 2 space separated integers N and K denoting the size of array A and the integer k from the description given above.
- The next line contains N space separated integers denoting the elements of array A.

## Output format

You need to print the required answer on a single line.

[link]: https://www.hackerearth.com/practice/data-structures/advanced-data-structures/fenwick-binary-indexed-trees/practice-problems/algorithm/vanya-and-array-4/
