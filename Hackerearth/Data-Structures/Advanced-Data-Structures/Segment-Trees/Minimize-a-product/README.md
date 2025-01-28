# [Minimize a product][link]

You are given an array A of N integers.

Also, you are given Q queries of the following type:

- 1 x v: Change the value of the element at x-th index to v i.e. set A[x] = v.
- 2 l r: Determine the number of pairs (i,j) such that:
  - l <= i < j <= r.
  - A[i] \* A[j] is minimum possible among all such possible pairs of elements.

Your task is to determine the sum of answers for queries of Type 2 over all Q queries.

**Note:** Assume 1-based indexing and the sum can be very large, print the output in modulo 10⁹ + 7.

## Input format

- The first line contains an integer T that denotes the number of test cases.
- For each test case:
  - The first line contains two space-separated integers that denotes N Q.
  - The next line contains N space-separated integers that denotes the array A.
  - The next Q lines contain queries.

## Output format

For each test case, print an integer denoting the sum of the answer for all the queries of Type 2 in a new line.

[link]: https://www.hackerearth.com/practice/data-structures/advanced-data-structures/segment-trees/practice-problems/algorithm/minimize-product-265ce7a0/
