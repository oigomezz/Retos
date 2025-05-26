# [Weak nodes][link]

You are given N nodes with the following information:

- The nodes are connected by M bidirectional edges.
- Each node has a value Vi associated with it.
- A node is called a weak node if the connections between some other nodes are broken when that node is deleted and any alternate connections are not present.

Write a program to tell the number of subsets from all the possible subsets of weak nodes, which on getting their values multiplied gives a number which is divisible by all primes less than 25.

Since the answer can be large, print the answer Modulo 10⁹ + 7.

## Input format

- First line: Two space-separated integers N and M
- Second line: N space-separated integers denoting the values of the nodes.
- Next M lines: Two space-separated integers u and v denoting an edge between u and v.

## Output format

Print the required answer Modulo 10⁹ + 7.

[link]: https://www.hackerearth.com/practice/algorithms/graphs/depth-first-search/practice-problems/algorithm/rhezo-and-super-tanks-a5a3a2f1/
