# [Coutinho][link]

Stevie: "Math is so much fun". Also, finally a player that is still at Liverpool:

You are given a number K expressed as a product of a given array A of N integers. In short, K = ∏ A[i]. Now, in addition, you are also given 2 functions that are :

- G(i) = smallest divisor of number i greater that 1.
- F(i) = 0, if i = 1, else F(i) = 1 + F(i/G(i))

Now, you need to answer Q queries. In each query, you shall be given a single number Y. You need to find the sum of all numbers X, such that K is divisible by X. and F(X) = Y.

As the answer to this can be rather large, print it Modulo 10⁹ + 7.

## Input format

- The first line contains 2 space separated integers N and Q. The next line contains N space separated integers, where the i-th integer denotes A[i].
- Each of the next Q lines contains a single integer Y.

## Output format

Print the answer to each query on a new line Modulo 10⁹ + 7.

[link]: https://www.hackerearth.com/practice/algorithms/dynamic-programming/state-space-reduction/practice-problems/algorithm/coutinho/
