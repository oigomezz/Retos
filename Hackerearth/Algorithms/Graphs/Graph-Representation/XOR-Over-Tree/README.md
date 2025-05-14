# [Xor over tree][link]

Given a set of N nodes, where each node has an integer Ai associated with it.

Construct a rooted tree using N nodes which is rooted at node 1, such that the value of the given function Z is maximized.

    Z = ΣΣ F(i,j) where F(i,j) = (S(i,j) ⊕ A[LDA(i,j)]) + (S(i,j) x A[LDA(i,j)])

- ⊕ denotes the bitwise xor operator.
- S(i,j) denotes the number of edges on the simple path between nodes i and j.
- LCA(i,j) denotes the lowest common ancestor of nodes i and j.

## Input format

- First line contains an integer N denoting number of nodes in the tree.
- Next line contains N space separated integers denoting the value of each node i.e. Ai.

## Output format

- Print N - 1 lines where each line contains:
  - Two space separated integers a b denoting an edge between node a and b in the tree.

[link]: https://www.hackerearth.com/practice/algorithms/graphs/graph-representation/practice-problems/approximate/xor-over-tree-29dfb939/
