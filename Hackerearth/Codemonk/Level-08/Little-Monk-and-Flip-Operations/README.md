# Little Monk and Flip Operations

Given a tree with N nodes and one integer, a. Each node is numbered from 1 to N. Each node i has an integer, A[i], attached to it. You can perform only one type of operation, i.e.

1. Select a subtree of the given tree which includes the node a.
2. Select a non-negative integer k
3. Flip the k-th least significant bit of the integers attached to each node in the selected subtree.

**Note:** A subtree of a tree T is a tree with both nodes and edges as subsets of nodes and edges of T.

Calculate the minimum number of operations that is required to make all the integers attached to the nodes of the given tree equal to 0.

## Input format

- First line : Two space separated integers N and a.
- Next N-1 lines : Two space separated integers x and y denoting an edge.
- Next line : N space separated integers, denoting A[i]

## Output format

Print the minimum number of operations that is required to make all the integers attached to the nodes of the given tree equal to 0.
