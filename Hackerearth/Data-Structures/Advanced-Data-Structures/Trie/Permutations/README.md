# [Permutations][link]

You are given a permutation A = {a1,a2,...,an} of N integers from 0 to N-1.

You are also given Q queries of the following two forms:

- 1 X Y: Swap(ax,ay)
- 2 L R K: Print MexK(al, ..., ar)

Here, MexK(al, ..., ar) = Kth smallest non-negative integer that is not available in the subarray (al, ..., ar).

You can answer the next query only when you answer the previous one. You must answer these queries online.

## Input format

- First line: A single integer N denoting the number of elements in the permutation.
- Second line: N space-separated integers a1,a2,...,an.
- Next Q lines: Each describing a query

As you are required to respond to the queries online, the queries are encoded.

- A query of the first type is provided in the following format: 1 X Y.
- A query of the second type is provided in the following format: 2 L R K.

## Output format

For each query, print the answer in a single line.

[link]: https://www.hackerearth.com/practice/data-structures/advanced-data-structures/trie-keyword-tree/practice-problems/algorithm/online-k-mex-007daa77/
