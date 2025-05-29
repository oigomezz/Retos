# [Tree and K-Tuple][link]

You have a Tree with N nodes rooted at 1 where i-th node is associated with a value Ai. Now consider the following definition:

K-Tuple: A tuple of K+1 nodes (X1,X2, ... , Xk+1) is a K-Tuple if:

1. Xi is an ancestor of Xi+1 for all 1 <= i <= K.
2. Axi > Axi+1 for all 1 <= i <= K.

Calculate the number of K-Tuples in the tree.

## Input format

- First line contains two integers N and K, the number of nodes in the tree and the value for the Tuple type you need to calculate answer for.
- Next line contains N space separated integers where the i-th integer denotes the value Ai.
- Next N-1 lines contains X and Y denoting that there is an edge between them.

## Output format

Output a single integer mod 10⁹ + 7 denoting the number of K-tuples in the tree.

[link]: https://www.hackerearth.com/practice/algorithms/graphs/depth-first-search/practice-problems/algorithm/tree-and-k-tuple/
