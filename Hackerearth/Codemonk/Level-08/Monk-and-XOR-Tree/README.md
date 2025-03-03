# Monk and XOR Tree

Monk has become a master in graph and trees, so he is ready with a task for you.

Given a Tree T consisting of N nodes rooted at node 1, each node has a value, where the value of the i-th node is A[i].

In addition to the tree, you have also been given an integer K. Now, you need to find in this tree, the number of distinct pairs (i,j) where node i is an ancestor of node j, and the XOR of the values of all nodes lying on the path from i to j is equal to K.

In short, you need to find the number of pairs (i,j), where node i is an ancestor of j, and: ∀x lying on the path from i to j inclusive, ⊕ A[x] = K.

Here, the ⊕ symbol denotes the logical XOR operation.

**Note:** A node x is considered an ancestor of another node y if x is parent of y or x is an ancestor of parent of y. For the purposes of this problem, we consider every node to be an ancestor of itself.

## Input format

- The first line contains 2 space separated integers N and K. The next line contains N space separated integers. where the i-th integer denotes A[i].
- The next line contains N - 1 space separated integers, where the i-th integer denotes the parent of node i + 1.

## Output format

Print the required answer on a single line.
