# [Sum of Sums][link]

Given a undirected tree containing N nodes where i-th node has value a(i). Let us define cost of the tree as C, where:

- C = Σ f(i).
- f(i) = Σ g(j); where j ∈ subtree of i.
- g(j) = Σ a(k); where k ∈ subtree of j.

Find a root of the tree such that the cost of the tree is minimum.

## Input format

- The first line of input contains N, the number of nodes in the tree.
- The second line contains N integers a1, a2, ..., aN, where ai (1 ≤ ai ≤ 10⁶) is the value stored at the i-th node.
- The next N-1 lines contains two integers u and v, meaning that there is an edge connecting u and v.

## Output format

Print two integers, the root of the tree such that the cost of tree is minimum and minimum cost. If there are multiple possible values of root, print the minimum one.

[link]: https://www.hackerearth.com/practice/algorithms/graphs/depth-first-search/practice-problems/algorithm/sum-of-sums/
