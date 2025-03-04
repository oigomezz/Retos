# Monk and Number Query

Monk is playing with a Tree T rooted at node 1 consisting of N nodes. Each node has a digit written on it ranging from 0 to 9 inclusive. He has an interesting task for you as follows:

You are given a prime number K that is co-prime to 10 and Q queries to answer. In each query, you shall be given 2 numbers i and j. It is guaranteed that for each query, node i shall be an ancestor of node j or i = j. Now, you need to report if the number formed by writing out the the digits from left to right of each node on the path from i to j inclusive, is divisible by K.

Writing out the digits from left to right implies that the digit written on node i shall be the most significant digit of the number thus formed, and the one written on node j shall be the least significant one.

## Input format

- The first line contains 3 space separated integers denoting N, K and Q.
- The next line contains N space separated integers. where the i-th integer is A[i] and denotes the digit written on node i.
- The next line contains N - 1 space separated integers, where the i-th integer denotes the parent of node i + 1.
- Each of the next Q lines contains 2 space separated integers, denoting the parameters of the i-th query.

## Output format

For the i-th query, print "YES" (without quotes) if the number formed by the parameters of the i-th is divisible by K, else print "NO" (without quotes).
