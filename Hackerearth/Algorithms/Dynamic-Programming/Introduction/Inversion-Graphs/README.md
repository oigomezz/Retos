# [Inversion graphs][link]

You are given an array A with N elements. You create a graph G with N vertices using A as follows:

- For any pair of indices (i,j) where 1 <= i,j <= N, if A[i] > A[j], then add an undirected edge between vertices i and j.

In graph G, find the maximum possible size of set S (of vertices in G) such that there exists an edge between every pair of vertices that are available in S.

## Input format

- The first line contains an integer N denoting the number of elements in A.
- The second line contains N space-separated integers denoting the elements of A.

## Output format

Among all the vertices available in S, find the maximum possible size of S.

[link]: https://www.hackerearth.com/practice/algorithms/dynamic-programming/introduction-to-dynamic-programming-1/practice-problems/algorithm/inversion-graph-4670b723/
