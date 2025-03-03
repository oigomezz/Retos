# Monk and BST

Monk as always has brought a new task for Fredo. He asks Fredo to create a Binary Search Tree (BST) with L levels and 2^L - 1 nodes. Let the sum of all node values in the BST be M. He further adds that M should be smallest possible integer greater than S, where S is an integer given by Monk. He states the rules of creating BST as follows:

1. The left sub-tree contains only nodes with values less than or equal to the parent node; the right sub-tree contains only nodes with values greater than the parent node.
2. If a node has level i, then the subtree rooted at that node should have exactly 2^(L-i) number of distinct values in the subtree. Note that it is the number of distinct values in the subtree and not the number of nodes in the subtree.
3. If a is the smallest value in the tree and b is the largest value, then all values from a to b must come atleast once in the tree.

Level of root is 1, next level is 2 and so on.

Now, he will ask two type of queries to Fredo.

- Type 0: Find the closest node to root whose value is equal to val and print path to that node from the root. If root has value equal to val, print "root". Else print "l" when we visit left child of any node and "r" when we visit right child of any node.
- Type 1: Tell the value of k-th node in the tree.

Here 1,2 and so on are node numbers and A,B etc. are values of nodes.

Finally, he will ask Fredo Q queries, each query belonging to one of the types mentioned above. Since, Fredo is new to this concept, help him complete this task.

## Input format

- First line consists of two integers L and S as described in the question.
- Second line consists of Q, denoting the number of queries.
- Each of the following Q lines consists of two integers. The first integer denoting the type of query and second denoting either val or k as described in the queries.

## Output format

For each query, print the required answer in a separate line.
