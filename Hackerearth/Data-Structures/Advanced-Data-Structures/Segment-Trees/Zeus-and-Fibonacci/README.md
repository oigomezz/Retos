# Zeus and Fibonacci

You are given an array A consisting of N integers. You have to process two types of queries on this array.

- Type 1: Change the ith element to X
- Type 2: Given l and r, calculate: ΣΣ Fib(Σ A[k])

**Note:** Fib(i) is the ith Fibonacci number. Fib(0) = 0, Fib(1) = 1.

## Input format

- First line contains an integer N.
- Next line contains N space separated integers denoting array A.
- Next line contains the integer Q.
- Next Q lines are of the following format:
  - 1 i X: for type 1 query
  - 2 l r: for type 2 query

## Output format

For each type 2 query output the answer modulo 10⁹ + 7 on a new line.
