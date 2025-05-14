# [Maximum Weight][link]

Given an undirected graph of N nodes and M edges. Every node has a weight attached to it denoted by an array W.

Select a subset of nodes say S, such that for every edge (u,v) in the above graph there exists either u or v in the subset S.

Let's define weight of set S as X = |S| \* Σ Wi, where i denotes all the nodes present in the subset S and |S| denotes size of subset.

Aim is to minimize X.

**Note:** Calculation of X, will only include distinct elements from the subset, even if it contains duplicate elements.

## Input format

- First line contains two space-separated integers : N and M
- Second line contain N space-separated integers denoting the array W.
- Next M lines contains two space-separated integers u v, denoting an edge between node u and v.

## Output format

- In the first line print an integer denoting the size of the second say Y (maximum value can be N).
- In the next line print Y space separated integers denoting the nodes present in the subset.

[link]: https://www.hackerearth.com/practice/algorithms/graphs/graph-representation/practice-problems/approximate/maximum-weight-534d23a3/
